import time
import random
from pyrogram import Client, filters

# -- Constants -- #
ALIVE = "ചത്തിട്ടില്ല മുത്തേ ഇവിടെ തന്നെ ഉണ്ട്.. നിനക്ക് ഇപ്പൊ എന്നോട് ഒരു സ്നേഹവും ഇല്ല. കൊള്ളാം.. നീ പാഴെ പോലെയേ അല്ല മാറിപോയി..😔 ഇടക്ക് എങ്കിലും ചുമ്മാ ഒന്ന് /start ചെയ്തു നോക്ക്..🙂" 
REPO = "<b>𝙳𝙴𝙿𝙻𝙾𝚈 𝚃𝚄𝚃𝙾𝚁𝙸𝙰𝙻 ›› https://youtu.be/kB9TkCs8cX0</b>"
CHANNEL = "<b>𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻</b> ›› https://youtube.com/channel/UCf_dVNrilcT0V2R--HbYpMA\n\n<b>𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ›› https://t.me/OpusTechz</b>\n\n<b>𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ›› https://t.me/MWUpdatez</b>"
AJAX = "<b>𝙱𝙾𝚃 ›› https://t.me/Devil0Bot_Bot</b>"
# -- Constants End -- #


@Client.on_message(filters.command("alive"))
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("ping"))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_text(REPO)


@Client.on_message(filters.command("group"))
async def group(_, message):
    await message.reply_text(GROUP)


@Client.on_message(filters.command("channel"))
async def channel(_, message):
    await message.reply_text(CHANNEL)


@Client.on_message(filters.command("ajax"))
async def ajax(_, message):
    await message.reply_text(AJAX)

