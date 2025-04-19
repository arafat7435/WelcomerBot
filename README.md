# 🤖 Discord AI Welcome Bot (DeepSeek + OpenRouter)

A Discord bot that sends **smart, stylish, one-liner welcome messages** using **DeepSeek AI** via **OpenRouter** API.

---

## 💡 What does this bot do?

Whenever a new member joins your Discord server, the bot:
- Generates an **AI-based welcome message**
- Shows their **profile picture** in an embed
- Sends everything to a **specific welcome channel**

---

## ⚙️ Setup Instructions (Step-by-Step)

> ⚠️ Don’t skip any step. Just follow exactly 👇

---

### 1. 🎯 Requirements

- Python 3.8+
- `discord.py` and `requests` module
- An account on [OpenRouter.ai](https://openrouter.ai)
- A Discord bot with proper permissions

---

### 2. 🧠 Get Your OpenRouter API Key

1. Go to: [https://openrouter.ai/keys](https://openrouter.ai/keys)
2. Click **Create Key**
3. Copy your API key
4. Replace this in your code:

```python
OPENROUTER_API_KEY = "YOUR_OPENROUTER_API_KEY"
```

---

### 3. 🤖 Create & Setup Your Discord Bot

1. Visit: [https://discord.com/developers/applications](https://discord.com/developers/applications)
2. Click **"New Application"** → Give it a name
3. Go to **Bot** tab → Click **Add Bot**
4. Enable this intent:

```py
Server Members Intent ✅
```

5. Copy your bot token and paste it in your code:

```python
DISCORD_TOKEN = "YOUR_DISCORD_BOT_TOKEN"
```

---

### 4. 🔗 Invite Bot to Server

1. Go to **OAuth2 > URL Generator**
2. Select:
   - `bot`
   - `applications.commands`
3. Scroll down and select permissions:
   - ✅ Send Messages
   - ✅ Embed Links
   - ✅ Read Message History
   - ✅ View Channel

4. Copy the invite link and add the bot to your server

---

### 5. 🔥 Set Welcome Channel ID

1. Enable **Developer Mode** in Discord:  
   `User Settings > Advanced > Developer Mode ✅`
2. Right-click on the welcome channel → `Copy ID`
3. Paste in your code:

```python
WELCOME_CHANNEL_ID = 123456789012345678
```

---

### 6. 📦 Install Required Libraries

Open your terminal or CMD and run:

```bash
pip install discord.py requests
```

---

### 7. 🏃 Run the Bot

Run the bot with:

```bash
python main.py
```

You’ll see:

```bash
✅ Bot is online as YourBotName
```

---

### 8. 🛠 Customize Message or Model

You can change the AI prompt or model here:

```python
MODEL_NAME = "deepseek/deepseek-chat:free"
```

To use another model, check:  
👉 [https://openrouter.ai/docs#models](https://openrouter.ai/docs#models)

You can also tweak the style:

```python
"You are a Discord bot that creates stylish, short and unique welcome messages."
```

---

## ✅ What if AI fails?

Don’t worry. Your bot will auto fallback:

```python
Welcome {member.name} to {member.guild.name}! 🎉
```

So no errors will crash the bot 😎

---

## 📁 Files You Need

Only one file:

```
main.py
```

---

## 🔒 Bot Permissions Required

Make sure the bot has these permissions in your server:

- ✅ View Channel
- ✅ Send Messages
- ✅ Embed Links
- ✅ Read Message History

---

## ✨ Example Output

> 👋 Welcome, Syed!  
> "Brace yourselves, legends never arrive quietly."  
> *(With their avatar and your server name)*

---

## 🧑‍💻 Author

Made with ❤️ by @SyedArafat
Feel free to fork or use in your server!

---
