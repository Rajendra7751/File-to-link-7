import asyncio
from pyrogram import Client
from aiohttp import web
from app.config import Config
from app.handlers import *
from app.server import web_server

# Initialize Pyrogram Client
bot = Client(
    "bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

async def main():
    await bot.start()
    print(f"✅ Bot @{(await bot.get_me()).username} started!")

    # Start aiohttp server
    app = await web_server(Config.BOT_TOKEN)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", Config.PORT)
    await site.start()
    print(f"🌐 Web server running at http://0.0.0.0:{Config.PORT}")

    await asyncio.Event().wait()  # keep the app running

if __name__ == "__main__":
    asyncio.run(main())
