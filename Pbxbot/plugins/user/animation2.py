# This plugin create by @II_BAD_MUNDA_II

import asyncio
import random
from collections import deque
import requests
from pyrogram import *
from pyrogram import Client, filters
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.types import *
from pyrogram.types import Message

from Pbxbot.bad.bad import edit_or_reply, get_text
from Pbxbot.bad.constants import MEMES
from . import *

DEFAULTUSER = "Bad"

@on_message("plain", allow_stan=True)
async def hello_world(client: Client, message: Message):
    mg = await edit_or_reply(message, "Wait for plane...")
    await asyncio.sleep(0.2)
    await mg.edit("✈-------------")
    await asyncio.sleep(0.2)
    await mg.edit("-✈------------")
    await asyncio.sleep(0.2)
    await mg.edit("--✈-----------")
    await asyncio.sleep(0.2)
    await mg.edit("---✈----------")
    await asyncio.sleep(0.2)
    await mg.edit("----✈---------")
    await asyncio.sleep(0.2)
    await mg.edit("-----✈--------")
    await asyncio.sleep(0.2)
    await mg.edit("------✈-------")
    await asyncio.sleep(0.2)
    await mg.edit("-------✈------")
    await asyncio.sleep(0.2)
    await mg.edit("--------✈-----")
    await asyncio.sleep(0.2)
    await mg.edit("---------✈----")
    await asyncio.sleep(0.2)
    await mg.edit("----------✈---")
    await asyncio.sleep(0.2)
    await mg.edit("-----------✈--")
    await asyncio.sleep(0.2)
    await mg.edit("------------✈-")
    await asyncio.sleep(0.2)
    await mg.edit("------------✈")
    

@on_message("addsudo", allow_stan=True)
async def hajqag(client: Client, message: Message):
    if message.forward_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 18)
    await message.edit("Deploying........")
    animation_chars = [
"**Heroku Connecting To Latest [Github Build](Badhacker98/PBX_2.0)**",
            f"**Build started by user** {DEFAULTUSER}",
            f"**Deploy** `535a74f0` **by user** **{DEFAULTUSER}**",
            "**Restarting Heroku Server...**",
            "**State changed from up to starting**",    
            "**Stopping all processes with SIGTERM**",
            "**Process exited with** `status 143`",
            "**Starting process with command** `python3 -m stdborg`",
            "**State changed from starting to up**",
            "__INFO:Pbxẞø†:Logged in as 557667062__",
            "__INFO:Pbxẞø†:Successfully loaded all plugins__",
            "**Build Succeeded**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 18])

@on_message("music", allow_stan=True)
async def pijtau(client: Client, message: Message):
    if message.forward_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 14)
    await message.edit("starting player...")
    animation_chars = [
        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/mivubot)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:00** ▱▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `▶️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: I Fone XXX**",
        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/mivubot)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:01** ▰▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Ifone XXX**",
        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/mivubot)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:02** ▰▰▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Ifone XXX**",
        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/mivubot)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:03** ▰▰▰▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Ifone XXX**",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/mivubot)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:04** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Ifone XXX**",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/mivubot)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:05** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Ifone XXX**",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/mivubot)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:06** ▰▰▰▰▰▰▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Ifone XXX**",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/mivubot)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:07** ▰▰▰▰▰▰▰▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Ifone XXX**",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/mivubot)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:08** ▰▰▰▰▰▰▰▰▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Ifone XXX**",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/mivubot)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:09** ▰▰▰▰▰▰▰▰▰▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Ifone XXX**",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/mivubot)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:10** ▰▰▰▰▰▰▰▰▰▰ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏺️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Ifone XXX**",
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 14])

@on_message("snake", allow_stan=True)
async def pijtau(client: Client, message: Message):
    if message.forward_from:
        return
    animation_interval = 0.3
    animation_ttl = range(27)
    await message.edit("snake....")
    animation_chars = [
    "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "‎◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◼️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◼️◻️◼️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 27])

@on_message("mc", allow_stan=True)
async def pijtau(client: Client, message: Message):
    if message.forward_from:
        return
    animation_interval = 0.3
    animation_ttl = range(28)
    await message.edit("mcc....")
    animation_chars = [
"◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◻️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◻️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◻️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◻️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◻️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◻️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◻️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◻️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◻️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◻️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◻️◼️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◻️◻️◻️◼️\n◼️◼️◼️◼️◼️",
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 28])

@on_message("nikal", allow_stan=True)
async def pijtau(client: Client, message: Message):
    if message.forward_from:
        return
    animation_interval = 0.5
    animation_ttl = range(6)
    await message.edit("bhkkkk....")
    animation_chars = [
"`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀  ⠀   ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Nikal   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀      ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Lavde   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__|⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Pehli   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀         ⡇\n  ⠙⢿⣯⠄⠀⠀(P)⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀   ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Fursat  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__ ⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀ ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Meeee   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__| ⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀  ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Nikal   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀lodu⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 6])

@on_message("gm", allow_stan=True)
async def pijtau(client: Client, message: Message):
    if message.forward_from:
        return
    animation_interval = 0.5
    animation_ttl = range(6)
    await message.edit("ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ...")
    animation_chars = [
    "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･\n╱╱╱╱╱╱╱╭╮╱╱╱╭╮╱╭╮╭╮\n╭━┳━┳━┳╯┃╭━┳╋╋━┫╰┫╰╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃┃╋┃┃┃╭┫\n┣╮┣━┻━┻━╯╰┻━┻╋╮┣┻┻━╯\n╰━╯╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥° ♥｡･ﾟ♡ﾟ･",
            ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 6])
        
        
@on_message("gn", allow_stan=True)
async def pijtau(client: Client, message: Message):
    if message.forward_from:
        return
    animation_interval = 0.5
    animation_ttl = range(6)
    await message.edit("ɢᴏᴏᴅ ɴɪɢʜᴛ...")
    animation_chars = [
    "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･\n╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮\n╭━┳━┳━┳╯┃╭━━┳━┳┳┳━┳╋╋━┳┳━╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃\n┣╮┣━┻━┻━╯╰┻┻┻━┻╯╰┻━┻┻┻━╋╮┃\n╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･",
        ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 6])

@on_message("Pikachu", allow_stan=True)
async def gunid(client: Client, message: Message):
    await edit_or_reply(
        message,
        "⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿\n"
"⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿\n"
"⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿\n"
"⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿\n"
"⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿\n"
"⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿\n"
"⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿\n"
"⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿\n"
"⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿\n"
"⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿\n"
"⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿\n"
)

HelpMenu("animation2").add(
    "soon.",
).info("Away From Keyboard").done()
