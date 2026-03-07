from pyrogram import Client, filters
from config import LOGGER

@Client.on_message(filters.all, group=-1)
async def debug_log(client, message):
    LOGGER(__name__).info(f"Received message from {message.from_user.id if message.from_user else 'unknown'} in {message.chat.id}: {message.text or message.caption or 'no text'}")
