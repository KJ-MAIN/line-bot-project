from datetime import datetime, timedelta

def build_profile_bubble():

    now = datetime.utcnow() + timedelta(hours=7)
    end = now + timedelta(hours=1)

    start_time = now.strftime("%H:%M")
    end_time = end.strftime("%H:%M")

    time_text = f"⏰ รอบเวลา {start_time} - {end_time}"

    bubble = {
        "type": "bubble",
        "size": "mega",

        "hero": {
            "type": "image",
            "url": "https://ik.imagekit.io/KJAY/ascess/profile.png?updatedAt=1774117225954",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover"
        },

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
                    "type": "text",
                    "text": "🔥BONUS TIME LIVE🔥",
                    "weight": "bold",
                    "size": "xl",
                    "align": "center",
                    "color": "#FFD700"
                },

                {
                    "type": "text",
                    "text": time_text,
                    "size": "md",
                    "weight": "bold",
                    "align": "center",
                    "color": "#FFFFFF"
                },

                {
                    "type": "separator",
                    "margin": "md",
                    "color": "#555555"
                },

                {
                    "type": "text",
                    "text": "🟢 วิเคราะห์ข้อมูลแบบเรียลไทม์🟢",
                    "size": "md",
                    "weight": "bold",
                    "align": "center",
                    "color": "#00E676"
                },

                {
                    "type": "text",
                    "text": "📊 อัปเดตล่าสุด : ไม่เกิน 5 นาที",
                    "size": "sm",
                    "weight": "bold",
                    "align": "center",
                    "color": "#FFFFFF"
                },

                {
                    "type": "separator",
                    "margin": "md",
                    "color": "#555555"
                },

                {
                    "type": "box",
                    "layout": "vertical",
                    "cornerRadius": "12px",
                    "paddingAll": "5px",

                    "background": {
                        "type": "linearGradient",
                        "angle": "0deg",
                        "startColor": "#80D8D7",
                        "centerColor": "#DEC2E0",
                        "endColor": "#607CAB"
                    },

                    "contents": [
                        {
                            "type": "text",
                            "text": "รีบตัดสินใจก่อนจะหมดเวลาโบนัสไทม์",
                            "size": "sm",
                            "weight": "bold",
                            "align": "center",
                            "color": "#000000"
                        }
                    ]
                }

            ]
        }
    }

    return bubble