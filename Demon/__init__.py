from pyrogram import *
from pyrogram.types import *
from Demon.vars import API_ID, API_HASH
from aiohttp import ClientSession
import logging
import asyncio
import os

FORMAT = "[None] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("botlogs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
LOGGER = logging.getLogger('[None]')
LOGGER.info("BOT STARTING !")

BOT_TOKEN = "" # Your Bot Token Here ....
TOKEN = BOT_TOKEN
ID = API_ID
HASH = API_HASH

# PYROGRAM CLIENT
pyro = Client(
    "DemonSlayer",
    api_id=ID,
    api_hash=HASH,
    bot_token=TOKEN
)
