import os
from os import environ

def getConfig(name: str):
    try:
        return environ[name]
    except:
        return ""

API_ID = environ("API_ID", "18990697")
API_HASH = environ("API_HASH", "f4815b9a16cb03c2f5eabe8db1cb0903")
