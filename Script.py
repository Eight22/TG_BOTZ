class script(object):
    START_TXT = """Hello {},
My Name Is <a href=https://t.me/{}>{}</a>, Just Add Me To Your Group And Enjoy... """

    HELP_TXT = """Hey {}
Here Is The Help For My Commands."""

 
    ABOUT_TXT = """
👰 Name : <a href=https://t.me/DesiSearchBot>Shreya Tyagi</a>
 🦹 Creator : <a href='https://t.me/YourX'>YourX</a> 
 🤖 Version : 4.0</b>"""

    SOURCE_TXT = """
<b>Hᴇʏ, Tʜɪs ɪs ᴀ Oᴘᴇɴ Sᴏᴜʀᴄᴇ Pʀᴏᴊᴇᴄᴛ.

Tʜɪs Bᴏᴛ ʜᴀs Lᴀᴛᴇsᴛ ᴀɴᴅ Aᴅᴠᴀɴᴄᴇᴅ Fᴇᴀᴛᴜʀᴇs⚡️

Fork our repository and give star ⭐- <a href='https://github.com/Kushalhk/TG_BOTZ/tree/stream-feature'>📥 ᴄʟɪᴄᴋ ʜᴇʀᴇ 📥</a></b>
"""
    MANUELFILTER_TXT = """
Filter Is A Feature Were Users Can Set Automated Replies For A Particular Keyword And I Will Respond Whenever A Keyword Is Found In The Message.
<b>ɴᴏᴛᴇ:</b>
1. This Bot Should Have Privilege.
2. Only Admin Can Add Filters In A Chat.
3. Alert Buttons Have A Limit Of 64 Characters.
Commands And Use:
• /filter - <code>Add A Filter In A Chat
• /filters - <code>List All The Filters Of A Chat List
• /del - <code>Delete A Specific Filter In A Chat
• /delall - <code>Delete The Whole Filters In A Chat (Chat Owner Only)"""

    BUTTON_TXT = """

Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/YourX)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """

<b>Note:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db.

