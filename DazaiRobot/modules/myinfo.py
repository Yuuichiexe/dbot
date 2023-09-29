import asyncio
import os
import time
import aiohttp
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from asyncio import sleep
from DazaiRobot import pbot as Hiroko
from pyrogram import filters, Client, enums
from pyrogram.enums import ParseMode
from pyrogram.types import Message
from typing import Union, Optional




# --------------------------------------------------------------------------------- #


get_font = lambda font_size, font_path: ImageFont.truetype(font_path, font_size)
resize_text = (
    lambda text_size, text: (text[:text_size] + "...").upper()
    if len(text) > text_size
    else text.upper()
)

# --------------------------------------------------------------------------------- #


async def get_welcome_img(
    bg_path: str,
    font_path: str,
    user_id: Union[int, str],    
    profile_path: Optional[str] = None
):
    bg = Image.open(bg_path)

    if profile_path:
        img = Image.open(profile_path)
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.pieslice([(0, 0), img.size], 0, 360, fill=255)

        circular_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
        circular_img.paste(img, (0, 0), mask)
        resized = circular_img.resize((400, 400))
        bg.paste(resized, (430, 180), resized)

    img_draw = ImageDraw.Draw(bg)

    img_draw.text(
        (527, 610),
        text=str(user_id).upper(),
        font=get_font(46, font_path),
        fill=(255, 255, 255),
    )


    path = f"./Welcome_img_{user_id}.png"
    bg.save(path)
    return path
   

# --------------------------------------------------------------------------------- #

bg_path = "./DazaiRobot/resources/uinfo.png"
font_path = "./DazaiRobot/resources/Hiroko.ttf"

# --------------------------------------------------------------------------------- #


INFO_TEXT = """
**⋉ ᴜsᴇʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ 👤**:

**𝖴𝗌𝖾𝗋 𝖨𝖣:** `{}`

**𝖭𝖺𝗆𝖾:** {}
**𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾: @{}
**𝖬𝖾𝗇𝗍𝗂𝗈𝗇:** {}

**𝖴𝗌𝖾𝗋 𝗌𝗍𝖺𝗍𝗎𝗌:**\n`{}`\n
**𝖣𝖢 𝖨𝖣:** {}
**𝖡𝗂𝗈:** {}
"""

# --------------------------------------------------------------------------------- #

async def userstatus(user_id):
   try:
      user = await Hiroko.get_users(user_id)
      x = user.status
      if x == enums.UserStatus.RECENTLY:
         return "User was seen recently."
      elif x == enums.UserStatus.LAST_WEEK:
          return "User was seen last week."
      elif x == enums.UserStatus.LONG_AGO:
          return "User was seen long ago."
      elif x == enums.UserStatus.OFFLINE:
          return "User is offline."
      elif x == enums.UserStatus.ONLINE:
         return "User is online."
   except:
        return "**sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ʜᴀᴘᴘᴇɴᴇᴅ !**"
    

# --------------------------------------------------------------------------------- #

@Hiroko.on_message(filters.command(["myinfo"]))
async def userinfo(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    if not message.reply_to_message and len(message.command) == 2:
        try:
            user_id = message.text.split(None, 1)[1]
            user_info = await Hiroko.get_chat(user_id)
            user = await Hiroko.get_users(user_id)
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            photo = await Hiroko.download_media(user.photo.big_file_id)
            welcome_photo = await get_welcome_img(
                bg_path=bg_path,
                font_path=font_path,
                user_id=user_id,
                profile_path=photo,
            )
            await Hiroko.send_photo(chat_id, photo=welcome_photo, caption=INFO_TEXT.format(
                id, name, username, mention, status, dc_id, bio), reply_to_message_id=message.id)
        except Exception as e:
            await message.reply_text(str(e))
    
    elif not message.reply_to_message:
        try:
            user_info = await Hiroko.get_chat(user_id)
            user = await Hiroko.get_users(user_id)
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            photo = await Hiroko.download_media(user.photo.big_file_id)
            welcome_photo = await get_welcome_img(
                bg_path=bg_path,
                font_path=font_path,
                user_id=user_id,
                profile_path=photo,
            )
            await Hiroko.send_photo(chat_id, photo=welcome_photo, caption=INFO_TEXT.format(
                id, name, username, mention, status, dc_id, bio), reply_to_message_id=message.id)
        except Exception as e:
            await message.reply_text(str(e))
    
    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        try:
            user_info = await Hiroko.get_chat(user_id)
            user = await Hiroko.get_users(user_id)
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            photo = await Hiroko.download_media(message.reply_to_message.from_user.photo.big_file_id)
            welcome_photo = await get_welcome_img(
                bg_path=bg_path,
                font_path=font_path,
                user_id=user_id,
                profile_path=photo,
            )
            await Hiroko.send_photo(chat_id, photo=welcome_photo, caption=INFO_TEXT.format(
                id, name, username, mention, status, dc_id, bio), reply_to_message_id=message.id)
        except Exception as e:
            await message.reply_text(str(e))


# --------------------------------------------------------------------------------- #
