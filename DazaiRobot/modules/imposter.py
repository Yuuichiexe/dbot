from pyrogram import filters
from datetime import datetime
import pytz
from pytz import timezone
from html import escape
from DazaiRobot.modules.mongo.sangmata_db import *
from DazaiRobot import pbot as app
from DazaiRobot.Pyro.permissions import adminsOnly
from DazaiRobot.Pyro.message_utils import kirimPesan
from DazaiRobot.utils.mongo import db as dbname

# Set the log channel ID where name change logs will be sent
LOG_CHANNEL_ID = -1001527287273  # Replace with the actual log channel ID

@app.on_message(filters.group & ~filters.bot & ~filters.via_bot, group=3)
async def cek_mataa(_, m):
    if not await is_sangmata_on(m.chat.id):
        return
    if not await cek_userdata(m.from_user.id):
        await add_userdata(m.from_user.id, m.from_user.username, m.from_user.first_name, m.from_user.last_name)
    else:
        username, first_name, last_name = await get_userdata(m.from_user.id)
        msg = ""
        old_user = await app.get_chat_member(m.chat.id, m.from_user.id)
        if username != m.from_user.username or first_name != m.from_user.first_name or last_name != m.from_user.last_name:
            if username != m.from_user.username:
                log_message = f"🚨 <b>Imposter Username Change Detected</b>\n\n"
                log_message += f"Chat: {m.chat.title}\n"
                if m.chat.username:
                    log_message += f"<b>Chat Username:</b> @{m.chat.username}\n"
                log_message += f"<b>User:</b> {m.from_user.mention}\n"
                log_message += f"<b>User ID:</b> <code>{m.from_user.id}</code>\n"
                log_message += f"<b>Previous Username:</b> @{username}\n"
                log_message += f"<b>New Username:</b> @{m.from_user.username}"
                await app.send_message(LOG_CHANNEL_ID, log_message)
            if first_name != m.from_user.first_name or last_name != m.from_user.last_name:
                log_message = f"🚨 <b>Imposter Name Change Detected</b>\n\n"
                log_message += f"Chat: {m.chat.title}\n"
                if m.chat.username:
                    log_message += f"<b>Chat Username:</b> @{m.chat.username}\n"
                log_message += f"<b>User:</b> {m.from_user.mention}\n"
                log_message += f"<b>User ID:</b> <code>{m.from_user.id}</code>\n"
                log_message += f"<b>Previous Name:</b> {first_name} {last_name}\n"
                log_message += f"<b>New Name:</b> {m.from_user.first_name} {m.from_user.last_name}"
                await app.send_message(LOG_CHANNEL_ID, log_message)

            msg += "👀 <b>Imposter Detected</b>\n\n"

        if username != m.from_user.username:
            msg += f"❇️ {m.from_user.mention} [<code>{m.from_user.id}</code>] changed username from @{username} to @{m.from_user.username}.\n"
            await add_userdata(m.from_user.id, m.from_user.username, m.from_user.first_name, m.from_user.last_name)
        if first_name != m.from_user.first_name or last_name != m.from_user.last_name:
            name_change = False
            if first_name != m.from_user.first_name:
                msg += f"❇️ {m.from_user.mention} [<code>{m.from_user.id}</code>] changed first Name from {first_name} to {m.from_user.first_name}.\n"
                name_change = True
            if last_name != m.from_user.last_name:
                msg += f"❇️ {m.from_user.mention} [<code>{m.from_user.id}</code>] changed last name from {last_name} to {m.from_user.last_name}.\n"
                name_change = True
            if name_change:
                await add_userdata(m.from_user.id, m.from_user.username, m.from_user.first_name, m.from_user.last_name)
        if msg != "":
            await kirimPesan(m, msg, quote=True)

@app.on_message(filters.group & filters.command("history") & ~filters.bot & ~filters.via_bot)
async def search_history(_, m):
    if len(m.command) == 1:
        # Check if the command was replied to a message
        if m.reply_to_message and m.reply_to_message.from_user:
            user_id = m.reply_to_message.from_user.id
            username = m.reply_to_message.from_user.username
        else:
            return await kirimPesan(m, f"Please provide a user ID, username, or reply to a message to search the history.")
    else:
        query = m.command[1].strip()
        user_id = None
        if query.startswith("@"):
            username = query[1:]
            try:
                user = await app.get_users(username)
                user_id = user.id
            except:
                await kirimPesan(m, f"User with username '{username}' not found.")
        else:
            try:
                user_id = int(query)
            except ValueError:
                await kirimPesan(m, f"Invalid user ID or username. Please provide a valid user ID or username to search the history.")

    if user_id is not None:
        if await cek_userdata(user_id):
            username, first_name, last_name = await get_userdata(user_id)
            history_msg = "<b>🔰 Name History:</b>\n\n"
            history_msg += f"<code>👤 {user_id}</code>\n\n"

            name_history = await history_db.find({"user_id": user_id}).sort("_id", -1).to_list(None)

            for i, history in enumerate(name_history, start=1):
                timestamp = history["_id"].generation_time.astimezone(pytz.timezone("Asia/Kolkata"))
                formatted_timestamp = timestamp.strftime("[<code>%d/%m/%Y %I:%M:%S %p</code>]")
                change_first_name = escape(history["first_name"])
                change_last_name = escape(history["last_name"]) if history["last_name"] is not None else ""
                history_msg += f"<code>{i}.</code> {formatted_timestamp}\n"
                history_msg += f"   <code>{change_first_name}</code> <code>{change_last_name}</code>\n"

                if history["username"]:
                    change_username = escape(history["username"])
                    history_msg += f"   @{change_username}\n"

                history_msg += "\n"

            await kirimPesan(m, history_msg, quote=True)
        else:
            await kirimPesan(m, "User data not found.")

@app.on_message(filters.group & filters.command("detectimposter") & ~filters.bot & ~filters.via_bot)
@adminsOnly("can_change_info")
async def set_mataa(_, m):
    if len(m.command) == 1:
        return await kirimPesan(m, f"Use <code>/{m.command[0]} on</code>, to enable Imposter Detection. If you want to disable, you can use off parameter.")
    if m.command[1] == "on":
        cekset = await is_sangmata_on(m.chat.id)
        if cekset:
            await kirimPesan(m, "Imposter Detection already enabled in your group.")
        else:
            await sangmata_on(m.chat.id)
            await kirimPesan(m, "Imposter Detection enabled in your group. I will track name and username changes in this chat. If a user changes their name and username, I will send a message showing any related changes.")
    elif m.command[1] == "off":
        cekset = await is_sangmata_on(m.chat.id)
        if not cekset:
            await kirimPesan(m, "Imposter Detection already disabled in your group.")
        else:
            await sangmata_off(m.chat.id)
            await kirimPesan(m, "Imposter Detection has been disabled in your group.")
    else:
        await kirimPesan(m, "Invalid command. Use <code>/detectimposter on/off</code> to enable or disable Imposter Detection in your chat.")

__mod_name__ = "ɪᴍᴘᴏsᴛᴇʀ ᴅᴇᴛᴇᴄᴛɪᴏɴ"
__help__ = """
*➛ /detectimposter:* Use this command to track name and username changes in the group. If a user changes their name and username, the bot will send a message showing any related changes.

*➛ /history:* Reply to a user with this command to get their previous name change history.
"""
