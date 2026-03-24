def build_feature_menu():

    bubble = {
        "type": "bubble",
        "size": "mega",
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "12px",
            "paddingAll": "12px",
            "background": {
                "type": "linearGradient",
                "angle": "45deg",
                "startColor": "#6B8E23",
                "centerColor": "#191970",
                "endColor": "#6B8E23"
            },
            "contents": [

                # 🔥 Header
                {
                    "type": "box",
                    "layout": "horizontal",
                    "cornerRadius": "12px",
                    "backgroundColor": "#00FFCC",
                    "borderWidth": "3px",
                    "borderColor": "#FF0000",
                    "paddingAll": "8px",
                    "contents": [
                        {
                            "type": "text",
                            "text": "☯คลิกเลือกฟีเจอร์ที่มีได้เลยค่ะ☯",
                            "weight": "bold",
                            "size": "md",
                            "align": "center",
                            "color": "#000000"
                        }
                    ]
                },

                {
                    "type": "text",
                    "text": "คัดเกมส์ตามตัวเลือกที่ดีที่สุด คลิกเลย!!!",
                    "size": "md",
                    "align": "center",
                    "color": "#FFFFFF"
                },

                {
                    "type": "separator",
                    "margin": "md",
                    "color": "#555555"
                },

                # 🔥 BUTTON GROUP
                {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "10px",
                    "contents": [

                        # ⭐ เลือกค่าย
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "paddingAll": "10px",
                            "cornerRadius": "12px",
                            "backgroundColor": "#8B0000",
                            "borderWidth": "2px",
                            "borderColor": "#00FF7F",
                            "shadow": "md",
                            "action": {
                                "type": "message",
                                "text": "ขอเมนูค่ายเกมส์"
                            },
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "⭐ เลือกค่ายเกม ⭐",
                                    "weight": "bold",
                                    "color": "#FFFFFF",
                                    "size": "md",
                                    "align": "center"
                                }
                            ]
                        },

                        # 💰 ถอนเยอะ
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "paddingAll": "10px",
                            "cornerRadius": "12px",
                            "backgroundColor": "#000000",
                            "borderWidth": "2px",
                            "borderColor": "#00FF7F",
                            "shadow": "md",
                            "action": {
                                "type": "message",
                                "text": "ถอนเยอะสุดช่วงเวลานี้"
                            },
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "💰 ถอนเยอะตอนนี้ 💰",
                                    "weight": "bold",
                                    "color": "#FFFFFF",
                                    "size": "md",
                                    "align": "center"
                                }
                            ]
                        },

                        # 💥 แตกหนัก
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "paddingAll": "10px",
                            "cornerRadius": "12px",
                            "backgroundColor": "#0000FF",
                            "borderWidth": "2px",
                            "borderColor": "#00FF7F",
                            "shadow": "md",
                            "action": {
                                "type": "message",
                                "text": "สถิติแตกหนักที่สุด"
                            },
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "💥 แตกหนักจัดเต็ม 💥",
                                    "weight": "bold",
                                    "color": "#FFFFFF",
                                    "size": "md",
                                    "align": "center"
                                }
                            ]
                        },

                        # 🎯 แนะนำ
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "paddingAll": "10px",
                            "cornerRadius": "12px",
                            "backgroundColor": "#003333",
                            "borderWidth": "2px",
                            "borderColor": "#00FF7F",
                            "shadow": "md",
                            "action": {
                                "type": "message",
                                "text": "โบนัสไทม์เฉพาะฉันเท่านั้น"
                            },
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "🎯 แนะนำสำหรับคุณ 🎯",
                                    "weight": "bold",
                                    "color": "#FFFFFF",
                                    "size": "md",
                                    "align": "center"
                                }
                            ]
                        }

                    ]
                }
            ]
        }
    }

    return bubble