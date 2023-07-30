from telethon import events, Button, custom
from DazaiRobot.events import register

@register(pattern=("^/(game|games)"))
async def games(event):

    await event.reply(
                    "𝖧𝖾𝗒 𝖨'𝗏𝖾 𝗀𝗈𝗍 𝗌𝗈𝗆𝖾 𝗀𝖺𝗆𝖾𝗌 𝖿𝗈𝗋 𝗒𝗈𝗎! 𝗉𝗋𝖾𝗌𝗌 𝗍𝗁𝖾 𝖻𝗎𝗍𝗍𝗈𝗇 𝖻𝖾𝗅𝗈𝗐 𝗍𝗈 𝗉𝗅𝖺𝗒 𝗍𝗁𝖾 𝗀𝖺𝗆𝖾...",
                    buttons=[
                        [
                            Button.url(
                                "ʙᴜʙʙʟᴇ ᴛᴏᴡᴇʀ 3ᴅ",
                                "https://play.famobi.com/bubble-tower-3d",
                            ),
                            Button.url(
                                "ʀᴏᴍ ɴᴏᴍ ʀᴜɴ",
                                "https://play.famobi.com/om-nom-run",
                            ),
                        ],

                        [
                            Button.url(
                                "ᴄᴀɴᴏɴ ʙᴀʟʟs 3ᴅ",
                                "https://play.famobi.com/cannon-balls-3d",
                            ),
                            Button.url(
                                "ᴀʀᴄʜᴇʀʏ ᴡᴏᴏᴅ ᴛᴏᴜʀ",
                                "https://play.famobi.com/archery-world-tour",
                            ),
                        ]
                    ],
                    parse_mode="html",
                )

__mod_name__ = "𝙶ᴀᴍᴇs"

__help__ = """
> /games : 𝖲𝗁𝗈𝗐𝗌 𝖺𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝗀𝖺𝗆𝖾𝗌 𝗍𝗈 𝗉𝗅𝖺𝗒.
"""
