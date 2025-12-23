# Discord Daily Poll Bot

A Discord bot that automatically posts daily polls at midnight (GMT+1, Italy timezone) in all channels with "votazioni" in their name.

## Features

- ✅ **Daily Automatic Polls**: Posts polls automatically at midnight GMT+1 (Italy timezone)
- ✅ **Date as Title**: Poll title is the current date (DD/MM/YYYY format)
- ✅ **Multiple Time Options**: 7, 9, 11, 13, 15, 17, 19, 21, 23
- ✅ **Discord Native Polls**: Uses Discord's built-in poll feature
- ✅ **24-Hour Duration**: Polls stay open for 24 hours
- ✅ **Multi-Select**: Users can select multiple time options
- ✅ **Auto-Detection**: Automatically finds all channels with "votazioni" in the name

## Requirements

- Python 3.8 or higher
- Discord Bot Token (see setup instructions below)
- Required Python packages (see `requirements.txt`)

## Setup Instructions

### 1. Create a Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **"New Application"** and give it a name (e.g., "Daily Poll Bot")
3. Go to the **"Bot"** section in the left sidebar
4. Click **"Add Bot"** and confirm
5. Under **"Token"**, click **"Reset Token"** or **"Copy"** to get your bot token
   - ⚠️ **IMPORTANT**: Keep this token secret! Never share it publicly.
6. Scroll down and enable these **Privileged Gateway Intents**:
   - ✅ **Message Content Intent** (required for polls)
   - ✅ **Server Members Intent** (optional, but recommended)
7. Save changes

### 2. Invite Bot to Your Server

1. Go to the **"OAuth2"** → **"URL Generator"** section
2. Select **"bot"** scope
3. Select these bot permissions:
   - ✅ **Send Messages**
   - ✅ **Create Public Threads** (optional)
   - ✅ **Use External Emojis** (optional)
4. Copy the generated URL and open it in your browser
5. Select your server (the one with votazioni channels) and authorize

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or if you're using Python 3 specifically:

```bash
python3 -m pip install -r requirements.txt
```

### 4. Configure Bot Token

1. Copy the `.env.example` file to `.env`:
   ```bash
   copy .env.example .env
   ```
   (On Linux/Mac: `cp .env.example .env`)

2. Open `.env` in a text editor and replace `your_bot_token_here` with your actual bot token:
   ```
   DISCORD_BOT_TOKEN=YOUR_ACTUAL_BOT_TOKEN_HERE
   ```

### 5. Run the Bot

**Option A: Using the setup script (Recommended for first time)**
```bash
python run_local.py
```
This script will check your setup and guide you through any issues.

**Option B: Direct run**
```bash
python bot.py
```

The bot will:
- Connect to Discord
- Find all channels with "votazioni" in their name
- Wait until midnight GMT+1
- Post polls automatically every day at midnight

## Testing

### Run Automated Tests

```bash
python test_bot.py
```

This will test:
- ✅ Timezone calculations
- ✅ Time options configuration
- ✅ Channel finding logic
- ✅ Poll data structure
- ✅ Midnight scheduling calculation
- ✅ Simulated poll creation

### Manual Testing

1. **Test Bot Connection**:
   - Run `python bot.py`
   - Check console for "has logged in!" message
   - Verify bot appears online in your Discord server

2. **Test Channel Detection**:
   - The bot will automatically find channels with "votazioni" in the name
   - Check console output for found channels

3. **Test Poll Creation** (Optional - modify code temporarily):
   - You can temporarily modify `bot.py` to create a poll immediately for testing
   - Add this after `on_ready()`:
   ```python
   # Test poll creation (remove after testing)
   async def test_poll():
       await self.wait_until_ready()
       for guild in self.guilds:
           channels = self.find_votazioni_channels(guild)
           for channel in channels:
               await self.create_daily_poll(channel)
   asyncio.create_task(test_poll())
   ```

## Deployment

### Option 1: Local Computer (24/7)

1. Keep your computer running 24/7
2. Run the bot in a terminal or as a background service
3. Use a process manager like `pm2` (Node.js) or `screen`/`tmux` (Linux) to keep it running

**Windows (PowerShell)**:
```powershell
# Run in background
Start-Process python -ArgumentList "bot.py" -WindowStyle Hidden
```

