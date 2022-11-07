from pyrogram import Client, filters


ABOUT_CREATOR = 'Full Name: Hansaka Anuhas\nAge: 16\nLive in: Sri Lanka 🇱🇰'

@Client.on_message(filters.command('about_creator'))
async def about_creator(bot, message):
    await message.reply_text(ABOUT_CREATOR)
