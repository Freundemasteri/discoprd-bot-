import discord
from discord.ext import commands
import os

intents = discord.Intents.all()  # Wichtig, damit Kick funktioniert
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot ist online als {bot.user}')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(f"{member} wurde gekickt! Grund: {reason}")
    except discord.Forbidden:
        await ctx.send("Ich habe keine Berechtigung, diesen Nutzer zu kicken.")
    except Exception as e:
        await ctx.send(f"Fehler: {e}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
