import discord
import requests
from discord.ext import commands

# ==== SETUP ====
DISCORD_TOKEN = "YOUR_DISCORD_BOT_TOKEN" #dc bot token
OPENROUTER_API_KEY = "YOUR_OPENROUTER_API_KEY" # open rauter api
WELCOME_CHANNEL_ID = 123456789012345678 #chanel id

MODEL_NAME = "deepseek/deepseek-chat:free" #check your model
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# ==== DISCORD SETUP ====
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

def generate_welcome_text(username: str, server_name: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a Discord bot that creates stylish, short and unique welcome messages."},
            {"role": "user", "content": f"Generate a cool one-liner welcome message for a user named '{username}' who just joined a Discord server called '{server_name}'."}
        ]
    }
    response = requests.post(OPENROUTER_API_URL, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user.name}")

@bot.event
async def on_member_join(member: discord.Member):
    try:
        ai_message = generate_welcome_text(member.name, member.guild.name)
    except Exception as e:
        print(f"AI Error: {e}")
        ai_message = f"Welcome {member.name} to {member.guild.name}! 🎉"

    embed = discord.Embed(
        title=f"👋 Welcome, {member.name}!",
        description=ai_message,
        color=discord.Color.green()
    )
    embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
    embed.set_footer(text=f"Welcome to {member.guild.name} ✨")

    channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
    if channel and channel.permissions_for(member.guild.me).send_messages:
        await channel.send(embed=embed)

bot.run(DISCORD_TOKEN)
