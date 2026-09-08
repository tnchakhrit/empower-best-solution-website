// Netlify Function: register-building
// Receives the reminder-registration form, stores it in Supabase, and
// sends a confirmation email to the customer plus a notification to admin.

const SUPABASE_URL = process.env.SUPABASE_URL;
const SUPABASE_SERVICE_ROLE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;
const RESEND_API_KEY = process.env.RESEND_API_KEY;
const ADMIN_EMAIL = process.env.ADMIN_EMAIL;
const FROM_EMAIL = "Empower Best Solution <notify@empowerbestsolution.com>";
const LINE_CHANNEL_ACCESS_TOKEN = process.env.LINE_CHANNEL_ACCESS_TOKEN;

function jsonResponse(statusCode, data) {
  return {
    statusCode,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  };
}

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

exports.handler = async (event) => {
  if (event.httpMethod !== "POST") {
    return jsonResponse(405, { error: "Method not allowed" });
  }

  let payload;
  try {
    payload = JSON.parse(event.body || "{}");
  } catch (e) {
    return jsonResponse(400, { error: "ข้อมูลไม่ถูกต้อง" });
  }

  const { name, phone, email, building_name, building_type, expiry_date, line_user_id } = payload;

  if (!name || !phone || !email || !building_name || !building_type || !expiry_date) {
    return jsonResponse(400, { error: "กรุณากรอกข้อมูลให้ครบทุกช่อง" });
  }

  try {
    // 1. Find existing contact by email, phone, or LINE user ID; else create a new one
    const orConditions = [
      `email.eq.${encodeURIComponent(email)}`,
      `phone.eq.${encodeURIComponent(phone)}`,
    ];
    if (line_user_id) {
      orConditions.push(`line_user_id.eq.${encodeURIComponent(line_user_id)}`);
    }
    const existing = await supabaseRequest(
      `contacts?or=(${orConditions.join(",")})&limit=1`,
      { method: "GET" }
    );

    let contact;
    if (existing && existing.length > 0) {
      contact = existing[0];
      // If this registration came with a LINE user ID that isn't saved yet, link it now
      if (line_user_id && !contact.line_user_id) {
        const updated = await supabaseRequest(
          `contacts?id=eq.${contact.id}`,
          {
            method: "PATCH",
            body: JSON.stringify({ line_user_id }),
          }
        );
        contact = updated[0];
      }
    } else {
      const created = await supabaseRequest("contacts", {
        method: "POST",
        body: JSON.stringify({ name, phone, email, line_user_id: line_user_id || null }),
      });
      contact = created[0];
    }

    // 2. Create the building record
    const buildings = await supabaseRequest("buildings", {
      method: "POST",
      body: JSON.stringify({
        building_name,
        building_type,
        inspection_expiry_date: expiry_date,
      }),
    });
    const building = buildings[0];

    // 3. Link building <-> contact
    await supabaseRequest("building_contacts", {
      method: "POST",
      body: JSON.stringify({
        building_id: building.id,
        contact_id: contact.id,
      }),
    });

    // 4. Compute days remaining
    const days = daysRemaining(expiry_date);
    const dayText =
      days >= 0 ? `อีก ${days} วัน` : `เลยกำหนดมาแล้ว ${Math.abs(days)} วัน`;

    // 5. Confirmation email to the customer
    await sendEmail(
      email,
      "ลงทะเบียนรับการแจ้งเตือนสำเร็จ - Empower Best Solution",
      `
        <div style="font-family:sans-serif; line-height:1.7; color:#333;">
          <h2 style="color:#1E3A28;">ลงทะเบียนสำเร็จ</h2>
          <p>เรียนคุณ ${name},</p>
          <p>ขอบคุณที่ลงทะเบียนรับการแจ้งเตือนกับ Empower Best Solution</p>
          <p>
            <strong>อาคาร:</strong> ${building_name}<br/>
            <strong>ประเภทอาคาร:</strong> ${building_type}<br/>
            <strong>วันหมดอายุ อ.6/ร.1:</strong> ${expiry_date}<br/>
            <strong>สถานะ:</strong> ${dayText} จะถึงกำหนดตรวจสอบ
          </p>
          <p>ทีมงานจะแจ้งเตือนท่านอีกครั้งเมื่อใกล้ถึงกำหนด (90 / 60 / 45 วันก่อนหมดอายุ)</p>
          <p>สอบถามเพิ่มเติม โทร 062-956-5194 หรือ LINE OA @911hrhms</p>
        </div>
      `
    );

    // 6. Notify admin
    await sendEmail(
      ADMIN_EMAIL,
      `มีลูกค้าลงทะเบียนใหม่: ${building_name}`,
      `
        <div style="font-family:sans-serif; line-height:1.7; color:#333;">
          <h2>มีการลงทะเบียนใหม่</h2>
          <p>
            <strong>ชื่อผู้ติดต่อ:</strong> ${name}<br/>
            <strong>เบอร์โทร:</strong> ${phone}<br/>
            <strong>อีเมล:</strong> ${email}<br/>
            <strong>อาคาร:</strong> ${building_name}<br/>
            <strong>ประเภทอาคาร:</strong> ${building_type}<br/>
            <strong>วันหมดอายุ อ.6/ร.1:</strong> ${expiry_date} (${dayText})
          </p>
        </div>
      `
    );

    // 7. LINE push notification (เฉพาะกรณีลงทะเบียนผ่าน LIFF และมี line_user_id)
    if (line_user_id) {
      await pushLineMessage(line_user_id, [
        {
          type: "text",
          text:
            `ลงทะเบียนสำเร็จ ✅\n\n` +
            `อาคาร: ${building_name}\n` +
            `ประเภทอาคาร: ${building_type}\n` +
            `วันหมดอายุ อ.6/ร.1: ${expiry_date}\n` +
            `สถานะ: ${dayText}\n\n` +
            `ทีมงานจะแจ้งเตือนท่านอีกครั้งทางไลน์และอีเมล เมื่อใกล้ถึงกำหนด (90 / 60 / 45 วันก่อนหมดอายุ)`,
        },
      ]);
    }

    return jsonResponse(200, { success: true, days_remaining: days });
  } catch (err) {
    console.error(err);
    return jsonResponse(500, {
      error: "เกิดข้อผิดพลาดในระบบ กรุณาลองใหม่อีกครั้ง",
    });
  }
};
