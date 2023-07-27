import secureme

from DazaiRobot.events import register


@register(pattern="^/encrypt ?(.*)")
async def hmm(event):
    if event.reply_to_msg_id:
        lel = await event.get_reply_message()
        cmd = lel.text
    else:
        cmd = event.pattern_match.group(1)
    Text = cmd
    k = secureme.encrypt(Text)
    await event.reply(k)


@register(pattern="^/decrypt ?(.*)")
async def hmm(event):
    if event.reply_to_msg_id:
        lel = await event.get_reply_message()
        ok = lel.text
    else:
        ok = event.pattern_match.group(1)
    Text = ok
    k = secureme.decrypt(Text)
    await event.reply(k)


__mod_name__ = "𝖳𝗈𝗈𝗅𝗌"

__help__ = """

*ᴄᴏɴᴠᴇʀᴛs*
 ➛ /encrypt*:* ᴇɴᴄʀʏᴘᴛs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ
 ➛ /decrypt*:* ᴅᴇᴄʀʏᴘᴛs ᴘʀᴇᴠɪᴏᴜsʟʏ ᴇᴄʀʏᴘᴛᴇᴅ ᴛᴇxᴛ
"""
