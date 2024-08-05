from pyrogram import Client

import config

from ..logging import LOGGER

class Userbot(Client):
    def __init__(self):
        super().__init__(
            name="DCxMUSIC",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Userbot...")
        await self.start()
        try:
            await self.join_chat("TEAM_DC_BOTS")
            await self.join_chat("TEAM_DC_BOTS")
        except:
            pass
        LOGGER(__name__).info(f"Userbot Started as {self.me.mention}")

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Userbot...")
        await self.stop()

# Create a single instance of the Userbot
userbot = Userbot()