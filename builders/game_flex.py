from builders.game_ui import build_ui

from utils.provider_mapper import map_provider

from providers import PROVIDERS_1, PROVIDERS_2
ALL_PROVIDERS = PROVIDERS_1 + PROVIDERS_2

PROVIDER_LOGOS = {}

for p in ALL_PROVIDERS:
    key = p["name"].upper()
    PROVIDER_LOGOS[key] = p["image"]
    
PLAY_BUTTON_IMAGES = [
    "https://res.cloudinary.com/dn9xnmoqx/image/upload/v1773603242/paly1.png",
    "https://res.cloudinary.com/dn9xnmoqx/image/upload/v1773603242/paly2.png",
    "https://res.cloudinary.com/dn9xnmoqx/image/upload/v1773603241/paly3.png",
    "https://res.cloudinary.com/dn9xnmoqx/image/upload/v1773603241/play4.png",
    "https://res.cloudinary.com/dn9xnmoqx/image/upload/v1773608200/play5.png"
]    

import random
from datetime import datetime

# ===== memory stats =====
GAME_STATS = {}

# =========================
# 🔹 1. LOGIC LAYER (stats)
# =========================
def _get_game_stats(game_id):
    today = datetime.now().strftime("%Y-%m-%d")

    if game_id not in GAME_STATS or GAME_STATS[game_id]["date"] != today:
        GAME_STATS[game_id] = {
            "withdraw": random.randint(20000, 60000),
            "players": random.randint(1000, 3000),
            "date": today
        }

    # เพิ่มค่า
    GAME_STATS[game_id]["players"] += random.randint(30, 120)
    GAME_STATS[game_id]["withdraw"] += random.randint(200, 20000)

    return GAME_STATS[game_id]


# =========================
# 🔹 2. FORMAT LAYER
# =========================
def _format_game_data(game, stats):
    rtp_raw = str(game.get("rtp", "0")).replace("%", "")
    
    try:
        base_rtp = float(rtp_raw)
    
        # 🔥 เพิ่ม dynamic offset (เนียน ๆ)
        offset = random.uniform(-0.5, 0.5)
    
        rtp_num = round(base_rtp + offset, 2)
        
        rtp_num = max(90, min(rtp_num, 99.5))
    
    except:
        rtp_num = 0
    
    provider_raw = game.get("provider", "")
    provider_key = map_provider(provider_raw)
    

    
    provider_icon = PROVIDER_LOGOS.get(provider_key, "")

    return {
    
        "provider": provider_key,
        "provider_icon": provider_icon,
        "name": game.get("name", "Unknown Game"),
        "desc": game.get("description", "-"),
        "bg": game.get("bg_url"),
        "icon": game.get("icon_url"),
        "volatility": game.get("volatility", "HIGH"),
        "maxwin": game.get("maxwin", "5000X"),
    
        # 🔥 แก้ตรงนี้
        "rtp": rtp_num,
        "bar": f"{rtp_num}%",
    
        "withdraw_text": f"💰{stats['withdraw']:,}฿",
        "players_text": f"{stats['players']:,} คน"
    }

# =========================
# 🔹 4. PUBLIC FUNCTION
# =========================
def build_game_bubble(game, play_button):
    game_id = game.get("name")

    stats = _get_game_stats(game_id)
    data = _format_game_data(game, stats)

    return build_ui(data, play_button)