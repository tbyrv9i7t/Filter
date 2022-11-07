from Script import script
from pyrogram import Client, filters

@Client.on_message(filters.command('about_creator'))
async def about_creator(bot, message):
    await message.reply(script.ABOUT_CREATOR)
