import logging
from oxfordTj import getDefinition
from googletrans import Translator
translator = Translator()
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5613206020:AAGOAlu7vWWaJ54Ln0kpywdSr46vfjug8_U'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply('Botdan foydalanish uchun ushbu kanalga azo buling https://t.me/mahsulot_com va kanaldan chiqb ketmang aks holda botdan foydalana olmaysiz ')

@dp.message_handler(commands='help')
async def send_welcome(message: types.Message):
    await message.reply("Botdan nima hohlisiz Vahaaka band edila yetkazib qo'yaman")



@dp.message_handler()
async def tarjimon(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if lang=='en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text

        lookup = getDefinition(word_id)
        if lookup:
            await message.reply(f"Word: {word_id} \nDefinitions:\n{lookup['definitions']}")
            if lookup.get('audio'):
                await message.reply_voice(lookup['audio'])
        else:
            await message.reply("Bunday so'z topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)