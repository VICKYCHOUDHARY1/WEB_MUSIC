import random
from typing import Dict, List, Union

from YM.core import userbot
from YM.core.mongo import mongodb

authdb = mongodb.adminauth
authuserdb = mongodb.authuser
autoenddb = mongodb.autoend
assdb = mongodb.assistants
blacklist_chatdb = mongodb.blacklistChat
blockeddb = mongodb.blockedusers
chatsdb = mongodb.chats
channeldb = mongodb.cplaymode
countdb = mongodb.upcount
gbansdb = mongodb.gban
langdb = mongodb.language
onoffdb = mongodb.onoffper
playmodedb = mongodb.playmode
playtypedb = mongodb.playtypedb
skipdb = mongodb.skipmode
sudoersdb = mongodb.sudoers
usersdb = mongodb.tgusersdb

# Shifting to memory [mongo sucks often]
active = []
activevideo = []
assistantdict = {}
autoend = {}
count = {}
channelconnect = {}
langm = {}
loop = {}
maintenance = []
nonadmin = {}
pause = {}
playmode = {}
playtype = {}
skipmode = {}

async def get_assistant_number(chat_id: int) -> str:
    assistant = assistantdict.get(chat_id)
    return assistant

async def get_client(assistant: int):
    return userbot

async def set_assistant_new(chat_id, number):
    number = int(number)
    await assdb.update_one(
        {"chat_id": chat_id},
        {"$set": {"assistant": number}},
        upsert=True,
    )

async def set_assistant(chat_id):
    assistantdict[chat_id] = 1
    await assdb.update_one(
        {"chat_id": chat_id},
        {"$set": {"assistant": 1}},
        upsert=True,
    )
    return userbot

async def get_assistant(chat_id: int) -> str:
    assistant = assistantdict.get(chat_id)
    if not assistant:
        dbassistant = await assdb.find_one({"chat_id": chat_id})
        if not dbassistant:
            userbot = await set_assistant(chat_id)
            return userbot
        else:
            got_assis = dbassistant["assistant"]
            if got_assis == 1:
                assistantdict[chat_id] = got_assis
                return userbot
            else:
                userbot = await set_assistant(chat_id)
                return userbot
    else:
        if assistant == 1:
            return userbot
        else:
            userbot = await set_assistant(chat_id)
            return userbot

async def is_skipmode(chat_id: int) -> bool:
    mode = skipmode.get(chat_id)
    if not mode:
        user = await skipdb.find_one({"chat_id": chat_id})
        if not user:
            skipmode[chat_id] = True
            return True
        skipmode[chat_id] = False
        return False
    return mode

async def skip_on(chat_id: int):
    skipmode[chat_id] = True
    user = await skipdb.find_one({"chat_id": chat_id})
    if user:
        return await skipdb.delete_one({"chat_id": chat_id})

async def skip_off(chat_id: int):
    skipmode[chat_id] = False
    user = await skipdb.find_one({"chat_id": chat_id})
    if not user:
        return await skipdb.insert_one({"chat_id": chat_id})

async def get_upvote_count(chat_id: int) -> int:
    mode = count.get(chat_id)
    if not mode:
        mode = await countdb.find_one({"chat_id": chat_id})
        if not mode:
            return 5
        count[chat_id] = mode["mode"]
        return mode["mode"]
    return mode

async def set_upvotes(chat_id: int, mode: int):
    count[chat_id] = mode
    await countdb.update_one(
        {"chat_id": chat_id}, {"$set": {"mode": mode}}, upsert=True
    )

async def is_autoend() -> bool:
    chat_id = 1234
    user = await autoenddb.find_one({"chat_id": chat_id})
    if not user:
        return False
    return True

async def autoend_on():
    chat_id = 1234
    await autoenddb.insert_one({"chat_id": chat_id})

async def autoend_off():
    chat_id = 1234
    await autoenddb.delete_one({"chat_id": chat_id})

async def get_loop(chat_id: int) -> int:
    lop = loop.get(chat_id)
    if not lop:
        return 0
    return lop

async def set_loop(chat_id: int, mode: int):
    loop[chat_id] = mode

async def get_cmode(chat_id: int) -> int: