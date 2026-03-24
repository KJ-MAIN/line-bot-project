from providers import PROVIDERS_1, PROVIDERS_2
ALL_PROVIDERS = PROVIDERS_1 + PROVIDERS_2

PROVIDER_LOGOS = {}

for p in ALL_PROVIDERS:
    key = p["name"].upper()
    PROVIDER_LOGOS[key] = p["image"]

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
    
    provider_raw = game.get("provider", "").upper()
    
    # 🔥 normalize ให้ match key
    if "PRAGMATIC" in provider_raw:
        provider_key = "PRAGMATIC"
    
    elif "PSG" in provider_raw:
        provider_key = "PSG PRIMESIGMA"
    
    elif "PGS" in provider_raw:
        provider_key = "PGS PEGASUS"
    
    elif "PG" in provider_raw:
        provider_key = "PG"
    
    elif "JILI" in provider_raw:
        provider_key = "JILI"
    
    elif "NAGA" in provider_raw:
        provider_key = "NAGAGAME"
    
    elif "JOKER" in provider_raw:
        provider_key = "JOKER"
    
    elif "YGG" in provider_raw:
        provider_key = "YGG"
    
    elif "SPADE" in provider_raw:
        provider_key = "SPADE"
    
    elif "RELAX" in provider_raw:
        provider_key = "RELAX"
    
    elif "EVOPLAY" in provider_raw:
        provider_key = "EVOPLAY"
    
    elif "BLUEPRINT" in provider_raw:
        provider_key = "BLUEPRINT"
    
    elif "NEXTSPIN" in provider_raw:
        provider_key = "NEXTSPIN"
    
    elif "ADVANT" in provider_raw:
        provider_key = "ADVANTPLAY"
    
    elif "MIMI" in provider_raw:
        provider_key = "MIMI"
    
    else:
        provider_key = provider_raw
    
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
# 🔹 3. UI LAYER
# =========================
def _build_ui(data, play_button):
    return {
        "type": "bubble",
        "size": "mega",

        "hero": {
            "type": "image",
            "url": data["bg"],
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover"
        },

        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "paddingAll": "5px",

            "background": {
                "type": "linearGradient",
                "angle": "30deg",
                "startColor": "#0F2027",
                "endColor": "#0F2027",
                "centerColor": "#203A43"
            },

            "contents": [

                # 🔹 icon + name
                {
                    "type": "box",
                    "layout": "horizontal",
                    "spacing": "10px",
                    "contents": [
                        {
                            "type": "image",
                            "url": data["icon"],
                            "aspectRatio": "1:1",
                            "size": "xs",
                            "flex": 0
                        },
                        {
                            "type": "image",
                            "url": data.get("provider_icon", ""),
                            "aspectRatio": "1:1",
                            "size": "xxs",
                            "flex": 0
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "flex": 1,
                            "backgroundColor": "#FFFFFF",
                            "borderWidth": "2px",
                            "borderColor": "#000000",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": data["name"],
                                    "weight": "bold",
                                    "size": "md",
                                    "align": "center",
                                    "color": "#1C1C1C",
                                    "wrap": True
                                },
                                {
                                    "type": "text",
                                    "text": data["desc"],
                                    "size": "xxs",
                                    "wrap": True,
                                    "align": "center",
                                    "color": "#1C1C1C"
                                }
                            ]
                        }
                    ]
                },

                # 🔹 stats
                {
                    "type": "box",
                    "layout": "horizontal",
                    "spacing": "5px",
                    "contents": [
                        _badge(data["volatility"], "ความผันผวน"),
                        _badge(data["maxwin"], "รางวัลสูงสุด"),
                        _badge(data["withdraw_text"], "ถอนล่าสุด"),
                        _badge(data["players_text"], "ผู้เล่น")
                    ]
                },

                # 🔹 RTP bar
                {
                    "type": "box",
                    "layout": "vertical",
                    "borderWidth": "2px",
                    "borderColor": "#000000",
                    "cornerRadius": "10px",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "backgroundColor": "#FFFFFF",
                            "height": "16px",
                            "cornerRadius": "10px",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "width": f"{min(data['rtp'], 100)}%",
                                    "height": "16px",
                                    "backgroundColor": "#00FF00",
                                    "contents": []   # 🔥 สำคัญมาก
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "position": "absolute",
                                    "width": "100%",
                                    "height": "16px",
                                    "alignItems": "center",
                                    "justifyContent": "center",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": f"{data['rtp']}%",
                                            "size": "xs",
                                            "weight": "bold",
                                            "align": "center",
                                            "color": "#000000"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },

                # 🔹 play button
                {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#CD0000",
                    "cornerRadius": "20px",
                    "action": {
                        "type": "uri",
                        "uri": "https://member.nupv.life/th"
                    },
                    "contents": [
                        {
                            "type": "image",
                            "url": play_button,
                            "size": "full",
                            "aspectRatio": "4.3:1"
                        }
                    ]
                }

            ]
        }
    }


def _badge(value, label):
    return {
        "type": "box",
        "layout": "vertical",
        "backgroundColor": "#A52A2A",
        "borderWidth": "2px",
        "borderColor": "#000000",
        "contents": [
            {
                "type": "text",
                "text": value,
                "size": "xxs",
                "weight": "bold",
                "align": "center",
                "color": "#FFFFFF"
            },
            {
                "type": "text",
                "text": label,
                "size": "10px",
                "align": "center",
                "color": "#FFFFFF"
            }
        ]
    }


# =========================
# 🔹 4. PUBLIC FUNCTION
# =========================
def build_game_bubble(game, play_button):
    game_id = game.get("name")

    stats = _get_game_stats(game_id)
    data = _format_game_data(game, stats)

    return _build_ui(data, play_button)