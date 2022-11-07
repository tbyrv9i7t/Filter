from pyrogram import Client, filters


HELP = 'HIIII'



@Client.on_message(filters.command('help'))
async def alive(bot, message):
    await message.reply_text(HELP)
    reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton('❤️‍🔥 Please Share and Support ❤️‍🔥', url=f'https://t.me/share/url?url=https://t.me/{temp.U_NAME}')
                ]]
            ),


