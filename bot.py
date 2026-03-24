from flask import Flask, request, abort

from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.webhooks import MessageEvent, TextMessageContent

from linebot.v3.messaging import (
    Configuration, ApiClient, MessagingApi,
    ReplyMessageRequest, FlexMessage, TextMessage,
    FlexContainer
)

import random
import os
import json
from dotenv import load_dotenv

from services.sheets_service import get_games
from builders.game_flex import build_game_bubble, PLAY_BUTTON_IMAGES
from builders.provider_menu import build_provider_carousel
from builders.profile_card import build_profile_bubble
from builders.feature_menu import build_feature_menu

app = Flask(__name__)

import time

user_last_request = {}
COOLDOWN = 3
user_last_games = {}

# ===== โหลด .env =====
load_dotenv()

CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")
CHANNEL_SECRET = os.getenv("CHANNEL_SECRET")

configuration = Configuration(access_token=CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


# =========================
@app.route("/callback", methods=["POST"])
def callback():

    signature = request.headers.get("X-Line-Signature", "")
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"

def pick_smart_random_games(rows, user_id, n=5):
    last_games = user_last_games.get(user_id, [])

    # 🔥 กรองเกมที่เพิ่งแสดง
    filtered = [
        g for g in rows
        if g.get("name") not in last_games
    ]

    # 🔄 fallback ถ้าเหลือน้อย
    if len(filtered) < n:
        filtered = rows

    picks = random.sample(filtered, min(n, len(filtered)))

    # 💾 บันทึกล่าสุด
    user_last_games[user_id] = [g.get("name") for g in picks][:3]

    return picks

# =========================
@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):

    text = (event.message.text or "").strip().lower()
    
    user_id = event.source.user_id
    now = time.time()
    
    last_time = user_last_request.get(user_id, 0)
    
    if now - last_time < COOLDOWN:
        print("⏳ User spam blocked")
        return
    
    user_last_request[user_id] = now

    print("📩 ได้รับข้อความ:", text)

    with ApiClient(configuration) as api_client:

        api = MessagingApi(api_client)

        # ===== เมนูหลัก =====

        if text == "ขอโบนัสไทม์":
        
            flex = build_feature_menu()  # 👈 สร้างใหม่
        
            api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        FlexMessage(
                            alt_text="เลือกประเภทเกม",
                            contents=FlexContainer.from_dict(flex)
                        )
                    ]
                )
            )
            return
            
        # ===== FEATURE: เมนูค่าย (ของเดิม) =====
        elif text == "ขอเมนูค่ายเกมส์":
        
            flex = build_provider_carousel()
        
            api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        FlexMessage(
                            alt_text="เลือกค่ายเกม",
                            contents=FlexContainer.from_dict(flex)
                        )
                    ]
                )
            )
            return

        # ===== FEATURE: ถอนเยอะ =====
        elif text == "ถอนเยอะสุดช่วงเวลานี้":
        
            rows = get_games()
            picks = pick_smart_random_games(rows, user_id, 5)
        
            bubbles = []
            bubbles.append(build_profile_bubble("withdraw"))
        
            buttons = random.sample(PLAY_BUTTON_IMAGES, len(picks))
        
            for g, btn in zip(picks, buttons):
                bubbles.append(build_game_bubble(g, btn, True))
        
            flex_json = {
                "type": "carousel",
                "contents": bubbles
            }
        
            api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        FlexMessage(
                            alt_text="ถอนเยอะ",
                            contents=FlexContainer.from_dict(flex_json)
                        )
                    ]
                )
            )
            return
        
        
        # ===== FEATURE: แตกหนัก =====
        elif text == "สถิติแตกหนักที่สุด":
        
            rows = get_games()
            picks = pick_smart_random_games(rows, user_id, 5)
        
            bubbles = []
            bubbles.append(build_profile_bubble("heavy"))
        
            buttons = random.sample(PLAY_BUTTON_IMAGES, len(picks))
        
            for g, btn in zip(picks, buttons):
                bubbles.append(build_game_bubble(g, btn, True))
        
            flex_json = {
                "type": "carousel",
                "contents": bubbles
            }
        
            api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        FlexMessage(
                            alt_text="แตกหนัก",
                            contents=FlexContainer.from_dict(flex_json)
                        )
                    ]
                )
            )
            return
        
        
        # ===== FEATURE: แนะนำ =====
        elif text == "โบนัสไทม์เฉพาะฉันเท่านั้น":
        
            rows = get_games()
            picks = pick_smart_random_games(rows, user_id, 5)
        
            bubbles = []
            bubbles.append(build_profile_bubble("recommend"))
        
            buttons = random.sample(PLAY_BUTTON_IMAGES, len(picks))
        
            for g, btn in zip(picks, buttons):
                bubbles.append(build_game_bubble(g, btn, True))
        
            flex_json = {
                "type": "carousel",
                "contents": bubbles
            }
        
            api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        FlexMessage(
                            alt_text="แนะนำ",
                            contents=FlexContainer.from_dict(flex_json)
                        )
                    ]
                )
            )
            return           



        # ===== โบนัสไทม์ =====

        if text.startswith("โบนัสไทม์"):

            rows = get_games()

            # แยกชื่อค่าย
            parts = text.split()

            provider = None
            
            show_provider = True
            
            if len(parts) > 1:
                provider = " ".join(parts[1:]).upper()
                show_provider = False   # 🔥 เลือกค่าย → ไม่ต้องโชว์โลโก้

            # กรองเกมตามค่าย
            if provider:
                rows = [
                    g for g in rows
                    if g.get("provider", "").strip().upper() == provider
                ]

            if not rows:

                api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[TextMessage(text="❌ ยังไม่มีเกมในระบบ")]
                    )
                )

                return

            picks = pick_smart_random_games(rows, user_id, 5)
            
            bubbles = []
            
            bubbles.append(build_profile_bubble())
            
            # สุ่มรูปปุ่มแบบไม่ซ้ำ
            buttons = random.sample(PLAY_BUTTON_IMAGES, len(picks))
            
            for g, btn in zip(picks, buttons):
            
                bubble = build_game_bubble(g, btn, show_provider)
            
                bubbles.append(bubble)

            flex_json = {
                "type": "carousel",
                "contents": bubbles
            }

            api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        FlexMessage(
                            alt_text="โบนัสไทม์",
                            contents=FlexContainer.from_dict(flex_json)
                        )
                    ]
                )
            )

            return


# ===== START SERVER =====
if __name__ == "__main__":
    print("🚀 LINE BOT STARTED")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)