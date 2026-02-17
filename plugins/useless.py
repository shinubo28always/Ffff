from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import OWNER_ID, BOT_STATS_TEXT, USER_REPLY_TEXT
from datetime import datetime
from helper_func import get_readable_time
from database.database import full_userbase

# --- 1. NORMAL USER KE LIYE AUTO-REPLY ---
# Isme humne commands ko exclude kar diya hai (~filters.command)
@Bot.on_message(filters.private & filters.incoming & ~filters.command(['start', 'stats', 'broadcast', 'cancel']))
async def useless_reply(bot: Bot, message: Message):
    user_id = message.from_user.id
    if user_id != OWNER_ID: # Sirf unko reply jaye jo owner nahi hain
        if USER_REPLY_TEXT:
            await message.reply_text(USER_REPLY_TEXT)

# --- 2. STATS COMMAND (WITH SECURITY) ---
@Bot.on_message(filters.command('stats') & filters.private)
async def stats(bot: Bot, message: Message):
    user_id = message.from_user.id
    
    # AGAR NORMAL USER HAI
    if user_id != OWNER_ID:
        if USER_REPLY_TEXT:
            await message.reply_text(USER_REPLY_TEXT)
        return

    # AGAR OWNER HAI
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
