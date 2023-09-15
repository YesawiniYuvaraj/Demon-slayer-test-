from pyrogram import *
from pyrogram.types import *
from Demon.vers import API_ID, API_HASH, BOT_TOKEN, BOT_OWNER
from aiohttp import ClientSession
import logging
import asyncio
import os

FORMAT = "[None] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
LOGGER = logging.getLogger('[None]')
LOGGER.info("BOT STARTING !")

pyro = Client(
    "DemonSlayer",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN
)
