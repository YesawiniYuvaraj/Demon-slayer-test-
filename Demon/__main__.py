from pyrogram import *
import psycopg2
from Demon import *
from pyrogram.types import *
import asyncio
import datetime
from Demon.plugins import ALL_MODULES
import importlib
from vars import SQLDB

loop = asyncio.get_event_loop()

DB_URI = SQLDB
DB = psycopg2.connect(DB_URI)
cur = DB.cursor()

async def main() -> None:
    "Normal Code To Start And Idle The Demon-Slayer-Bot"

    global HELPABLE

    for module in ALL_MODULES:
        imported_module = importlib.import_module("Demon.plugins." + module)
        if (
                hasattr(imported_module, "__MODULE__")
                and imported_module.__MODULE__
        ):
            imported_module.__MODULE__ = imported_module.__MODULE__

    bot_modules = ""
    tot = 0
    for i in ALL_MODULES:
        bot_modules += f"{i}\t"
        tot += 1
        
    LOGGER.info("LOADED THESE PLUGINS :")
    LOGGER.info(bot_modules)
    LOGGER.info(f"MODULE LOADED {tot}")
    
    await app.start()
    LOGGER.info("CONNECTED DB")
    cur.execute("Select 1")
    x = [y[0] for y in cur.fetchall()]
    if 1 in x :
        LOGGER.info("CONNECTED DB")
    else : 
        LOGGER.info("CAN'T CONNECT TO DB")

    await idle()
    await app.stop()

if __name__ == "__main__":
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt :
        LOGGER.info("STOPPED")
