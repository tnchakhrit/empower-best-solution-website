// Netlify Scheduled Function: send-reminders
// รันอัตโนมัติทุกวัน เช็คอาคารทั้งหมดว่าใกล้ถึงกำหนดตรวจสอบ (อ.6/ร.1) หรือยัง
// ถ้าเหลือ 90 / 60 / 45 วัน (หรือน้อยกว่า) ให้ส่งแจ้งเตือนทางอีเมลและ LINE
// ไปหาผู้ติดต่อที่ยังผูกกับอาคารนั้น (และยังไม่ได้ยกเลิกรับแจ้งเตือน)
// โดยจะส่งแต่ละระยะ (90/60/45) แค่ครั้งเดียวต่อ 1 อาคาร ต่อ 1 ผู้ติดต่อ
// (เช็คจากตาราง notification_log กันการส่งซ้ำ)
//
// นอกจากนี้ ถ้าอาคารเลยกำหนดตรวจสอบมาแล้ว 180 วัน (และยังไม่เคยอัปเดตวันหมดอายุ
// ใหม่ในระบบ) จะส่งข้อความเตือนให้อัปเดตข้อมูลอาคารอีก 1 ครั้ง (ครั้งเดียว ไม่ส่งซ้ำ)

const SUPABASE_URL = process.env.SUPABASE_URL;
const SUPABASE_SERVICE_ROLE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;
const RESEND_API_KEY = process.env.RESEND_API_KEY;
const FROM_EMAIL = "Empower Best Solution <notify@empowerbestsolution.com>";
const LINE_CHANNEL_ACCESS_TOKEN = process.env.LINE_CHANNEL_ACCESS_TOKEN;

// เรียงจากระยะไกลไปใกล้ เพื่อให้ log สร้างตามลำดับที่อ่านง่าย
const THRESHOLDS = [
  { days: 90, noticeType: "90_day" },
  { days: 60, noticeType: "60_day" },
  { days: 45, noticeType: "45_day" },
];

const OVERDUE_UPDATE_DAYS = 180;
const OVERDUE_UPDATE_NOTICE_TYPE = "overdue_update_180";

async function supabaseRequest(path, options) {
  const res = await fetch(`${SUPABASE_URL}/rest/v1/${path}`, {
    ...options,
    headers: {
      apikey: SUPABASE_SERVICE_ROLE_KEY,
      Authorization: `Bearer ${SUPABASE_SERVICE_ROLE_KEY}`,
      "Content-Type": "application/json",
      Prefer: "return=representation",
      ...(options && options.headers ? options.headers : {}),
    },
  });
  const text = await res.text();
  const data = text ? JSON.parse(text) : null;
  if (!res.ok) {
    throw new Error(`Supabase error (${res.status}): ${text}`);
  }
  return data;
}

async function sendEmail(to, subject, html) {
  try {
    const res = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${RESEND_API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ from: FROM_EMAIL, to, subject, html }),
    });
    if (!res.ok) {
      const text = await res.text();
      console.error("Resend error:", res.status, text);
    }
  } catch (err) {
    console.error("Resend request failed:", err);
  }
}

async function pushLineMessage(userId, messages) {
  if (!userId || !LINE_CHANNEL_ACCESS_TOKEN) return;
  try {
    const res = await fetch("https://api.line.me/v2/bot/message/push", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${LINE_CHANNEL_ACCESS_TOKEN}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ to: userId, messages }),
    });
    if (!res.ok) {
      const text = await res.text();
      console.error("LINE push error:", res.status, text);
    }
  } catch (err) {
    console.error("LINE push request failed:", err);
  }
}

function daysRemaining(expiryDateStr) {
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  const expiry = new Date(expiryDateStr + "T00:00:00");
  return Math.round((expiry - today) / 86400000);
}

