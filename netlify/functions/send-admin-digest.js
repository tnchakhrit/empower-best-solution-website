// Netlify Scheduled Function: send-admin-digest
// รันทุกวัน แต่จะส่งอีเมลจริงเฉพาะวันที่ 10, 20 และวันสุดท้ายของเดือนเท่านั้น
// (เช็คจากเวลาไทย ไม่ใช่เวลา UTC ของเซิร์ฟเวอร์)
//
// สรุปรายชื่ออาคารทั้งหมดที่ใกล้ถึงกำหนดตรวจสอบอาคาร (อ.6/ร.1) ภายใน 150 วัน
// ส่งเป็นอีเมลสรุปให้ทีมงาน (ไม่ใช่อีเมลลูกค้า) แบ่งเป็น 4 ช่วง:
// ≤ 60 วัน, 61-90 วัน, 91-120 วัน, 121-150 วัน
// พร้อมชื่อผู้ติดต่อ/เบอร์โทร เพื่อให้ทีมงานติดต่อเสนอราคารอบถัดไปได้สะดวก

const SUPABASE_URL = process.env.SUPABASE_URL;
const SUPABASE_SERVICE_ROLE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;
const RESEND_API_KEY = process.env.RESEND_API_KEY;
const FROM_EMAIL = "Empower Best Solution <notify@empowerbestsolution.com>";
const ADMIN_EMAIL = "empower.bestsolution2024@gmail.com";

const BANDS = [
  { label: "ใกล้ครบกำหนดมาก (ไม่เกิน 60 วัน)", min: 0, max: 60 },
  { label: "61 - 90 วัน", min: 61, max: 90 },
  { label: "91 - 120 วัน", min: 91, max: 120 },
  { label: "121 - 150 วัน", min: 121, max: 150 },
];

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
}

// เวลาปัจจุบันแบบเวลาไทย (UTC+7) — เซิร์ฟเวอร์ของ Netlify รันเป็น UTC
function nowInThailand() {
  return new Date(Date.now() + 7 * 60 * 60 * 1000);
}

function isSendDay(dateTH) {
  const day = dateTH.getUTCDate(); // ใช้ getUTCDate เพราะ dateTH ถูกเลื่อนมาแล้วด้วยมือ
  if (day === 10 || day === 20) return true;
  const tomorrow = new Date(dateTH);
  tomorrow.setUTCDate(dateTH.getUTCDate() + 1);
  return tomorrow.getUTCDate() === 1; // วันนี้เป็นวันสุดท้ายของเดือน
}

function daysRemaining(expiryDateStr, todayTH) {
  const today = new Date(
    Date.UTC(todayTH.getUTCFullYear(), todayTH.getUTCMonth(), todayTH.getUTCDate())
  );
  const expiry = new Date(expiryDateStr + "T00:00:00Z");
  return Math.round((expiry - today) / 86400000);
}

function formatThaiDate(dateStr) {
  try {
    const d = new Date(dateStr + "T00:00:00Z");
    return d.toLocaleDateString("th-TH-u-ca-buddhist", {
      year: "numeric",
      month: "long",
      day: "numeric",
      timeZone: "UTC",
    });
  } catch (e) {
    return dateStr;
  }
}

