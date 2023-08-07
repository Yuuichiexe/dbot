import asyncio
import os
import subprocess
import time

import psutil
from pyrogram import filters

from DazaiRobot import StartTime, DEV_USERS, pbot
import DazaiRobot.utils.formatter as formatter
import DazaiRobot.modules.sql.users_sql as sql




# Stats Module

async def bot_sys_stats():
    bot_uptime = int(time.time() - StartTime)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    users = sql.num_users()
    chats = sql.num_chats()
    stats = f"""
➢ 𝖣𝖺𝗓𝖺𝗂'𝗌 𝖼𝗎𝗋𝗋𝖾𝗇𝗍 𝗌𝗒𝗌𝗍𝖾𝗆 𝗌𝗍𝖺𝗍𝗌:

───────────────────────
• UPTIME: {formatter.get_readable_time((bot_uptime))}
• BOT: {round(process.memory_info()[0] / 1024 ** 2)} MB
• CPU: {cpu}%
• RAM: {mem}%
• DISK: {disk}%
• CHATS: {chats}
• USERS: {users}
───────────────────────
"""
    return stats
    
