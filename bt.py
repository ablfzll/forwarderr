import logging
import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from client_kb import mainmenu , editCaption
from databese import create_databese
import sqlite3

ADMIN = 5633358205

create_databese()

API_TOKEN = '5974789843:AAH02Q-kHadvAQ5zr8DzERzE82zhLweuL0Q'

PROXY_URL = 'socks5://127.0.0.1:5454'

conn = sqlite3.connect('bot.db')
cur = conn.cursor()

logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher

bot = Bot(token=API_TOKEN , proxy=PROXY_URL)
# bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(content_types=['video','photo'])

async def echo(message: types.Message):

    if message.content_type == 'photo':
        referal = message
        iD = referal.message_id
        conn.execute(f'INSERT INTO photo (photoid , type) VALUES (?, ?)',(iD, 'photo'))
        conn.commit()
        Message = await bot.copy_message(chat_id='-1001668023072',
                                    from_chat_id=referal.chat.id,
                                    message_id=referal.message_id,caption='hello')


    if message.content_type == 'video':
        referal = message
        iD = referal.message_id
        conn.execute(f'INSERT INTO video (videoid , type) VALUES (?, ?)',(iD, 'video'))
        conn.commit()
        Message = await bot.copy_message(chat_id='-1001668023072',
                                    from_chat_id=referal.chat.id,
                                    message_id=referal.message_id,caption='hello')



@dp.message_handler(commands=['admin'], commands_prefix='!/')
async def send_welcome(message: types.Message):
    print(message)

    user = message.chat
    if user.id == ADMIN:
        m = await bot.send_message(chat_id=ADMIN, text='welcome admin',reply_markup=mainmenu())
            
    else:
        await bot.send_message(chat_id=message.chat.id, text='you not admin')
            


@dp.callback_query_handler(text = ['allphotos' , 'allvidos' , 'caption'])
async def p_v(call: types.CallbackQuery):
    if call.data == 'allphotos':
        cursor = cur.execute("SELECT count(*) from photo")
        countP = cursor.fetchall()[0]
        await call.answer(text=countP , show_alert=True)
    if call.data == 'allvidos':
        cursor = cur.execute("SELECT count(*) from video")
        countV = cursor.fetchall()[0]
        await call.answer(text=countV , show_alert=True)

    if call.data == 'caption':
        await bot.edit_message_text(text='send caption' , chat_id=call.message.chat.id,message_id=call.message.message_id)
        # Chat = await bot.get_chat(call.message.chat.id)

        
        
if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)
