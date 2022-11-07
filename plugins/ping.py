from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


HELP_TXT = 'HIIII'

@Client.on_message(filters.command('help'))
async def alive(bot, message):
    btn = [[
        InlineKeyboardButton('Contact Me', url='https://t.me/Hansaka_Anuhas')
           ]]
    await message.reply(HELP_TXT, reply_markup=InlineKeyboardMarkup(btn))
