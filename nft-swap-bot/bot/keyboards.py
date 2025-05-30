from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('🎁 Мои NFT'))
    kb.add(KeyboardButton('🔄 Создать обмен'))
    kb.add(KeyboardButton('📊 Активные офферы'))
    return kb

def get_approve_kb(offer_id):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("✅ Подтвердить", callback_data=f"approve_{offer_id}"))
    kb.add(InlineKeyboardButton("❌ Отклонить", callback_data=f"reject_{offer_id}"))
    return kb