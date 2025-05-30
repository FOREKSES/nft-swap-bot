from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
COMMISSION_PERCENT = 0.02  # 2% комиссия
MIN_COMMISSION = 0.5       # Минимум 0.5 TON
SURIKATISS_ACCOUNT = "@surikatisss"
