from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("PREFIX", ".")

if not TOKEN:
    raise ValueError("DISCORD_TOKEN not found in .env")
