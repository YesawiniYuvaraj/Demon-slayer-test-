import os
from os import environ

def getConfig(name: str):
    try:
        return environ[name]
    except:
        return ""

BOT_OWNER = environ("BOT_OWNER", "")
API_ID = environ("API_ID", "")
API_HASH = environ("API_HASH", "")
