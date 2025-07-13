import asyncio
from pyrogram import Client
from app.config import Config
from app import handlers
from aiohttp import web
from app.server import web_server

bot = Client("bot", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)

async def start():
    await bot.start()
    print("Bot started")

    app = await web_server(Config.BOT_TOKEN)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", Config.PORT)
    await site.start()
    print(f"Server running at http://0.0.0.0:{Config.PORT}")

    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(start())
