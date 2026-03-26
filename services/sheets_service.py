

import os
import json
import gspread
import time
from google.oauth2.service_account import Credentials

from config import config


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# 🔥 โหลด JSON จาก ENV
service_account_info = json.loads(os.getenv("SERVICE_ACCOUNT_JSON"))

creds = Credentials.from_service_account_info(
    service_account_info,
    scopes=SCOPES
)

gc = gspread.authorize(creds)

# ===== worksheets =====
games_ws = gc.open(config.SPREADSHEET_NAME).worksheet("games")
users_ws = gc.open(config.SPREADSHEET_NAME).worksheet("users")


# ===== CACHE =====
_games_cache = None
_games_by_provider = {}
_cache_time = 0
CACHE_TTL = 300


# ===== functions =====
def get_games():
    global _games_cache, _cache_time, _games_by_provider   # 🔥 เพิ่มตัวนี้

    now = time.time()

    if _games_cache is None or now - _cache_time > CACHE_TTL:
        try:
            # ✅ โหลดครั้งเดียวพอ
            rows = games_ws.get_all_records()

            _games_cache = [r for r in rows if r.get("name")]

            # 🔥 สร้าง index แยก provider
            from utils.provider_mapper import map_provider

            provider_map = {}

            for g in _games_cache:
                raw = g.get("provider", "")
                key = map_provider(raw)

                if key not in provider_map:
                    provider_map[key] = []

                provider_map[key].append(g)

            # ✅ เก็บ index
            _games_by_provider = provider_map

            _cache_time = now

            print("📥 โหลด games จาก Google Sheet (refresh cache)")

        except Exception as e:
            print("❌ โหลด Google Sheet ไม่ได้:", e)

            if _games_cache:
                print("⚠️ ใช้ cache เดิมแทน")
                return _games_cache

            return []

    return _games_cache
    
def get_games_by_provider(provider):
    if not _games_by_provider:
        get_games()

    return _games_by_provider.get(provider, [])
    
def save_user(user_id, line_name, picture_url, text):

    from datetime import datetime

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        rows = users_ws.get_all_records()
    except:
        rows = []

    username = None

    # 🔥 ตรวจว่า user พิมพ์ nv ไหม
    if text.startswith("nv"):
        username = text

    # 🔍 หา user เดิม
    for i, row in enumerate(rows):

        if row.get("user_id") == user_id:

            # ✅ update last_active
            users_ws.update_cell(i+2, 5, now)

            # ✅ update last_action
            users_ws.update_cell(i+2, 6, text)

            # ✅ update username (ถ้ามี nv)
            if username:
                users_ws.update_cell(i+2, 4, username)

            return

    # ➕ user ใหม่
    users_ws.append_row([
        user_id,
        line_name,
        picture_url,
        username or "",
        now,
        text
    ])