// Netlify Function: link-line
// ใช้เชื่อม LINE user id เข้ากับผู้ติดต่อที่เคยลงทะเบียนผ่านเว็บฟอร์มไว้แล้ว
// โดยไม่ต้องกรอกข้อมูลซ้ำ — จับคู่ด้วยอีเมลที่เคยลงทะเบียนไว้ (ส่งมาจากหน้า
// thank-you-reminder.html ผ่านลิงก์ LIFF โหมด mode=link)

const SUPABASE_URL = process.env.SUPABASE_URL;
const SUPABASE_SERVICE_ROLE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;
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

  const { email, line_user_id } = payload;
  if (!email || !line_user_id) {
    return jsonResponse(400, { error: "ข้อมูลไม่ครบ" });
  }

  try {
    const contacts = await supabaseRequest(
      `contacts?email=eq.${encodeURIComponent(email)}&limit=1`,
      { method: "GET" }
    );

    if (!contacts || contacts.length === 0) {
      return jsonResponse(404, {
        error: "ไม่พบข้อมูลการลงทะเบียนของอีเมลนี้ กรุณาลงทะเบียนใหม่อีกครั้ง",
      });
    }

    let contact = contacts[0];

    if (contact.line_user_id !== line_user_id) {
      const updated = await supabaseRequest(`contacts?id=eq.${contact.id}`, {
        method: "PATCH",
        body: JSON.stringify({ line_user_id }),
      });
      contact = updated[0];
    }

    // หาอาคารที่ยังผูกกับผู้ติดต่อนี้อยู่ (ยังไม่ยกเลิกรับแจ้งเตือน) เพื่อสรุปให้เห็น
    const links = await supabaseRequest(
      `building_contacts?contact_id=eq.${contact.id}&is_active=eq.true`,
      { method: "GET" }
    );

    let buildingNames = [];
    if (links && links.length > 0) {
      const orFilter = links.map((l) => `id.eq.${l.building_id}`).join(",");
      const buildings = await supabaseRequest(`buildings?or=(${orFilter})`, {
        method: "GET",
      });
      buildingNames = buildings.map((b) => b.building_name);
    }

    await pushLineMessage(line_user_id, [
      {
        type: "text",
        text:
          `เชื่อมบัญชี LINE สำเร็จ ✅\n\n` +
          (buildingNames.length > 0
            ? `อาคารที่จะได้รับแจ้งเตือนผ่าน LINE:\n${buildingNames
                .map((n) => `• ${n}`)
                .join("\n")}`
            : `ระบบจะแจ้งเตือนเมื่อมีอาคารลงทะเบียนไว้กับอีเมลนี้`) +
          `\n\nระบบจะแจ้งเตือนล่วงหน้า 90 / 60 / 45 วันก่อนถึงกำหนดตรวจสอบทาง LINE นี้ค่ะ`,
      },
    ]);

    return jsonResponse(200, { success: true, buildings: buildingNames });
  } catch (err) {
    console.error(err);
    return jsonResponse(500, {
      error: "เกิดข้อผิดพลาดในระบบ กรุณาลองใหม่อีกครั้ง",
    });
  }
};
