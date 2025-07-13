from pyrogram import Client, filters
from pyrogram.types import Message
from app.database import insert_file
from app.config import Config

@Client.on_message(filters.private & filters.document)
async def handle_private_file(bot, message: Message):
    file_id = message.document.file_id
    file_name = message.document.file_name

    insert_file(file_id, file_name)
    link = f"https://{Config.FQDN}/{file_id}/{file_name}"
    await message.reply(f"🔗 Your download link:\n{link}")

@Client.on_message(filters.channel & filters.document)
async def handle_channel_file(bot, message: Message):
    file_id = message.document.file_id
    file_name = message.document.file_name

    insert_file(file_id, file_name)
    link = f"https://{Config.FQDN}/{file_id}/{file_name}"

    try:
        await message.reply_text(
            f"🎬 Download / Stream",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📥 Watch/Download", url=link)]]
            )
        )
    except Exception:
        pass
