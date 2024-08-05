import random
import string

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message
from pytgcalls.exceptions import NoActiveGroupCall

import config
from DCxMUSIC import Telegram, YouTube, app
from DCxMUSIC.core.call import DC
from DCxMUSIC.utils import seconds_to_min, time_to_seconds
from DCxMUSIC.utils.channelplay import get_channeplayCB
from DCxMUSIC.utils.decorators.language import languageCB
from DCxMUSIC.utils.decorators.play import PlayWrapper
from DCxMUSIC.utils.formatters import formats
from DCxMUSIC.utils.inline import (
    botplaylist_markup,
    livestream_markup,
    playlist_markup,
    slider_markup,
    track_markup,
)
from DCxMUSIC.utils.logger import play_logs
from DCxMUSIC.utils.stream.stream import stream
from config import BANNED_USERS, lyrical

@app.on_message(
    filters.command(
        [
            "play",
        ]
    )
    & filters.group
    & ~BANNED_USERS
)
@PlayWrapper
async def play_commnd(
    client,
    message: Message,
    _,
    chat_id,
    video,
    channel,
    playmode,
    url,
    fplay,
):
    mystic = await message.reply_text(
        _["play_2"].format(channel) if channel else _["play_1"]
    )
    plist_id = None
    slider = None
    plist_type = None
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    audio_telegram = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    video_telegram = (
        (message.reply_to_message.video or message.reply_to_message.document)
        if message.reply_to_message
        else None
    )
    if audio_telegram:
        #...
    elif video_telegram:
        #...
    elif url:
        if await YouTube.exists(url):
            #...
        else:
            try:
                await DC.stream_call(url)
            except NoActiveGroupCall:
                await mystic.edit_text(_["black_9"])
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=_["play_17"],
                )
            except Exception as e:
                return await mystic.edit_text(_["general_2"].format(type(e).__name__))
            await mystic.edit_text(_["str_2"])
            try:
                await stream(
                    _,
                    mystic,
                    message.from_user.id,
                    url,
                    chat_id,
                    message.from_user.first_name,
                    message.chat.id,
                    video=video,
                    streamtype="index",
                    forceplay=fplay,
                )
            except Exception as e:
                ex_type = type(e).__name__
                err = e if ex_type == "AssistantErr" else _["general_2"].format(ex_type)
                return await mystic.edit_text(err)
            return await play_logs(message, streamtype="M3u8 or Index Link")
    else:
        #...

@app.on_callback_query(filters.regex("MusicStream") & ~BANNED_USERS)
@languageCB
async def play_music(client, CallbackQuery, _):
    #...

@app.on_callback_query(filters.regex("YMPlaylists") & ~BANNED_USERS)
@languageCB
async def play_playlists_command(client, CallbackQuery, _):
    #...

@app.on_callback_query(filters.regex("slider") & ~BANNED_USERS)
@languageCB
async def slider_queries(client, CallbackQuery, _):
    #...

# New code for web player
@app.on_message(filters.command("webplay") & filters.group & ~BANNED_USERS)
@PlayWrapper
async def webplay_commnd(client, message: Message, _, chat_id, video, channel, playmode, url, fplay):
    mystic = await message.reply_text("Web player is loading...")
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    if url:
        try:
            await stream(
                _,
                mystic,
                user_id,
                url,
                chat_id,
                user_name,
                message.chat.id,
                video=video,
                streamtype="web",
                forceplay=fplay,
            )
        except Exception as e:
            ex_type = type