<b>Note: Auto Filter</b>
1. Add The Bot As Admin On Your Group.
2. Use /connect And Connect Your Group To The Bot.
3. Use /settings On Bot's Pm And Turn On Auto Filter On The Settings Menu."""

    CONNECTION_TXT = """

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """
<b>ɴᴏᴛᴇ:</b>
my features Stay here new features coming soon...  
 <b>✯ Maintained by : <a href=https://t.me/KUSHALHK>OWNER</a></b>
  
 <b>✯ Join here : <a href=https://t.me/TG_UPDATES1>Join my updateds</a></b> 
  
 ./id - <code>ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.</ 
 code> 
  
 ./info  - <code>ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.</code> 
  
 ./song - Download any song [<code>example /song vaa vaathi song</code>] 
  
 ./telegraph - <code>Telegraph generator sen under 5MB video or photo I give telegraph link</code> 
  
 ./tts - <code>This command usage text to voice converter</code> 
  
 ./video - This command usage any YouTube video download hd [<code>example /video https://youtu.be/Aiue8PMuD-k</code>]

./font - This command usage stylish and cool font generator [<code>example /font hi</code>]"""


    ADMIN_TXT = """ʜᴇʟᴘ: Aᴅᴍɪɴ Mᴏᴅs
<b>ɴᴏᴛᴇ:</b>
Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /logs - <code>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ. [Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</code>
• /delete - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ</code>
• /leave  - <code>ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /ban  - <code>ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban  - <code>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /channel - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ</code>
• /broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ</code>
• /grp_broadcast - <code>Tᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.</code>
• /gfilter - <code>ᴛᴏ ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /gfilters - <code>ᴛᴏ ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /delg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ</code>
• /request - <code>Tᴏ sᴇɴᴅ ᴀ Mᴏᴠɪᴇ/Sᴇʀɪᴇs ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ʙᴏᴛ ᴀᴅᴍɪɴs. Oɴʟʏ ᴡᴏʀᴋs ᴏɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ. [Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</code>
• /delallg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ Gғɪʟᴛᴇʀs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /deletefiles - <code>Tᴏ ᴅᴇʟᴇᴛᴇ CᴀᴍRɪᴘ ᴀɴᴅ PʀᴇDVD Fɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>"""

    STATUS_TXT = """🗃️ Total Files: <code>{}</code>
👪 Total Users: <code>{}</code>
💬 Total Chats: <code>{}</code>
📂 Used Storage: <code>{}</code> 
🗂 Free Storage: <code>{}</code> """
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """🚩 #NewUser
🆔 ID - <code>{}</code>
🤹🏻 Name - {}
"""

    ALRT_TXT = """ʜᴇʟʟᴏ {},
ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇQᴜᴇꜱᴛ,
ʀᴇQᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ..."""

    OLD_ALRT_TXT = """ʜᴇʏ {},
ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏʟᴅ ᴍᴇꜱꜱᴀɢᴇꜱ, 
ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇQᴜᴇꜱᴛ ᴀɢᴀɪɴ."""

    CUDNT_FND = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}
ᴅɪᴅ ʏᴏᴜ ᴍᴇᴀɴ ᴀɴʏ ᴏɴᴇ ᴏꜰ ᴛʜᴇꜱᴇ?"""

    I_CUDNT = """<b>sᴏʀʀʏ ɴᴏ ꜰɪʟᴇs ᴡᴇʀᴇ ꜰᴏᴜɴᴅ ꜰᴏʀ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ {} 😕

ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴘᴇʟʟɪɴɢ ɪɴ ɢᴏᴏɢʟᴇ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ 😃

ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 👇

ᴇxᴀᴍᴘʟᴇ : Uncharted or Uncharted 2022 or Uncharted En

ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 👇

ᴇxᴀᴍᴘʟᴇ : Loki S01 or Loki S01E04 or Lucifer S03E24

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)</b>"""

    I_CUD_NT = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}.
ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ꜱᴘᴇʟʟɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ ᴏʀ ɪᴍᴅʙ..."""

    MVE_NT_FND = """ᴍᴏᴠɪᴇ ɴᴏᴛ ꜰᴏᴜɴᴅ ɪɴ ᴅᴀᴛᴀʙᴀꜱᴇ..."""

    TOP_ALRT_MSG = """Cʜᴇᴄᴋɪɴɢ Fᴏʀ Mᴏᴠɪᴇ Iɴ Dᴀᴛᴀʙᴀsᴇ..."""

    MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️</b>"""

    SHORTLINK_INFO = """
<b>──────「<a href=https://t.me/TG_UPADTES1/346> Hᴏᴡ ᴛᴏ Eᴀʀɴ Mᴏɴᴇʏ </a> 」──────

Yᴏᴜ ᴄᴀɴ Eᴀʀɴ Mᴏɴᴇʏ Fʀᴏᴍ Tʜɪs Bᴏᴛ Uɴᴛɪʟ ᴛʜɪs ʙᴏᴛ ɪs ᴀʟɪᴠᴇ.

Wᴀɴᴛ ᴛᴏ Kɴᴏᴡ Hᴏᴡ? Fᴏʟʟᴏᴡ Tʜᴇsᴇ Sᴛᴇᴘs:-

sᴛᴇᴘ 𝟷 : ʏᴏᴜ ᴍᴜsᴛ ʜᴀᴠᴇ ᴀᴛʟᴇᴀsᴛ ᴏɴᴇ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴍɪɴɪᴍᴜᴍ 1𝟶𝟶 ᴍᴇᴍʙᴇʀs.

sᴛᴇᴘ 𝟸 : ᴍᴀᴋᴇ ᴀᴄᴄᴏᴜɴᴛ ᴏɴ Aɴʏ <a href=https://moneykamalo.com/ref/Harikushal>Sʜᴏʀᴛᴇɴᴇʀ Wᴇʙsɪᴛᴇ</a>.

sᴛᴇᴘ 𝟹 : ꜰᴏʟʟᴏᴡ ᴛʜᴇsᴇ <a href=https://t.me/TG_UPDATES1/346> ɪɴꜱᴛʀᴜᴄᴛɪᴏɴꜱ </a>Tᴏ ᴄᴏɴɴᴇᴄᴛ sʜᴏʀᴛᴇɴᴇʀ.

➣ Yᴏᴜ ᴄᴀɴ ᴄᴏɴɴᴇᴄᴛ ᴀs ᴍᴀɴʏ ɢʀᴏᴜᴘ ʏᴏᴜ ʜᴀᴠᴇ.

Any Doubts or Not Connecting? Contact Me </b>
"""

    REQINFO = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠

ᴀꜰᴛᴇʀ 5 ᴍɪɴᴜᴛᴇꜱ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇʟᴇᴛᴇᴅ

ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ꜱᴇᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴍᴏᴠɪᴇ / sᴇʀɪᴇs ꜰɪʟᴇ, ʟᴏᴏᴋ ᴀᴛ ᴛʜᴇ ɴᴇxᴛ ᴘᴀɢᴇ"""

    SELECT = """
MOVIES ➢ Sᴇʟᴇᴄᴛ "Lᴀɴɢᴜᴀɢᴇs"

SERIES ➢ Sᴇʟᴇᴄᴛ "Sᴇᴀsᴏɴs"

Tɪᴘ: Sᴇʟᴇᴄᴛ "Lᴀɴɢᴜᴀɢᴇs" ᴏʀ "Sᴇᴀsᴏɴs" Bᴜᴛᴛᴏɴ ᴀɴᴅ Cʟɪᴄᴋ "Sᴇɴᴅ Aʟʟ" Tᴏ ɢᴇᴛ Aʟʟ Fɪʟᴇ Lɪɴᴋs ɪɴ ᴀ Sɪɴɢʟᴇ ᴄʟɪᴄᴋ"""

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : MirzaPur S01E01

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)"""

    NORSLTS = """
★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★

𝗜𝗗 <b>: {}</b>

𝗡𝗮𝗺𝗲 <b>: {}</b>

𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""

    CAPTION = """<b>📂 : {file_name}
<b> Size ⚙️: {file_size}</b>"""
    IMDB_TEMPLATE_TXT = """
<b>Query: {qurey}

IMDB_TEMPLATE = """✅ I Found: <code>{query}</code>

🏷 Title:: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟Rating: <a href={url}/ratings>{rating} / 10</a>
☀️ Languages : <code>{languages}</code>
📀 RunTime: {runtime} Minutes
📆 Release Info : {release_date}
🎛 Countries : <code>{countries}</code>
⏰ Result Shown in: {remaining_seconds} 

🗣 Requested by: {message.from_user.mention}
©️ Powered by: <b>{message.chat.title}</b>"""
    
    ALL_FILTERS = """
<b>Hᴇʏ {}, Tʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs.</b>"""
    
    GFILTER_TXT = """
<b>Welcome To Global Filters Are The Filters Set By Bot Admins Which Will Work On All Groups.</b>
    
Available Commands:
• /gfilter - <code>To Create A Global Filter.
• /gfilters - <code>To View All Global Filters.
• /delg - <code>To Delete A Particular Global Filter.
• /delallg - <code>To Delete All Global Filters."""
    
    FILE_STORE_TXT = """
<b>Fɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</b>

Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /batch - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</code>
• /link - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.</code>
• /pbatch - <code>Jᴜsᴛ ʟɪᴋᴇ /batch, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.</code>
• /plink - <code>Jᴜsᴛ ʟɪᴋᴇ /link, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.</code>"""

    SONG_TXT = """<b>ꜱᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴏᴅᴜʟᴇ</b> 
      
 <b>ꜱᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴏᴅᴜʟᴇ, ꜰᴏʀ ᴛʜᴏꜱᴇ ᴡʜᴏ ʟᴏᴠᴇ ᴍᴜꜱɪᴄ. yᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ꜰᴇᴀᴛᴜᴇ ꜰᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴy ꜱᴏɴɢ ᴡɪᴛʜ ꜱᴜᴩᴇʀ ꜰᴀꜱᴛ ꜱᴩᴇᴇᴅ. ᴡᴏʀᴋꜱ ʙᴏᴛ ᴀɴᴅ ɢʀᴏᴜᴩꜱ ᴏɴʟy...</b> 
  
 <b>ᴄᴏᴍᴍᴀɴᴅꜱ</b> :<b> 𝄟⃝.  /song ꜱᴏɴɢ ɴᴀᴍᴇ</b></b>""" 
  
    YTDL_TXT = """<b>ʜᴇʟᴩ yᴏᴜ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ꜰʀᴏᴍ yᴏᴜᴛᴜʙᴇ. 
  
 ᴜꜱᴀɢᴇ : yᴏᴜ ᴄᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴy ᴠɪᴅᴇᴏ ꜰʀᴏᴍ yᴏᴜᴛᴜʙᴇ 
  
 ʜᴏᴡ ᴛᴏ ᴜꜱᴇ : ᴛyᴩᴇ - /video ᴏʀ /mp4 
  
 ᴇxᴀᴍᴩʟᴇ :<code>/mp4 https://youtu.be/example...</code></b>""" 
  
    TTS_TXT = """<b>ᴛᴛꜱ 🎤 ᴍᴏᴅᴜʟᴇ : ᴛʀᴀɴꜱʟᴀᴛᴇ ᴛᴇxᴛ ᴛᴏ ꜱᴩᴇᴇᴄʜ 
  
 ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ : /tts ᴄᴏɴᴠᴇʀᴛ ᴛᴇꜱᴛ ᴛᴏ ꜱᴩᴇᴇᴄʜ</b>""" 
  
    GTRANS_TXT = """<b>ʜᴇʟᴩ:ɢᴏᴏɢʟᴇ ᴛʀᴀɴꜱʟᴀᴛᴇʀ 
  
 ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ʜᴇʟᴩꜱ yᴏᴜ ᴛᴏ ᴛʀᴀɴꜱʟᴀᴛᴇ ᴀ ᴛᴇxᴛ ᴛᴏ ᴀɴy ʟᴀɴɢᴜᴀɢᴇꜱ yᴏᴜ ᴡᴀɴᴛ. ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋꜱ ᴏɴ ʙᴏᴛʜ ᴩᴍ ᴀɴᴅ ɢʀᴏᴜᴏ  
  
 ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ : /tr - ᴛᴏ ᴛʀᴀɴꜱʟᴀᴛᴇʀ ᴛᴇxᴛꜱ ᴛᴏ ᴀ ꜱᴩᴇᴄɪꜰᴄ ʟᴀɴɢᴜᴀɢᴇ 
  
 ɴᴏᴛᴇ: ᴡʜɪʟᴇ ᴜꜱɪɴɢ /tr yᴏᴜ ꜱʜᴏᴜʟᴅ ꜱᴩᴇᴄɪꜰy ᴛʜᴇ ʟᴀɴɢᴜᴀɢᴇ ᴄᴏᴅᴇ 
  
 ᴇxᴀᴍᴩʟᴇ: /𝗍𝗋 ᴍʟ 
 • ᴇɴ = ᴇɴɢʟɪꜱʜ 
 • ᴍʟ = ᴍᴀʟᴀyᴀʟᴀᴍ 
 • ʜɪ = ʜɪɴᴅɪ</b>""" 
  
    TELE_TXT = """<b>ʜᴇʟᴘ: ᴛᴇʟᴇɢʀᴀᴘʜ ᴅᴏ ᴀꜱ ʏᴏᴜ ᴡɪꜱʜ ᴡɪᴛʜ ᴛᴇʟᴇɢʀᴀ.ᴘʜ ᴍᴏᴅᴜʟᴇ! 
  
 ᴜꜱᴀɢᴇ: /telegraph - ꜱᴇɴᴅ ᴍᴇ ᴘɪᴄᴛᴜʀᴇ ᴏʀ ᴠɪᴅᴇ ᴜɴᴅᴇʀ (5ᴍʙ) 
  
 ɴᴏᴛᴇ: 
 ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪꜱ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ɢᴏᴜᴘꜱ ᴀɴᴅ ᴘᴍꜱ 
 ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ʙᴇ ᴜꜱᴇᴅ ʙʏ ᴇᴠᴇʀʏᴏɴᴇ</b>""" 
  
    CORONA_TXT = """<b>ʜᴇʟᴩ: ᴄᴏᴠɪᴅ 
  
 ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ʜᴇʟᴩꜱ yᴏᴜ ᴛᴏ ᴋɴᴏᴡ ᴅᴀɪʟy ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴄᴏᴠɪᴅ 
  
 ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ: 
  
 /covid - ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ yᴏᴜʀ ᴄᴏᴜɴᴛʀy ɴᴀᴍᴇ ᴛᴏ ɢᴇᴛ ᴄᴏᴠɪᴅᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ 
 ᴇxᴀᴍᴩʟᴇ:<code>/covid 𝖨𝗇𝖽𝗂𝖺</code> 
  
 ⚠️ ᴛʜɪꜱ ꜱᴇʀᴠɪᴄᴇ ʜᴀꜱ ʙᴇᴇɴ ꜱᴛᴏᴩᴩᴇᴅ 
  
 </b>""" 
  
    ABOOK_TXT = """<b>ʜᴇʟᴩ : ᴀᴜᴅɪᴏʙᴏᴏᴋ 
  
 yᴏᴜ ᴄᴀɴ ᴄᴏɴᴠᴇʀᴛ ᴀ ᴩᴅꜰ ꜰɪʟᴇ ᴛᴏ ᴀ ᴀᴜᴅɪᴏ ꜰɪʟᴇ ᴡɪᴛʜ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ✯ 
  
 ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ: 
 /audiobook: ʀᴇᴩʟy ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴀɴy ᴩᴅꜰ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴛʜᴇ ᴀᴜᴅɪᴏ 
</b>""" 
  
 
    PINGS_TXT = """<b>ᴘɪɴɢ ᴛᴇꜱᴛɪɴɢ:ʜᴇʟᴘꜱ ʏᴏᴜ ᴛᴏ ᴋɴᴏᴡ ʏᴏᴜʀ ᴘɪɴɢ🪄 
  
 ᴄᴏᴍᴍᴀɴᴅꜱ: 
 • /alive - ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜ ᴀʀᴇ ᴀʟɪᴠᴇ. 
 • /help - To get help. 
 • /ping - <b>ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴘɪɴɢ. 
  
 ᴜꜱᴀɢᴇ : 
 • ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅꜱ ᴄᴀɴ ʙᴇ ᴜꜱᴇᴅ ɪɴ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘꜱ 
 • ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅꜱ ᴄᴀɴ ʙᴇ ᴜꜱᴇᴅ ʙᴜʏ ᴇᴠᴇʀʏᴏɴᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘꜱ ᴀɴᴅ ʙᴏᴛꜱ ᴘᴍ 
 • ꜱʜᴀʀᴇ ᴜꜱ ꜰᴏʀ ᴍᴏʀᴇ ꜰᴇᴀᴛᴜʀᴇꜱ 
  </b>""" 
  
    STICKER_TXT = """<b>yᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴍᴏᴅᴜʟᴇ ᴛᴏ ꜰɪɴᴅᴀɴy  ꜱᴛɪᴄᴋᴇʀꜱ ɪᴅ. 
 • ᴜꜱᴀɢᴇ :ᴛᴏ ɢᴇᴛ ꜱᴛɪᴄᴋᴇʀ 
   
 ⭕ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ 
 ◉ Reply To Any Sticker [/stickerid]  
 </b>""" 
  
    FONT_TXT= """<b>ᴜꜱᴀɢᴇ 
  
 yᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴍᴏᴅᴜʟᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ꜰᴏɴᴛ ꜱᴛyʟᴇ   
  
 ᴄᴏᴍᴍᴀɴᴅ : /font yᴏᴜʀ ᴛᴇxᴛ (ᴏᴩᴛɪᴏɴᴀʟ) 
 ᴇɢ:- /font ʜᴇʟʟᴏ 
  
 </b>""" 
  
    PURGE_TXT = """<b>ᴘᴜʀɢᴇ 
      
 ᴅᴇʟᴇᴛᴇ ᴀ ʟᴏᴛ ᴏꜰ ᴍᴇssᴀɢᴇs ꜰʀᴏᴍ ɢʀᴏᴜᴘs!  
      
  ᴀᴅᴍɪɴ  
  
 ◉ /purge :- ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴇssᴀɢᴇs ꜰʀᴏᴍ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴍᴇssᴀɢᴇ, ᴛᴏ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴍᴇssᴀɢᴇ</b>""" 
  
    WHOIS_TXT = """<b>ᴡʜᴏɪꜱ ᴍᴏᴅᴜʟᴇ 
  
 ɴᴏᴛᴇ:- ɢɪᴠᴇ ᴀ ᴜꜱᴇʀ ᴅᴇᴛᴀɪʟꜱ 
 /whois :- ɢɪᴠᴇ ᴀ ᴜꜱᴇʀ ꜰᴜʟʟ ᴅᴇᴛᴀɪʟꜱ 📑 
 </b>""" 
  
    JSON_TXT = """<b> 
 ᴊsᴏɴ:  
 ʙᴏᴛ ʀᴇᴛᴜʀɴs ᴊsᴏɴ ꜰᴏʀ ᴀʟʟ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇs ᴡɪᴛʜ /json 
  
 ꜰᴇᴀᴛᴜʀᴇs: 
  
 ᴍᴇssᴀɢᴇ ᴇᴅɪᴛᴛɪɴɢ ᴊsᴏɴ 
 ᴘᴍ sᴜᴘᴘᴏʀᴛ 
 ɢʀᴏᴜᴘ sᴜᴘᴘᴏʀᴛ 
  
 ɴᴏᴛᴇ: 
  
 ᴇᴠᴇʀʏᴏɴᴇ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ , ɪꜰ sᴘᴀᴍɪɴɢ ʜᴀᴘᴘᴇɴs ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʙᴀɴ ʏᴏᴜ ꜰʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ.</b>""" 
  
    URLSHORT_TXT = """<b>ʜᴇʟᴩ: ᴜʀʟ ꜱʜᴏʀᴛɴᴇʀ 
  
 <i><b>𝚃𝚑𝚒𝚜ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ʜᴇʟᴩꜱ yᴏᴜ ᴛᴏ ꜱʜᴏʀᴛ ᴛᴏ ᴜʀʟ </i></b> 
  
 ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ: 
  
 /short: <b>ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ yᴏᴜʀ ʟɪɴᴋ ᴛᴏ ɢᴇᴛ ꜱʜᴏʀᴛ ʟɪɴᴋꜱ</b> 
 ᴇxᴀᴍᴩʟᴇ:<code>/short https://youtu.be/example...</code> 
</b>""" 
  
    CARB_TXT = """<b>ʜᴇʟᴩ ꜰᴏʀ ᴄᴀʀʙᴏɴ 
  
 ᴄᴀʀʙᴏɴ ɪꜱ ᴀ ꜰᴇᴜᴛᴜʀᴇ ᴛᴏ ᴍᴀᴋᴇ ᴛʜᴇ ɪᴍᴀɢᴇ ᴀꜱ ꜱʜᴏᴡɴ ɪɴ ᴛʜᴇ ᴛᴏᴩ ᴡɪᴛʜ ʏᴏᴜʀ ᴛᴇxᴛꜱ. 
 ꜰᴏʀ ᴜꜱɪɴɢ ᴛʜᴇ ᴍᴏᴅᴜʟᴇ ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴛʜᴇ ᴛᴇxᴛ ᴀɴᴅ ᴏᴇᴩʟᴀʏ ᴛɪ ɪᴛ ᴡɪᴛʜ  /carbon ᴄᴏᴍᴍᴀɴᴅ ᴛʜᴇ ʙᴏᴛ ᴡɪʟʟ ᴩᴇᴩᴀʏ ᴡɪᴛʜ ᴛʜᴇ ᴄᴀʀʙᴏɴ ɪᴍᴀɢᴇ 
</b>""" 
    GEN_PASS = """<b>Hᴇʟᴘ: Pᴀꜱꜱᴡᴏʀᴅ Gᴇɴᴇʀᴀᴛᴏʀ 
  
 Tʜᴇʀᴇ Iꜱ Nᴏᴛʜɪɴɢ Tᴏ Kɴᴏᴡ Mᴏʀᴇ. Sᴇɴᴅ Mᴇ Tʜᴇ Lɪᴍɪᴛ Oғ Yᴏᴜʀ Pᴀꜱꜱᴡᴏʀᴅ. 
 - I Wɪʟʟ Gɪᴠᴇ Tʜᴇ Pᴀꜱꜱᴡᴏʀᴅ Oғ Tʜᴀᴛ Lɪᴍɪᴛ. 
  
 Cᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ Uꜱᴀɢᴇ: 
 • /genpassword ᴏʀ /genpw 𝟸𝟶 
  
 NOTE: 
 • Oɴʟʏ Dɪɢɪᴛꜱ Aʀᴇ Aʟʟᴏᴡᴇᴅ 
 • Mᴀxɪᴍᴜᴍ Aʟʟᴏᴡᴇᴅ Dɪɢɪᴛꜱ Tɪʟʟ 𝟾𝟺  
 (I Cᴀɴ'ᴛ Gᴇɴᴇʀᴀᴛᴇ Pᴀꜱꜱᴡᴏʀᴅꜱ Aʙᴏᴠᴇ Tʜᴇ Lᴇɴɢᴛʜ 𝟾𝟺) 
 • IMDʙ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ. 
 • Tʜᴇꜱᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ᴡᴏʀᴋꜱ ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ. 
 • Tʜᴇꜱᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ᴄᴀɴ ʙᴇ ᴜꜱᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ.</b>""" 
  
    SHARE_TXT = """<b>/share ﹛ ʏᴏᴜʀ ᴛᴇxᴛ ﹜ 
  
 - ᴇx :- /share hi da 
  
 </b>""" 
  
    PIN_TXT = """<b>ᴩɪɴ ᴍᴏᴅᴜʟᴇ 
 ᴩɪɴ ᴀ ᴍᴇꜱꜱᴀɢᴇ... 
  
 ᴀʟʟ ᴛʜᴇ ᴩɪɴ ʀᴇᴩʟᴀᴛᴇᴅ ᴄᴏᴍᴍᴀɴᴅꜱ ᴄᴀɴ ʙᴇ ꜰᴏᴜɴᴅ ʜᴇʀᴇ: 
  
 📌ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ📌 
  
 /pin :- ᴛᴏ ᴩɪɴ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ ᴏɴ ʏᴏᴜʀ ᴄʜᴀᴛꜱ 
 /unpin :- ᴛᴏ ᴜɴᴩɪɴ ᴛʜᴇ ᴄᴜʀʀᴇᴇɴᴛ ᴩɪɴɴᴇᴅ ᴍᴇꜱꜱᴀɢᴇ</b>"""

 
    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code></b>"""
    
    DELF_TXT = """
ᴛʜɪꜱ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.

ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴀʀᴇ ꜰʀᴇᴇʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴏʀ ᴘᴏꜱᴛᴇᴅ ʙʏ ꜱᴏᴍᴇʙᴏᴅʏ ᴇʟꜱᴇ. ᴊᴜꜱᴛ ꜰᴏʀ ᴇᴀꜱʏ ꜱᴇᴀʀᴄʜɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɪɴᴅᴇxɪɴɢ ꜰɪʟᴇꜱ ᴡʜɪᴄʜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ. ᴡᴇ ʀᴇꜱᴘᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀᴡꜱ ᴀɴᴅ ᴡᴏʀᴋꜱ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴅᴍᴄᴀ ᴀɴᴅ ᴇᴜᴄᴅ. ɪꜰ ᴀɴʏᴛʜɪɴɢ ɪꜱ ᴀɢᴀɪɴꜱᴛ ʟᴀᴡ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ꜱᴏ ᴛʜᴀᴛ ɪᴛ ᴄᴀɴ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀꜱᴀᴘ. ɪᴛ ɪꜱ ꜰᴏʀʙɪʙʙᴇɴ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ꜱᴛʀᴇᴀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ꜱʜᴀʀᴇ ᴏʀ ᴄᴏɴꜱᴜᴍᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ʟᴇɢᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ʜᴏʟᴅᴇʀ. ɪꜰ ʏᴏᴜ ʙᴇʟɪᴇᴠᴇ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴠɪᴏʟᴀᴛɪɴɢ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ʀᴇꜱᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰᴏʀ ʀᴇᴍᴏᴠᴀʟ. ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇꜱ ɴᴏᴛ ᴏᴡɴ ᴀɴʏ ᴏꜰ ᴛʜᴇꜱᴇ ᴄᴏɴᴛᴇɴᴛꜱ, ɪᴛ ᴏɴʟʏ ɪɴᴅᴇx ᴛʜᴇ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ. .."""

    RENDERING_TXT = """
⚡️ʟɪᴠᴇ sʏsᴛᴇᴍ sᴛᴀᴛᴜs ⚡️

❂ ʀᴀᴍ ●●●●●●●◌◌◌
✇ ᴄᴘᴜ ●●●●●●●◌◌◌
✪ ᴅᴀᴛᴀ ᴛʀᴀꜰɪᴄs ●●●●◌◌◌◌◌◌ 🛰

ᴠ2.8.1 [sᴛᴀʙʟᴇ] """

    LOGO = """
 ____  ___    ____   __  ____  ____ 
(_  _)/ __)  (  _ \ /  \(_  _)(__  )
  )( ( (_ \   ) _ ((  O ) )(   / _/ 
 (__) \___/  (____/ \__/ (__) (____)"""

# dont remove my logo 

  
