from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import OWNER_ID, BOT_STATS_TEXT, USER_REPLY_TEXT
from datetime import datetime
from helper_func import get_readable_time
from database.database import full_userbase

# --- SMART AUTO-REPLY & COMMAND CHECK ---
@Bot.on_message(filters.private & filters.incoming)
async def handle_private_messages(bot: Bot, message: Message):
    user_id = message.from_user.id
    text = message.text if message.text else ""

    # 1. Agar user command use kar raha hai (/ se shuru)
    if text.startswith("/"):
        # List of admin commands
        admin_commands = ["/stats", "/broadcast", "/cancel", "/status"]
        
        # Check agar command admin wala hai aur user owner nahi hai
        current_cmd = text.split()[0].lower()
        if current_cmd in admin_commands and user_id != OWNER_ID:
            if USER_REPLY_TEXT:
                return await message.reply_text(USER_REPLY_TEXT)
            return

    # 2. Agar normal message hai (command nahi hai) aur user owner nahi hai
    if not text.startswith("/") and user_id != OWNER_ID:
        if USER_REPLY_TEXT:
            await message.reply_text(USER_REPLY_TEXT)

# --- SECURE STATS COMMAND ---
@Bot.on_message(filters.command('stats') & filters.private)
async def stats(bot: Bot, message: Message):
    user_id = message.from_user.id
    
    # Extra Security Check
    if user_id != OWNER_ID:
        if USER_REPLY_TEXT:
            return await message.reply_text(USER_REPLY_TEXT)
        return

    # Owner ke liye Stats process karna
    now = datetime.now()
    delta = now - bot.uptime
    uptime_time = get_readable_time(delta.seconds)
    
    wait_msg = await message.reply_text("<code>📊 Processing Stats...</code>")
    
    try:
        users_list = await full_userbase()
        total_users = len(users_list)
    except:
        total_users = "Error"

    final_text = (
        "<b>📊 ᴀɴɪʀᴇᴀʟ ᴘʀɪᴠᴀᴛᴇ sᴛᴀᴛs</b>\n\n"
        f"<b>🚀 ᴜᴘᴛɪᴍᴇ:</b> <code>{uptime_time}</code>\n"
        f"<b>👤 ᴛᴏᴛᴀʟ ᴜsᴇʀs:</b> <code>{total_users}</code>\n"
        f"<b>🔐 ᴀᴄᴄᴇss:</b> ꜰᴜʟʟ ᴄᴏɴᴛʀᴏʟ"
    )
    
    await wait_msg.edit_text(final_text)
