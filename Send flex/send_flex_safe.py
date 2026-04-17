import sys
import os
import time
import requests
from dotenv import load_dotenv

# =========================
# 📌 FIX PATH (สำคัญ)
# =========================
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

load_dotenv()

CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")

if not CHANNEL_ACCESS_TOKEN:
    raise Exception("❌ Missing CHANNEL_ACCESS_TOKEN")

URL = "https://api.line.me/v2/bot/message/push"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"
}

# =========================
# 🎯 FLEX TEMPLATE
# =========================
PROMO_TEST = {
    "type": "flex",
    "altText": "test flex",
    "contents": {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "🔥 TEST SUCCESS",
                    "weight": "bold",
                    "size": "xl"
                },
                {
                    "type": "text",
                    "text": "ระบบ push ใช้งานได้แล้ว",
                    "wrap": True
                }
            ]
        }
    }
}

# =========================
# 📤 SEND FUNCTION
# =========================
def send_flex(user_id, flex):
    payload = {
        "to": user_id,
        "messages": [flex]
    }

    try:
        res = requests.post(URL, headers=HEADERS, json=payload, timeout=10)
        print(f"📤 {user_id} -> {res.status_code}")

        if res.status_code != 200:
            print("⚠️", res.text)

    except Exception as e:
        print("❌ error:", e)


# =========================
# 🚀 TEST MODE
# =========================
def test():
    user_id = "U886c807ecb26c36b982f363a9b233328"
    send_flex(user_id, PROMO_TEST)


# =========================
# ▶️ MAIN
# =========================
if __name__ == "__main__":

    args = sys.argv

    if len(args) < 2:
        print("❌ use: single / test")
        exit()

    mode = args[1]

    # =========================
    # 🟢 TEST
    # =========================
    if mode == "test":
        print("🧪 TEST MODE")
        test()

    # =========================
    # 🟢 SINGLE USER
    # =========================
    elif mode == "single":

        if len(args) < 3:
            print("❌ ต้องใส่ user_id")
            exit()

        user_id = args[2]

        print("📤 sending to:", user_id)
        send_flex(user_id, PROMO_TEST)

    else:
        print("❌ unknown mode")