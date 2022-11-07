from pyrogram import Client, filters


@Client.on_message(filters.command("alive"))
async def check_alive(_, message):
    await message.reply_text('hii')