**Linux/Mac**:
```bash
# Using screen
screen -S discord_bot
python bot.py
# Press Ctrl+A then D to detach
```

### Option 2: Cloud Server (Recommended)

Deploy to a cloud service that runs 24/7:

#### **Heroku** (Free tier available):
1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Create `Procfile`:
   ```
   worker: python bot.py
   ```
3. Deploy:
   ```bash
   heroku login
   heroku create your-bot-name
   heroku config:set DISCORD_BOT_TOKEN=your_token_here
   git push heroku main
   ```

#### **DigitalOcean / AWS / Azure**:
1. Create a virtual server (droplet/instance)
2. Install Python and dependencies
3. Upload bot files
4. Run as a systemd service or use PM2

#### **Replit / Glitch**:
1. Upload bot code
2. Set environment variable `DISCORD_BOT_TOKEN`
3. Keep the repl/glitch running (may require paid plan for 24/7)

### Option 3: Raspberry Pi / Home Server

1. Install Python on your Raspberry Pi
2. Set up the bot as described above
3. Run it as a systemd service for auto-start on boot

## Configuration

### Timezone

The bot is configured for **GMT+1 (Italy timezone)**. To change:

Edit `bot.py`:
```python
TIMEZONE = pytz.timezone('Europe/Rome')  # Change to your timezone
```

Common timezones:
- `'Europe/London'` - GMT/UTC+0
- `'America/New_York'` - EST
- `'Asia/Tokyo'` - JST
- See [pytz timezone list](https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3e5f8c40)

### Time Options

To change the time options, edit `bot.py`:
```python
TIME_OPTIONS = [7, 9, 11, 13, 15, 17, 19, 21, 23]  # Modify as needed
```

### Poll Duration

To change poll duration (default: 24 hours), edit `bot.py`:
```python
POLL_DURATION_HOURS = 24  # Change to desired hours
```

### Channel Names

The bot automatically finds channels with "votazioni" in the name (case-insensitive). If you want to target specific channels, you can modify the `find_votazioni_channels()` method in `bot.py`.

## API Keys / Tokens Required

### Discord Bot Token

**Required**: Yes  
**Where to get it**: [Discord Developer Portal](https://discord.com/developers/applications)

1. Create a new application
2. Go to "Bot" section
3. Copy the token
4. Add it to `.env` file as `DISCORD_BOT_TOKEN`

**Security Note**: 
- Never commit your `.env` file to version control
- Never share your bot token publicly
- If token is leaked, reset it immediately in Discord Developer Portal

## Troubleshooting

### Bot doesn't connect
- ✅ Check if bot token is correct in `.env`
- ✅ Verify bot is invited to the server
- ✅ Check internet connection

### Polls not posting
- ✅ Verify bot has "Send Messages" permission in votazioni channels
- ✅ Check if channels with "votazioni" in name exist
- ✅ Check console for error messages
- ✅ Verify bot is running at midnight GMT+1

### "Permission denied" errors
- ✅ Give bot "Send Messages" permission in channel settings
- ✅ Check channel permissions in Discord server settings
- ✅ Ensure bot role has necessary permissions

### Polls not using native Discord feature
- ✅ Ensure you're using `discord.py` version 2.3.0 or higher
- ✅ Update: `pip install --upgrade discord.py`
- ✅ Verify bot has proper intents enabled in Developer Portal

### Bot stops running
- ✅ Check console for error messages
- ✅ Ensure Python process isn't being killed
- ✅ For cloud deployment, check service logs
- ✅ Verify server/hosting is running 24/7

## File Structure

```
Discord_bot/
├── bot.py              # Main bot code
├── test_bot.py         # Test suite
├── requirements.txt    # Python dependencies
├── .env.example       # Example environment file
├── .env               # Your actual bot token (create this, don't commit)
└── README.md          # This file
```

## Support

If you encounter issues:
1. Check the console output for error messages
2. Run `python test_bot.py` to verify configuration
3. Ensure all dependencies are installed: `pip install -r requirements.txt`
4. Verify bot token is correct and bot has proper permissions

## License

This bot is provided as-is for your Discord server use.

---

**Note**: This bot requires `discord.py` 2.3.0 or higher for native poll support. If you encounter issues with polls, ensure you have the latest version installed.

