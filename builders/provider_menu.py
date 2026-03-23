from providers import PROVIDERS_1, PROVIDERS_2


# ===== ปุ่ม provider =====
def build_provider_button(label, provider, image):

    return {
        "type": "box",
        "layout": "vertical",
        "flex": 1,
        "cornerRadius": "14px",
        "backgroundColor": "#0C1A2B",
        "borderWidth": "1px",
        "borderColor": "#FFD54F",
        "shadow": "md",

        "action": {
            "type": "message",
            "text": f"โบนัสไทม์ {provider}"
        },

        "contents": [

            {
                "type": "box",
                "layout": "vertical",
                "backgroundColor": "#091E36",
                "paddingAll": "2px",

                "contents": [
                    {
                        "type": "text",
                        "text": label,
                        "size": "xs",
                        "weight": "bold",
                        "color": "#FFD54F",
                        "align": "center",
                        "wrap": False
                    }
                ]
            },

            {
                "type": "image",
                "url": image,
                "aspectRatio": "1:1",
                "aspectMode": "cover",
                "size": "full"
            }

        ]
    }


# ===== จัด layout 3-3-2 =====
def build_provider_rows(providers):

    rows = []

    row1 = []
    for p in providers[0:3]:
        row1.append(build_provider_button(p["label"], p["name"], p["image"]))

    row2 = []
    for p in providers[3:6]:
        row2.append(build_provider_button(p["label"], p["name"], p["image"]))

    row3 = []
    for p in providers[6:8]:
        row3.append(build_provider_button(p["label"], p["name"], p["image"]))

    rows.append({
        "type": "box",
        "layout": "horizontal",
        "spacing": "8px",
        "contents": row1
    })

    rows.append({
        "type": "box",
        "layout": "horizontal",
        "spacing": "8px",
        "contents": row2
    })

    rows.append({
        "type": "box",
        "layout": "horizontal",
        "spacing": "8px",
        "contents": row3
    })

    return rows


# ===== สร้าง bubble =====
def build_provider_bubble(providers):

    rows = build_provider_rows(providers)

    return {
        "type": "bubble",
        "size": "mega",

        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "12px",
            "paddingAll": "5px",
            "cornerRadius": "20px",

            "background": {
                "type": "linearGradient",
                "angle": "45deg",
                "startColor": "#DCEAF6",
                "centerColor": "#0F4C81",
                "endColor": "#DCEAF6"
            },

            "contents": [

                {
                    "type": "box",
                    "layout": "vertical",
                    "paddingAll": "10px",
                    "cornerRadius": "12px",

                    "background": {
                        "type": "linearGradient",
                        "angle": "0deg",
                        "startColor": "#0B223D",
                        "endColor": "#123A63"
                    },

                    "borderWidth": "1px",
                    "borderColor": "#1E88E5",

                    "contents": [
                        {
                            "type": "text",
                            "text": "SELECT GAME PROVIDER",
                            "weight": "bold",
                            "size": "md",
                            "align": "center",
                            "color": "#FFFFFF"
                        }
                    ]
                },

                {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "8px",
                    "contents": rows
                }

            ]
        }
    }


# ===== รวมเป็น carousel =====
def build_provider_carousel():

    bubble1 = build_provider_bubble(PROVIDERS_1)
    bubble2 = build_provider_bubble(PROVIDERS_2)

    return {
        "type": "carousel",
        "contents": [bubble1, bubble2]
    }