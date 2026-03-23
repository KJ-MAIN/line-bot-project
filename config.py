import os
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration
from linebot.v3 import WebhookHandler

# โหลด env
load_dotenv()


class Config:
    def __init__(self):
        # LINE
        self.CHANNEL_ACCESS_TOKEN = self._get("CHANNEL_ACCESS_TOKEN")
        self.CHANNEL_SECRET = self._get("CHANNEL_SECRET")

        # GOOGLE
        self.SPREADSHEET_NAME = self._get("SPREADSHEET_NAME")
        self.SERVICE_ACCOUNT_FILE = self._get("SERVICE_ACCOUNT_FILE")

        # LINE SDK objects
        self.line_config = Configuration(access_token=self.CHANNEL_ACCESS_TOKEN)
        self.handler = WebhookHandler(self.CHANNEL_SECRET)

    def _get(self, key: str) -> str:
        value = os.getenv(key)
        if not value:
            raise ValueError(f"❌ Missing ENV: {key}")
        return value


# ใช้ตัวเดียวทั้งระบบ
config = Config()