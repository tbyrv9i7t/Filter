from pyrogram import Client, filters


HELP = 'HIIII'
GROUP = 


@Client.on_message(filters.command('help'))
async def alive(bot, message):
    await message.reply_text(HELP)
    reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton('❤️‍🔥 Please Share and Support ❤️‍🔥', url=f'https://t.me/share/url?url=https://t.me/{temp.U_NAME}')
                ]]
            ),


@Client.on_message(filters.command(''))
async def alive(bot, message):
    await message.reply_text(GROUP)


@Client.on_message(filters.command('alive'))
async def alive(bot, message):
    await message.reply_text(ALIVE)
