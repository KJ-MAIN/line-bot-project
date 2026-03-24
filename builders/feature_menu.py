def build_feature_menu():

    def button(label, text):
        return {
            "type": "button",
            "style": "primary",
            "height": "sm",
            "action": {
                "type": "message",
                "label": label,
                "text": text
            }
        }

    bubble = {
        "type": "bubble",
        "size": "mega",
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "lg",
            "contents": [

                {
                    "type": "text",
                    "text": "🎯 เลือกสไตล์เกม",
                    "weight": "bold",
                    "size": "lg",
                    "align": "center"
                },

                button("💥 แตกหนัก", "โบนัสไทม์ แตกหนัก"),
                button("💰 ถอนเยอะ", "โบนัสไทม์ ถอนเยอะ"),
                button("⭐ แนะนำ", "โบนัสไทม์ แนะนำ"),
                button("🏢 เลือกค่ายเอง", "โบนัสไทม์ เลือกค่ายเอง")

            ]
        }
    }

    return bubble