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


def build_ui(data, play_button, show_provider=True):   # 🔥 เปลี่ยนชื่อแล้วนะ
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
                    *([
                        {
                            "type": "image",
                            "url": data.get("provider_icon", ""),
                            "aspectRatio": "1:1",
                            "size": "xs",
                            "flex": 0
                        }
                    ] if show_provider else []),
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
                                    "contents": []
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