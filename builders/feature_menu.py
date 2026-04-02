def build_feature_menu():

    return {
        "type": "carousel",
        "contents": [

            # 🎮 เลือกค่าย
            {
                "type": "bubble",
                "size": "mega",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "paddingAll": "10px",
                    "spacing": "12px",
                    "background": {
                        "type": "linearGradient",
                        "angle": "30deg",
                        "startColor": "#0F2027",
                        "centerColor": "#203A43",
                        "endColor": "#2C5364"
                    },
                    "contents": [
                        {
                            "type": "image",
                            "url": "https://ik.imagekit.io/KJAY/Option/Option1.png",
                            "size": "full",
                            "aspectRatio": "1:1",
                            "aspectMode": "cover",
                            "action": {
                                "type": "message",
                                "text": "ขอเมนูค่ายเกมส์"
                            }
                        },
                        {
                            "type": "text",
                            "text": "🎮 เลือกค่ายเกม 🎮",
                            "weight": "bold",
                            "size": "xl",
                            "align": "center",
                            "color": "#FFFFFF",
                            "style": "italic"
                        },
                        {
                            "type": "text",
                            "text": "เลือกค่ายที่คุณต้องการเล่นด้วยตนเอง\nเพื่ออรรถรสจากค่ายที่คุณรัก",
                            "size": "md",
                            "align": "center",
                            "wrap": True,
                            "color": "#FFF0F5"
                        }
                    ]
                }
            },

            # 💰 ถอนบ่อย
            {
                "type": "bubble",
                "size": "mega",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "paddingAll": "10px",
                    "spacing": "12px",
                    "background": {
                        "type": "linearGradient",
                        "angle": "30deg",
                        "startColor": "#0F2027",
                        "centerColor": "#203A43",
                        "endColor": "#2C5364"
                    },
                    "contents": [
                        {
                            "type": "image",
                            "url": "https://ik.imagekit.io/KJAY/Option/Option2.png",
                            "size": "full",
                            "aspectRatio": "1:1",
                            "aspectMode": "cover",
                            "action": {
                                "type": "message",
                                "text": "เกมส์จ่ายบ่อยถอนไม่พัก"
                            }
                        },
                        {
                            "type": "text",
                            "text": "💰ถอนบ่อยที่สุด💰",
                            "weight": "bold",
                            "size": "xl",
                            "align": "center",
                            "color": "#FFFFFF",
                            "style": "italic"
                        },
                        {
                            "type": "text",
                            "text": "เกมส์ที่จ่ายบ่อยที่สุด\nอาจจะถอนไม่หนักแต่ถอนไม่พักแน่นอน",
                            "size": "md",
                            "align": "center",
                            "wrap": True,
                            "color": "#FFF0F5"
                        }
                    ]
                }
            },

            # 💥 แตกหนัก
            {
                "type": "bubble",
                "size": "mega",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "paddingAll": "10px",
                    "spacing": "12px",
                    "background": {
                        "type": "linearGradient",
                        "angle": "30deg",
                        "startColor": "#0F2027",
                        "centerColor": "#203A43",
                        "endColor": "#2C5364"
                    },
                    "contents": [
                        {
                            "type": "image",
                            "url": "https://ik.imagekit.io/KJAY/Option/Option3.png",
                            "size": "full",
                            "aspectRatio": "1:1",
                            "aspectMode": "cover",
                            "action": {
                                "type": "message",
                                "text": "สถิติแตกหนักที่สุด"
                            }
                        },
                        {
                            "type": "text",
                            "text": "🪙แตกหนักที่สุด🪙",
                            "weight": "bold",
                            "size": "xl",
                            "align": "center",
                            "color": "#FFFFFF"
                        },
                        {
                            "type": "text",
                            "text": "เกมส์สถิติแตกหนักที่สุดคำนวนทุกวัน\nถอนหนักไม่เกรงใจแอดมินเลย",
                            "size": "md",
                            "align": "center",
                            "wrap": True,
                            "color": "#FFF0F5"
                        }
                    ]
                }
            },

            # 🎯 แนะนำ
            {
                "type": "bubble",
                "size": "mega",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "paddingAll": "10px",
                    "spacing": "12px",
                    "background": {
                        "type": "linearGradient",
                        "angle": "30deg",
                        "startColor": "#0F2027",
                        "centerColor": "#203A43",
                        "endColor": "#2C5364"
                    },
                    "contents": [
                        {
                            "type": "image",
                            "url": "https://ik.imagekit.io/KJAY/Option/Option4.png",
                            "size": "full",
                            "aspectRatio": "1:1",
                            "aspectMode": "cover",
                            "action": {
                                "type": "message",
                                "text": "โบนัสไทม์เฉพาะฉันเท่านั้น"
                            }
                        },
                        {
                            "type": "text",
                            "text": "🌟แนะนำเฉพาะฉัน🌟",
                            "weight": "bold",
                            "size": "xl",
                            "align": "center",
                            "color": "#FFFFFF"
                        },
                        {
                            "type": "text",
                            "text": "เกมส์เด็ดที่คัดมาเพื่อคุณโดยเฉพาะ\nอย่ารอช้ารีบตัดสินใจแล้วคลิกเลย",
                            "size": "md",
                            "align": "center",
                            "wrap": True,
                            "color": "#FFF0F5"
                        }
                    ]
                }
            }

        ]
    }