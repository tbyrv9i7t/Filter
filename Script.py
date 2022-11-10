class script(object):
    START_TXT = """<b>👋 හෙලෝ {},

මට පුළුවන් Movies සහ TV Series ඔයා වෙනුවෙන් දෙන්න... 🥳

ඔයාට කරන්න තියෙන්නේ මාව Group එකකට Add කරලා මට Admin දෙන්න විතරයි... 😌

ඉතුරු හරිය මං බලා ගන්නම්.... 😎</b>"""

    HELP_TXT = """Help"""

    ABOUT_TXT = """★ My Name: <a href=https://t.me/{}>{}</a>
★ Creator: <a href=https://t.me/Hansaka_Anuhas>Hansaka Anuhas</a> 🇱🇰
★ Bot Server: <a href=https://www.heroku.com>Heroku</a>
★ Database: <a href=https://www.mongodb.com>MongoDB</a>"""

    FILTERS_TXT = """Filters"""

    MANUALFILTERS_TXT = """<b><u>Manual Filters</u></b>

<b>Commands and Usage:</b>
• /filter - Add Filter
• /filters - List All Filters
• /del - Delete Filter
• /delall - Delete All Filters"""

    BUTTONS_TXT = """<b><u>Buttons</u></b>

<b>URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/{})</code>

<b>Alert Buttons:</b>
<code>[Button Text](buttonalert:Alert Message)</code>"""

    AUTOFILTERS_TXT = """<b><u>Auto Filters</u></b>

<b>භාවිතයට උපදෙස්:</b>
<b>1. ඔයාට Movies හරි TV Series හරි Channel එකක් තියෙනවනම්, මාව ඒකට Add කරලා මට Admin දෙන්න.
2. ඔයාගේ Channel එකේ ඔයාට කැමති Message එකක් මට Forward කරන්න.
3. ඉතුරු හරිය මං බලා ගන්නම්.</b>"""

    CONNECTIONS_TXT = """<b><u>Connections</u></b>

<b>Commands and Usage:</b>
• /connect - Connect PM
• /disconnect - Disconnect PM
• /connections - List All Connections"""

    EXTRAMODS_TXT = """<b><u>Extra Mods</u></b>

<b>Commands and Usage:</b>
• /id - User ID
• /info - User Informations
• /imdb or /search - IMDb Movie Informations
• /status - Bot Database Status
• /settings - Change Group Settings
• /set_template - Set IMDb Template
• /link - Create Link One Post
• /batch - Create Link Multiple Posts"""

    OWNERMODS_TXT = """<b><u>Owner Mods</u></b>

<b>Commands and Usage:</b>
• /users - List All Users
• /chats - List All Groups
• /ban - Ban User
• /unban - Unban User
• /leave - Leave Group
• /disable - Disable Group
• /enable - Re-enable Group
• /invite_link - Generate Group Link
• /users_broadcast - Broadcast Message All Users
• /groups_broadcast - Broadcast Message All Groups"""

    STATUS_TXT = """★ Total Files: <code>{}</code>
★ Total Users: <code>{}</code>
★ Total Groups: <code>{}</code>
★ Used Storage: <code>{}</code>
★ Free Storage: <code>{}</code>"""

    LOG_TEXT_G = """#NewGroup
Group - {}
ID - <code>{}</code>
Total Members - {}
Added by - {}"""

    LOG_TEXT_P = """#NewUser
Name - {}
ID - <code>{}</code>"""
