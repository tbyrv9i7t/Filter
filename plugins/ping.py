from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

HELP = 'HIIII'



@Client.on_message(filters.command('help'))
async def alive(bot, message):
    btn = [[InlineKeyboardButton('HIII', url='https://github.com/Hansaka-Anuhas/Filter-Bot/blob/master/plugins/pm_filter.py')
           ]]
    await message.reply("I couldn't find anything related to that\nDid you mean any one of these?",
                    reply_markup=InlineKeyboardMarkup(btn))


