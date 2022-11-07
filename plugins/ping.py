from pyrogram import Client, filters


HELP = 'HIIII'



@Client.on_message(filters.command('help'))
async def alive(bot, message):
    buttons = [[
            InlineKeyboardButton('➕ Add Me To Your Group ➕', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
            ],[
            InlineKeyboardButton('🔍 Search Movie', switch_inline_query_current_chat='')
            ],[
            InlineKeyboardButton('❓ Help', callback_data='help'),
            InlineKeyboardButton('ℹ️ About', callback_data='about')
            ],[
            InlineKeyboardButton('❌ Close ❌', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )


