// Netlify Function: check-buildings
// ใช้โดยหน้า LIFF "เช็ควันหมดอายุ" — รับ line_user_id แล้วคืนรายการอาคาร
// ที่ผูกกับผู้ติดต่อคนนั้น (ที่ยังไม่ยกเลิกรับแจ้งเตือน) พร้อมจำนวนวันที่เหลือ
// ก่อนถึงกำหนดตรวจสอบอาคารครั้งถัดไป

const SUPABASE_URL = process.env.SUPABASE_URL;
const SUPABASE_SERVICE_ROLE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;

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

function daysRemaining(expiryDate) {
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  const expiry = new Date(expiryDate);
  expiry.setHours(0, 0, 0, 0);
  return Math.round((expiry - today) / (1000 * 60 * 60 * 24));
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

  const { line_user_id } = payload;
  if (!line_user_id) {
    return jsonResponse(400, { error: "ข้อมูลไม่ครบ" });
  }

  try {
    const contacts = await supabaseRequest(
      `contacts?line_user_id=eq.${encodeURIComponent(line_user_id)}&limit=1`,
      { method: "GET" }
    );

    if (!contacts || contacts.length === 0) {
      return jsonResponse(404, {
        error:
          "ยังไม่พบข้อมูลการลงทะเบียนของบัญชี LINE นี้ กรุณาลงทะเบียนอาคารก่อน",
      });
    }

    const contact = contacts[0];

    const links = await supabaseRequest(
      `building_contacts?contact_id=eq.${contact.id}&is_active=eq.true`,
      { method: "GET" }
    );

    if (!links || links.length === 0) {
      return jsonResponse(200, { success: true, buildings: [] });
    }

    const orFilter = links.map((l) => `id.eq.${l.building_id}`).join(",");
    const buildings = await supabaseRequest(`buildings?or=(${orFilter})`, {
      method: "GET",
    });

    const result = buildings
      .map((b) => ({
        building_name: b.building_name,
        building_type: b.building_type,
        expiry_date: b.inspection_expiry_date,
        days_remaining: daysRemaining(b.inspection_expiry_date),
      }))
      .sort((a, b) => a.days_remaining - b.days_remaining);

    return jsonResponse(200, { success: true, buildings: result });
  } catch (err) {
    console.error(err);
    return jsonResponse(500, {
      error: "เกิดข้อผิดพลาดในระบบ กรุณาลองใหม่อีกครั้ง",
    });
  }
};
