from aiohttp import web
from app.database import get_file_name
from pyrogram.raw.functions.messages import GetMessages
from app.config import Config
from pyrogram import Client
import os

async def web_server(bot_token: str):
    routes = web.RouteTableDef()
    app = web.Application()

    bot = Client("bot", bot_token=bot_token, api_id=Config.API_ID, api_hash=Config.API_HASH)

    await bot.start()

    @routes.get("/{file_id}/{file_name}")
    async def serve_file(request):
        file_id = request.match_info["file_id"]
        file_name = request.match_info["file_name"]

        saved_name = get_file_name(file_id)
        if not saved_name:
            return web.Response(text="File not found", status=404)

        try:
            tg_link = await bot.get_file(file_id)
            tg_url = f"https://api.telegram.org/file/bot{Config.BOT_TOKEN}/{tg_link.file_path}"
            raise web.HTTPFound(tg_url)
        except Exception as e:
            return web.Response(text="Failed to fetch file", status=500)

    app.add_routes(routes)
    return app
