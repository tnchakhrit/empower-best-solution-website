// Netlify Function: contact-message
// รับข้อมูลจากฟอร์ม "ส่งข้อความถึงเรา" ในหน้าติดต่อเรา (contact.html)
// เก็บ record ไว้ใน Supabase (ตาราง contact_messages) และส่งอีเมลแจ้งทีมงาน
// โดยใช้หัวข้ออีเมลที่ต่างจากอีเมล "มีลูกค้าลงทะเบียนใหม่" ของฟอร์มลงทะเบียนรับแจ้งเตือน
// เพื่อให้แยกออกจากกันได้ง่ายตอนเปิดอินบ็อกซ์

const SUPABASE_URL = process.env.SUPABASE_URL;
const SUPABASE_SERVICE_ROLE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;
const RESEND_API_KEY = process.env.RESEND_API_KEY;
const ADMIN_EMAIL = process.env.ADMIN_EMAIL;
const FROM_EMAIL = "Empower Best Solution <notify@empowerbestsolution.com>";

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

  // กันสแปมแบบเดียวกับ honeypot field ของ Netlify Forms เดิม
  if (payload["bot-field"]) {
    return jsonResponse(200, { success: true });
  }

  const { name, phone, email, building_name, message } = payload;

  if (!name || !phone || !email) {
    return jsonResponse(400, { error: "กรุณากรอกชื่อ เบอร์โทร และอีเมลให้ครบ" });
  }

  try {
    // 1. บันทึกลง Supabase
    await supabaseRequest("contact_messages", {
      method: "POST",
      body: JSON.stringify({
        name,
        phone,
        email,
        building_name: building_name || null,
        message: message || null,
      }),
    });

    // 2. แจ้งทีมงานทางอีเมล (หัวข้อต่างจากอีเมลลงทะเบียนรับแจ้งเตือน)
    await sendEmail(
      ADMIN_EMAIL,
      `มีข้อความติดต่อใหม่จากเว็บไซต์ - ${name}`,
      `
        <div style="font-family:sans-serif; line-height:1.7; color:#333;">
          <h2 style="color:#1E3A28;">มีข้อความติดต่อใหม่จากหน้าเว็บไซต์</h2>
          <p>
            <strong>ชื่อผู้ติดต่อ:</strong> ${name}<br/>
            <strong>เบอร์โทร:</strong> ${phone}<br/>
            <strong>อีเมล:</strong> ${email}<br/>
            ${building_name ? `<strong>ชื่ออาคาร:</strong> ${building_name}<br/>` : ""}
          </p>
          ${message ? `<p><strong>รายละเอียดที่ต้องการปรึกษา:</strong><br/>${message.replace(/\n/g, "<br/>")}</p>` : ""}
        </div>
      `
    );

    return jsonResponse(200, { success: true });
  } catch (err) {
    console.error(err);
    return jsonResponse(500, {
      error: "เกิดข้อผิดพลาดในระบบ กรุณาลองใหม่อีกครั้ง",
    });
  }
};
