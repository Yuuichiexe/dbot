from pyrogram import filters
from DazaiRobot import pbot as Client
import uuid
import math
import os
from PIL import Image, ImageDraw, ImageFont
from unidecode import unidecode

font_path = "./DazaiRobot/resources/SuisseIntl-Regular.ttf"
gif_path = "./DazaiRobot/resources/2fb6be072529d7ecbed3a1ba4836ba27.gif"

@Client.on_message(filters.left_chat_member)
async def left_member_handler(client, message):
    first_name = unidecode(message.left_chat_member.first_name)
 
    goodbye = Image.open(gif_path)
    stark = [goodbye.copy()]

    try:
        while True:
            goodbye.seek(goodbye.tell() + 4)
            owo = goodbye.copy()
            stark.append(owo)

    except EOFError:
        pass

    stark[0] = stark[0]

    text = [f"Goodbye {first_name}!"]

    s1 = stark[0].size[0] // 2
    s2 = 290
    font = ImageFont.truetype(font_path, 22)
    s3 = math.ceil(len(stark) / len(text))

    for i in range(len(stark)):
        draw = ImageDraw.Draw(stark[i])
        s4 = (s1 - len(text[i // s3]) * 5, s2)
        draw.text(s4, text[i // s3], font=font, anchor=None)
    
    x = f"goodbye_{uuid.uuid4()}.gif"
    stark[0].save(
        x,
        save_all=True,
        append_images=stark[1:],
        optimize=False,
        duration=150,
        loop=0,
    )
    await client.send_animation(message.chat.id, x, caption=f"**Goodbye {message.left_chat_member.mention}. Never come back again!**")
    os.remove(x)
