# Quick Start Guide

Get your Discord Daily Poll Bot running in 5 minutes!

## 🚀 Quick Setup

### 1. Get Bot Token (2 minutes)
1. Go to https://discord.com/developers/applications
2. Click "New Application" → Name it → Create
3. Go to "Bot" → "Add Bot" → Confirm
4. Click "Reset Token" → Copy the token
5. Enable "Message Content Intent" under Privileged Gateway Intents
6. Save changes

### 2. Invite Bot to Server (1 minute)
1. Go to "OAuth2" → "URL Generator"
2. Select "bot" scope
3. Select "Send Messages" permission
4. Copy URL → Open in browser → Select your server → Authorize

### 3. Install & Configure (1 minute)
```bash
# Install dependencies
pip install -r requirements.txt

# Create .env file
copy env_example.txt .env

# Edit .env and add your token:
# DISCORD_BOT_TOKEN=your_token_here
```

### 4. Run Bot (1 minute)
```bash
python bot.py
```

**Done!** The bot will:
- ✅ Connect to Discord
- ✅ Find all "votazioni" channels
- ✅ Post polls daily at midnight GMT+1

## 📋 What You Need

**Only 1 thing required:**
- **Discord Bot Token** (free, from Discord Developer Portal)

**No API keys needed!** This bot uses Discord's native features only.

## 🧪 Test First

Before going live, run tests:
```bash
python test_bot.py
```

All tests should pass. See `TESTING_GUIDE.md` for detailed testing.

## 📚 Full Documentation

- **README.md** - Complete setup and deployment guide
- **TESTING_GUIDE.md** - How to test the bot
- **QUICK_START.md** - This file (quick setup)

## ⚙️ Configuration

All settings are in `bot.py`:
- **Timezone**: `TIMEZONE = pytz.timezone('Europe/Rome')` (GMT+1)
- **Time Options**: `TIME_OPTIONS = [7, 9, 11, 13, 15, 17, 19, 21, 23]`
- **Poll Duration**: `POLL_DURATION_HOURS = 24`

## 🐛 Troubleshooting

**Bot won't connect?**
- Check `.env` file has correct token
- Verify bot is invited to server

**Polls not posting?**
- Check bot has "Send Messages" permission
- Verify channels with "votazioni" in name exist
- See README.md for more help

## 🚢 Going Live

For 24/7 operation, deploy to:
- Cloud server (Heroku, DigitalOcean, AWS)
- Raspberry Pi
- Always-on computer

See README.md "Deployment" section for details.

---

**Need help?** Check README.md or TESTING_GUIDE.md for detailed instructions.

