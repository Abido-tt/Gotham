import discord
from discord.ext import commands
from config import TOKEN, PREFIX
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix=PREFIX,
    intents=intents,
    help_command=None
)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print(f"Bot ID: {bot.user.id}")

    try:
        synced = await bot.tree.sync()
        print([cmd.name for cmd in synced])
        print(f"Synced {len(synced)} slash commands")
    except Exception as e:
        print(f"Sync error: {e}")

async def load_cogs():
    await bot.load_extension("cogs.utility")
    await bot.load_extension("cogs.moderation")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

asyncio.run(main())
