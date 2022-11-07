from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


HELP = 'HIIII'

@Client.on_message(filters.command('help'))
async def alive(bot, message):
    buttons = [[
        InlineKeyboardButton('HIII', url='https://github.com/Hansaka-Anuhas/Filter-Bot/blob/master/plugins/pm_filter.py')
           ]]
    await message.reply(HELP, reply_markup = InlineKeyboardMarkup(buttons))
