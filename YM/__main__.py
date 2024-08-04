import os
import uvicorn
import asyncio
import socketio
from bot import bot
from YM import LOGGER
from pyrogram import idle
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

load_dotenv()

# Create FastAPI app instance
app = FastAPI()

# Configure static files directory
app.mount("/static", StaticFiles(directory="YM/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("YM/templates/index.html", "r") as f:
        return HTMLResponse(content=f.read(), status_code=200)

# Configure Socket.IO server
sio = socketio.AsyncServer(async_mode='asgi')
sio_app = socketio.ASGIApp(sio, other_asgi_app=app)

@sio.event
async def message(sid, data):
    await sio.emit('response', f"Message received: {data}")

async def start_bot():
    LOGGER("YM").info("Starting bot...")
    await bot.start()
    await bot.send_message(-1002136795173, "Started")
    LOGGER("YM").info(f"Bot Started As {bot.me.first_name}")
    await idle()

async def start_server():
    config = uvicorn.Config(app=sio_app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)), workers=1)
    server = uvicorn.Server(config)
    LOGGER("YM").info("\x53\x54\x41\x52\x54\x45\x44\x20\x57\x45\x42\x20\x43\x4c\x45\x4e\x54\x0a\x4d\x41\x44\x45\x20\x42\x59\x20\x59\x4f\x55\x52\x20\x46\x41\x54\x48\x45\x52\x20\x56\x49\x4b\x52\x41\x4e\x54\x20\x40\x44\x55\x44\x45\x5f\x31\x32\x30\x33\x0a\x42\x45\x54\x45\x20\x42\x41\x43\x48\x41\x20\x48\x45\x49\x20\x42\x41\x43\x48\x41\x20\x48\x49\x20\x52\x41\x48\x4c\x45\x0a\x43\x4f\x50\x59\x20\x4b\x52\x4e\x45\x20\x4b\x45\x20\x42\x41\x41\x44\x20\x56\x49\x4b\x52\x41\x4e\x54\x20\x50\x41\x50\x41\x20\x4b\x41\x20\x43\x52\x45\x44\x49\x54\x20\x44\x45\x44\x45\x4e\x41")
    await server.serve()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())
    loop.run_until_complete(start_server())
