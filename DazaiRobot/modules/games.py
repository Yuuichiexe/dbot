from telethon import events, Button, custom
from DazaiRobot.events import register

@register(pattern=("^/(game|games)"))
async def games(event):

    await event.reply(
                    "𝗁𝖾𝗅𝗅𝗈, 𝗐𝖾 𝗁𝖺𝗏𝖾 𝖺𝗍𝗍𝖼𝗁𝖾𝖽 𝗌𝗈𝗆𝖾 𝗀𝖺𝗆𝖾𝗌 𝖿𝗈𝗋 𝗒𝗈𝗎, 𝗉𝗋𝖾𝗌𝗌 𝗍𝗁𝖾 𝖻𝗎𝗍𝗍𝗈𝗇 𝖺𝗇𝖽 𝗉𝗅𝖺𝗒 𝗀𝖺𝗆𝖾𝗌",
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
> /games : Some games for ur boredom
"""
