// Netlify Function: line-webhook
// Receives events from LINE Messaging API (follow / unfollow / message / postback)
// Verifies the request is genuinely from LINE, then reacts to each event.

const crypto = require("crypto");

const LINE_CHANNEL_SECRET = process.env.LINE_CHANNEL_SECRET;
const LINE_CHANNEL_ACCESS_TOKEN = process.env.LINE_CHANNEL_ACCESS_TOKEN;

function isValidSignature(rawBody, signature) {
  if (!signature || !LINE_CHANNEL_SECRET) return false;
  const hash = crypto
    .createHmac("SHA256", LINE_CHANNEL_SECRET)
    .update(rawBody)
    .digest("base64");
  return hash === signature;
}

async function replyMessage(replyToken, messages) {
  try {
    const res = await fetch("https://api.line.me/v2/bot/message/reply", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${LINE_CHANNEL_ACCESS_TOKEN}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ replyToken, messages }),
    });
    if (!res.ok) {
      const text = await res.text();
      console.error("LINE reply error:", res.status, text);
    }
  } catch (err) {
    console.error("LINE reply request failed:", err);
  }
}

async function handleEvent(event) {
  if (event.type === "follow") {
    await replyMessage(event.replyToken, [
      {
        type: "template",
        altText: "ยินดีต้อนรับสู่ Empower Best Solution - กดลงทะเบียนอาคารเพื่อรับแจ้งเตือนฟรี",
        template: {
          type: "buttons",
          text:
            "ยินดีต้อนรับสู่ Empower Best Solution\n\n" +
            "กดปุ่มด้านล่างเพื่อลงทะเบียนอาคาร รับแจ้งเตือนก่อนถึงกำหนดตรวจสอบอาคารฟรี",
          actions: [
            {
              type: "uri",
              label: "ลงทะเบียนอาคาร",
              uri: "https://liff.line.me/2011500534-lO4GZZ0d",
            },
          ],
        },
      },
    ]);
    return;
  }

  if (event.type === "unfollow") {
    // ผู้ใช้บล็อก/ลบเพื่อน OA — ยังไม่มีการผูก LINE user ID กับข้อมูลลูกค้า
    // (จะทำในขั้นตอนสร้าง LIFF) ตอนนี้แค่บันทึก log ไว้ก่อน
    console.log("Unfollow event from userId:", event.source && event.source.userId);
    return;
  }

  // เหตุการณ์อื่นๆ (message, postback ฯลฯ) ยังไม่ต้องทำอะไรในตอนนี้
  console.log("Unhandled LINE event type:", event.type);
}

exports.handler = async (event) => {
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, body: "Method not allowed" };
  }

  const signature =
    event.headers["x-line-signature"] || event.headers["X-Line-Signature"];
  const rawBody = event.body || "";

  if (!isValidSignature(rawBody, signature)) {
    console.error("Invalid LINE signature");
    return { statusCode: 401, body: "Invalid signature" };
  }

  let payload;
  try {
    payload = JSON.parse(rawBody);
  } catch (e) {
    return { statusCode: 400, body: "Invalid JSON" };
  }

  const events = payload.events || [];
  await Promise.all(events.map(handleEvent));

  return { statusCode: 200, body: "OK" };
};
