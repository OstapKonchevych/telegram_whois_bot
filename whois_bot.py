from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

TOKEN=""

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Вітаю у системі\nВведи IP адресу і я перевірю whois інформацію та пропінгую її")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Допомога")


@dp.message_handler()
async def echo_message(message: types.Message):
    UID = message.from_user.id
    msg = message.text

    whois_data = os.popen('whois ' + msg).read()
    await message.reply(whois_data)

    ping_status = os.system('ping -c 1 -W 1 ' + msg + ' > /dev/null')
    
    if not ping_status :
        await message.reply("Хост " + msg + ' доступний')
    else :
        await message.reply("Хост " + msg + ' не доступний')



if __name__ == '__main__':
    executor.start_polling(dp)
