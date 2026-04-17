import sys
import os
import requests
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

load_dotenv()

CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")

URL = "https://api.line.me/v2/bot/message/push"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"
}

PROMO_TEST = {
    "type": "flex",
    "altText": "test flex",
    "contents": {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {"type": "text", "text": "🔥 ไนท์คิดถึงครีมมาก", "weight": "bold", "size": "xl"},
                {"type": "text", "text": "ระบบ push ใช้งานได้แล้ว", "wrap": True}
            ]
        }
    }
}

def send(user_id):
    payload = {"to": user_id, "messages": [PROMO_TEST]}
    res = requests.post(URL, headers=HEADERS, json=payload)
    print(res.status_code, res.text)

def test():
    send("U886c807ecb26c36b982f363a9b233328")

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("❌ single / test")
        exit()

    mode = sys.argv[1]

    if mode == "single":
        send(sys.argv[2])

    elif mode == "test":
        test()

    else:
        print("❌ โหมดไม่ถูกต้อง (single / test)")