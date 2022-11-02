import datetime
import random
import time

from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from TelethonHell.DB.gvar_sql import gvarstat

from . import *

# -------------------------------------------------------------------------------

ALIVE_TEMP = """
<b><i>🔥🔥𝒜𝓈𝓈𝒾𝓈𝓉𝒶𝓃𝓉 ɨs օռʟɨռɛ🔥🔥</b></i>
<i><b>↼ Øwñêr ⇀</i></b> : 『 <a href='tg://user?id={}'>{}</a> 』
╭──────────────
┣─ <b>» Telethon ~</b> <i>{}</i>
┣─ <b>» 𝒜𝓈𝓈𝒾𝓈𝓉𝒶𝓃𝓉 ~</b> <i>{}</i>
┣─ <b>» Sudo ~</b> <i>{}</i>
┣─ <b>» Uptime ~</b> <i>{}</i>
┣─ <b>» Ping ~</b> <i>{}</i>
╰──────────────
<b><i>»»» <a href='https://t.me/groupscout_bot'>[ †hê 𝒜𝓈𝓈𝒾𝓈𝓉𝒶𝓃𝓉 ]</a> «««</i></b>
"""

msg = """{}\n
<b><i>🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅</b></i>
<b>Telethon ≈</b>  <i>{}</i>
<b>𝒜𝓈𝓈𝒾𝓈𝓉𝒶𝓃𝓉 ≈</b>  <i>{}</i>
<b>Uptime ≈</b>  <i>{}</i>
<b>Abuse ≈</b>  <i>{}</i>
<b>Sudo ≈</b>  <i>{}</i>
"""
# -------------------------------------------------------------------------------


@hell_cmd(pattern="alive$")
async def up(event):
    ForGo10God, HELL_USER, hell_mention = await client_id(event)
    start = datetime.datetime.now()
    reply = await event.get_reply_message()
    hell = await eor(event, "`Building Alive....`")
    uptime = await get_time((time.time() - StartTime))
    alive_name = gvarstat("ALIVE_NAME") or HELL_USER
    a = gvarstat("ALIVE_PIC")
    pic_list = []
    if a:
        b = a.split(" ")
        if len(b) >= 1:
            for c in b:
                pic_list.append(c)
        PIC = random.choice(pic_list)
    else:
        PIC = "https://telegra.ph/file/6aa4511d1d19f22eff650.jpg"
    end = datetime.datetime.now()
    ling = (end - start).microseconds / 1000
    omk = ALIVE_TEMP.format(ForGo10God, alive_name, tel_ver, hell_ver, is_sudo, uptime, ling)
    await event.client.send_file(
        event.chat_id,
        file=PIC,
        caption=omk,
        parse_mode="HTML",
        reply_to=reply,
    )
    await hell.delete()


@hell_cmd(pattern="assist$")
async def hell_a(event):
    ForGo10God, HELL_USER, hell_mention = await client_id(event)
    uptime = await get_time((time.time() - StartTime))
    am = gvarstat("ALIVE_MSG") or "<b>»» 𝒜𝓈𝓈𝒾𝓈𝓉𝒶𝓃𝓉 ιѕ σиℓιиє ««</b>"
    try:
        hell = await event.client.inline_query(Config.BOT_USERNAME, "alive")
        await hell[0].click(event.chat_id)
        if event.sender_id == ForGo10God:
            await event.delete()
    except (noin, dedbot):
        await eor(
            event,
            msg.format(am, tel_ver, hell_ver, uptime, abuse_m, is_sudo),
            parse_mode="HTML",
        )


CmdHelp("alive").add_command(
    "alive", None, "Shows the Default Alive Message"
).add_command(
    "assist", None, "Shows Inline Alive Menu with more details."
).add_warning(
    "✅ Harmless Module"
).add()