exports.handler = async (event) => {
  const todayTH = nowInThailand();
  const forceTest = !!(event && event.queryStringParameters && event.queryStringParameters.force === "true");

  if (!isSendDay(todayTH) && !forceTest) {
    console.log("send-admin-digest: ไม่ใช่วันที่ต้องส่ง ข้ามรอบนี้");
    return { statusCode: 200, body: JSON.stringify({ success: true, sent: false, reason: "not a send day" }) };
  }

  try {
    const buildings = await supabaseRequest("buildings?select=*", { method: "GET" });

    const inRange = buildings
      .map((b) => ({ ...b, days_remaining: daysRemaining(b.inspection_expiry_date, todayTH) }))
      .filter((b) => b.days_remaining >= 0 && b.days_remaining <= 150);

    if (inRange.length === 0) {
      console.log("send-admin-digest: ไม่มีอาคารที่ใกล้ครบกำหนดในช่วงนี้");
      return { statusCode: 200, body: JSON.stringify({ success: true, sent: false, reason: "no buildings in range" }) };
    }

    // ดึงรายชื่อผู้ติดต่อที่ยังผูกอยู่ (is_active) ของแต่ละอาคารที่เข้าเงื่อนไข
    for (const b of inRange) {
      const links = await supabaseRequest(
        `building_contacts?building_id=eq.${b.id}&is_active=eq.true`,
        { method: "GET" }
      );
      const contactIds = (links || []).map((l) => l.contact_id);
      if (contactIds.length === 0) {
        b.contacts = [];
        continue;
      }
      const orFilter = contactIds.map((id) => `id.eq.${id}`).join(",");
      const contacts = await supabaseRequest(`contacts?or=(${orFilter})`, { method: "GET" });
      b.contacts = contacts || [];
    }

    const bandSections = BANDS.map((band) => {
      const items = inRange
        .filter((b) => b.days_remaining >= band.min && b.days_remaining <= band.max)
        .sort((a, b2) => a.days_remaining - b2.days_remaining);
      return { ...band, items };
    }).filter((section) => section.items.length > 0);

    const totalCount = inRange.length;

    const sectionsHtml = bandSections
      .map((section) => {
        const rowsHtml = section.items
          .map((b) => {
            const contactsText =
              b.contacts && b.contacts.length > 0
                ? b.contacts
                    .map((c) => `${c.name || "-"}${c.phone ? ` (${c.phone})` : ""}`)
                    .join(", ")
                : "ไม่มีผู้ติดต่อ";
            return `
              <tr>
                <td style="padding:8px 10px; border-bottom:1px solid #E4DCC8;">${b.building_name}</td>
                <td style="padding:8px 10px; border-bottom:1px solid #E4DCC8;">${b.building_type || "-"}</td>
                <td style="padding:8px 10px; border-bottom:1px solid #E4DCC8; white-space:nowrap;">${formatThaiDate(b.inspection_expiry_date)}</td>
                <td style="padding:8px 10px; border-bottom:1px solid #E4DCC8; white-space:nowrap; text-align:center;">${b.days_remaining} วัน</td>
                <td style="padding:8px 10px; border-bottom:1px solid #E4DCC8;">${contactsText}</td>
              </tr>
            `;
          })
          .join("");
        return `
          <h3 style="font-family:sans-serif; color:#1E3A28; margin:24px 0 8px;">${section.label} (${section.items.length} อาคาร)</h3>
          <table style="width:100%; border-collapse:collapse; font-family:sans-serif; font-size:13.5px; color:#333;">
            <thead>
              <tr style="background:#F7F2E3;">
                <th style="padding:8px 10px; text-align:left;">ชื่ออาคาร</th>
                <th style="padding:8px 10px; text-align:left;">ประเภท</th>
                <th style="padding:8px 10px; text-align:left;">วันหมดอายุ</th>
                <th style="padding:8px 10px; text-align:center;">เหลือ</th>
                <th style="padding:8px 10px; text-align:left;">ผู้ติดต่อ</th>
              </tr>
            </thead>
            <tbody>${rowsHtml}</tbody>
          </table>
        `;
      })
      .join("");

    const todayLabel = formatThaiDate(
      `${todayTH.getUTCFullYear()}-${String(todayTH.getUTCMonth() + 1).padStart(2, "0")}-${String(todayTH.getUTCDate()).padStart(2, "0")}`
    );

    await sendEmail(
      ADMIN_EMAIL,
      `สรุปอาคารใกล้ครบกำหนดตรวจสอบ (${totalCount} อาคาร) - ${todayLabel}`,
      `
        <div style="font-family:sans-serif; line-height:1.7; color:#333;">
          <h2 style="color:#1E3A28;">สรุปอาคารใกล้ครบกำหนดตรวจสอบอาคาร</h2>
          <p>ประจำวันที่ ${todayLabel} — พบอาคารที่ใกล้ครบกำหนดภายใน 150 วัน ทั้งหมด ${totalCount} อาคาร</p>
          ${sectionsHtml}
        </div>
      `
    );

    console.log(`send-admin-digest: ส่งสรุปอาคาร ${totalCount} รายการไปที่ ${ADMIN_EMAIL}`);
    return { statusCode: 200, body: JSON.stringify({ success: true, sent: true, count: totalCount }) };
  } catch (err) {
    console.error(err);
    return { statusCode: 500, body: JSON.stringify({ error: String(err) }) };
  }
};
