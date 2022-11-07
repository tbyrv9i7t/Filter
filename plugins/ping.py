from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


HELP = 'HIIII'

@Client.on_message(filters.command('help'))
async def alive(bot, message):
    btn = [[
        InlineKeyboardButton('Contact Me', url='https://t.me/Hansaka_Anuhas')
           ]]
    await message.reply.photo(photo'https://telegra.ph/file/6cdc6dee747e610adc994.jpg', reply_markup=InlineKeyboardMarkup(btn))
