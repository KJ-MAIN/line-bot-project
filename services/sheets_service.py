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


# ===== CACHE =====
_games_cache = None
_cache_time = 0
CACHE_TTL = 300


# ===== functions =====
def get_games():
    global _games_cache, _cache_time

    now = time.time()

    if _games_cache is None or now - _cache_time > CACHE_TTL:
        try:
            rows = games_ws.get_all_records()
            _games_cache = [r for r in rows if r.get("name")]
            _cache_time = now

            print("📥 โหลด games จาก Google Sheet (refresh cache)")

        except Exception as e:
            print("❌ โหลด Google Sheet ไม่ได้:", e)

            if _games_cache:
                print("⚠️ ใช้ cache เดิมแทน")
                return _games_cache

            return []

    return _games_cache