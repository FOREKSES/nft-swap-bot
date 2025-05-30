from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN, SURIKATISS_ACCOUNT
from keyboards import get_main_kb
import database.crud as crud

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "🔄 Добро пожаловать в NFT Swap Bot!\n"
        "Здесь вы можете обмениваться NFT через гаранта",
        reply_markup=get_main_kb()
    )

@dp.message_handler(text='🎁 Мои NFT')
async def my_nfts(message: types.Message):
    nfts = await crud.get_user_nfts(message.from_user.id)
    if not nfts:
        await message.answer("У вас пока нет NFT")
        return
    
    for nft in nfts:
        await message.answer_photo(
            nft['image_url'],
            caption=f"{nft['name']}\nКоллекция: {nft['collection']}"
        )

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)