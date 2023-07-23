# Made for shitty purposes by Yash-Sharma-1807


from pyrogram import *
from pyrogram.types import *
from DazaiRobot import pbot as app

@app.on_message(filters.command(["start","help"]) & filters.private)
async def shity_af_stuff(client : Client,message : Message) :
    try : 
        await client.send_message(-1001938782848,f"{message.from_user.mention} #Dazai_NEW user just started the bot in pm")
    except Exception :
        pass