exports.handler = async () => {
  let sentCount = 0;

  try {
    const buildings = await supabaseRequest("buildings?select=*", {
      method: "GET",
    });

    for (const building of buildings) {
      const days = daysRemaining(building.inspection_expiry_date);

      let dueThresholds;
      if (days >= 0) {
        dueThresholds = THRESHOLDS.filter((t) => days <= t.days);
      } else if (days <= -OVERDUE_UPDATE_DAYS) {
        // เลยกำหนดมาแล้วอย่างน้อย 180 วัน — เตือนให้อัปเดตข้อมูลอาคาร (ครั้งเดียว)
        dueThresholds = [{ noticeType: OVERDUE_UPDATE_NOTICE_TYPE, kind: "overdue" }];
      } else {
        dueThresholds = []; // เลยกำหนดแล้วแต่ยังไม่ถึง 180 วัน หรือยังไม่ถึง 90 วันก่อนหมดอายุ
      }
      if (dueThresholds.length === 0) continue;

      const links = await supabaseRequest(
        `building_contacts?building_id=eq.${building.id}&is_active=eq.true`,
        { method: "GET" }
      );
      if (!links || links.length === 0) continue;

      for (const link of links) {
        const contacts = await supabaseRequest(
          `contacts?id=eq.${link.contact_id}&limit=1`,
          { method: "GET" }
        );
        const contact = contacts && contacts[0];
        if (!contact) continue;

        for (const threshold of dueThresholds) {
          const existingLog = await supabaseRequest(
            `notification_log?building_id=eq.${building.id}&contact_id=eq.${contact.id}&notice_type=eq.${threshold.noticeType}&limit=1`,
            { method: "GET" }
          );
          if (existingLog && existingLog.length > 0) continue; // เคยส่งแล้ว ข้าม

          const isOverdueUpdate = threshold.kind === "overdue";
          const dayText = `อีก ${days} วัน`;
          const updateFormUrl = "https://empowerbestsolution.com/reminder-program.html#reminder-form";

          if (contact.email) {
            await sendEmail(
              contact.email,
              isOverdueUpdate
                ? `แจ้งเตือน: กรุณาอัปเดตข้อมูลอาคาร ${building.building_name}`
                : `แจ้งเตือน: ${building.building_name} ใกล้ถึงกำหนดตรวจสอบอาคาร (เหลือ ${days} วัน)`,
              isOverdueUpdate
                ? `
                  <div style="font-family:sans-serif; line-height:1.7; color:#333;">
                    <h2 style="color:#1E3A28;">กรุณาอัปเดตข้อมูลอาคาร</h2>
                    <p>เรียนคุณ ${contact.name},</p>
                    <p>อาคาร <strong>${building.building_name}</strong> เลยกำหนดตรวจสอบอาคาร (อ.6/ร.1) ที่เคยแจ้งไว้ในระบบมาแล้วกว่า ${OVERDUE_UPDATE_DAYS} วัน (วันหมดอายุเดิม: ${building.inspection_expiry_date})</p>
                    <p>หากท่านดำเนินการตรวจสอบและได้รับใบรับรองฉบับใหม่แล้ว กรุณาอัปเดตวันหมดอายุใหม่ในระบบ เพื่อให้เราแจ้งเตือนล่วงหน้าได้ถูกต้อง</p>
                    <p>หากยังไม่ได้ดำเนินการตรวจสอบ สามารถติดต่อทีมงานเพื่อขอรับบริการได้เช่นกัน</p>
                    <p><a href="${updateFormUrl}" style="color:#1E3A28; font-weight:600;">อัปเดตข้อมูลอาคาร</a></p>
                    <p>สอบถามเพิ่มเติม โทร 062-956-5194 หรือ LINE OA @911hrhms</p>
                  </div>
                `
                : `
                  <div style="font-family:sans-serif; line-height:1.7; color:#333;">
                    <h2 style="color:#1E3A28;">แจ้งเตือนล่วงหน้า</h2>
                    <p>เรียนคุณ ${contact.name},</p>
                    <p>อาคาร <strong>${building.building_name}</strong> ของท่านใกล้ถึงกำหนดตรวจสอบอาคารประจำปีแล้ว</p>
                    <p>
                      <strong>ประเภทอาคาร:</strong> ${building.building_type}<br/>
                      <strong>วันหมดอายุ อ.6/ร.1:</strong> ${building.inspection_expiry_date}<br/>
                      <strong>สถานะ:</strong> ${dayText} จะถึงกำหนด
                    </p>
                    <p>กรุณาเตรียมความพร้อมสำหรับการตรวจสอบอาคารครั้งถัดไป หรือติดต่อทีมงานเพื่อขอรับบริการ</p>
                    <p>สอบถามเพิ่มเติม โทร 062-956-5194 หรือ LINE OA @911hrhms</p>
                  </div>
                `
            );
          }

          if (contact.line_user_id) {
            await pushLineMessage(contact.line_user_id, [
              {
                type: "text",
                text: isOverdueUpdate
                  ? `กรุณาอัปเดตข้อมูลอาคาร 📋\n\n` +
                    `อาคาร: ${building.building_name}\n` +
                    `เลยกำหนดตรวจสอบมาแล้วกว่า ${OVERDUE_UPDATE_DAYS} วัน (วันหมดอายุเดิม: ${building.inspection_expiry_date})\n\n` +
                    `หากตรวจสอบและได้ใบรับรองใหม่แล้ว กรุณาอัปเดตวันหมดอายุใหม่ในระบบด้วยนะคะ หรือหากยังไม่ได้ตรวจสอบ ติดต่อทีมงานเพื่อขอรับบริการได้เลยค่ะ`
                  : `แจ้งเตือนล่วงหน้า ⏰\n\n` +
                    `อาคาร: ${building.building_name}\n` +
                    `วันหมดอายุ อ.6/ร.1: ${building.inspection_expiry_date}\n` +
                    `สถานะ: ${dayText}\n\n` +
                    `กรุณาเตรียมความพร้อมสำหรับการตรวจสอบอาคารครั้งถัดไป หรือติดต่อทีมงานเพื่อขอรับบริการค่ะ`,
              },
            ]);
          }

          await supabaseRequest("notification_log", {
            method: "POST",
            body: JSON.stringify({
              building_id: building.id,
              contact_id: contact.id,
              notice_type: threshold.noticeType,
            }),
          });

          sentCount++;
        }
      }
    }

    console.log(`send-reminders: ส่งแจ้งเตือนไปทั้งหมด ${sentCount} รายการ`);
    return {
      statusCode: 200,
      body: JSON.stringify({ success: true, sent: sentCount }),
    };
  } catch (err) {
    console.error(err);
    return { statusCode: 500, body: JSON.stringify({ error: String(err) }) };
  }
};
