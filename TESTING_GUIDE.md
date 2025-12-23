# Testing Guide for Discord Daily Poll Bot

This guide explains how to test the bot before deploying it live to your Discord server.

## Prerequisites

1. ✅ Python 3.8+ installed
2. ✅ All dependencies installed: `pip install -r requirements.txt`
3. ✅ Bot token obtained from Discord Developer Portal
4. ✅ Bot invited to a test server (or your actual server)

## Step 1: Run Automated Tests

The bot includes a comprehensive test suite that verifies all core functionality without connecting to Discord.

```bash
python test_bot.py
```

**Expected Output:**
```
============================================================
Running Discord Bot Tests
============================================================

Timezone Calculation
Testing timezone calculation...
  [OK] Date format correct: DD/MM/YYYY
  [PASSED]

Time Options
Testing time options...
  [OK] Time options correct: [7, 9, 11, 13, 15, 17, 19, 21, 23]
  [PASSED]

Channel Finding
Testing channel finding logic...
  [OK] Found X votazioni channels
  [PASSED]

Poll Creation Logic
Testing poll creation logic...
  [OK] Poll data structure correct
  [PASSED]

Midnight Calculation
Testing midnight calculation...
  [OK] Next midnight calculated
  [PASSED]

Simulated Poll Creation
Testing simulated poll creation...
  [OK] Successfully simulated creating polls
  [PASSED]

============================================================
Test Results: 6 passed, 0 failed
============================================================
[SUCCESS] All tests passed!
```

If all tests pass, proceed to Step 2.

## Step 2: Test Bot Connection

1. **Create `.env` file** (if not already created):
   ```bash
   copy .env.example .env
   ```
   Then edit `.env` and add your bot token:
   ```
   DISCORD_BOT_TOKEN=your_actual_bot_token_here
   ```

2. **Run the bot**:
   ```bash
   python bot.py
   ```

3. **Expected Console Output:**
   ```
   [Bot Name] has logged in!
   Bot is ready to post daily polls at midnight (GMT+1)
   ⏰ Bot will post first poll in X.XX hours (at midnight GMT+1)
   ```

4. **Verify in Discord:**
   - Bot should appear online in your server
   - Bot should be visible in the member list
   - Check that bot has proper permissions

## Step 3: Test Poll Creation (Manual Trigger)

To test poll creation immediately without waiting for midnight, you can temporarily modify the bot code:

### Option A: Quick Test Script

Create a file `test_poll_creation.py`:

```python
import discord
import asyncio
import os
from dotenv import load_dotenv
from datetime import datetime
import pytz

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
TIMEZONE = pytz.timezone('Europe/Rome')
TIME_OPTIONS = [7, 9, 11, 13, 15, 17, 19, 21, 23]
POLL_DURATION_HOURS = 24

class TestBot(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has logged in!')
        
        # Find votazioni channels
        for guild in self.guilds:
            votazioni_channels = [ch for ch in guild.text_channels if 'votazioni' in ch.name.lower()]
            
            if not votazioni_channels:
                print(f"No votazioni channels found in {guild.name}")
                continue
            
            print(f"Found {len(votazioni_channels)} votazioni channel(s)")
            
            # Create poll in first channel for testing
            channel = votazioni_channels[0]
            await self.create_test_poll(channel)
            
        await self.close()
    
    async def create_test_poll(self, channel):
        now_italy = datetime.now(TIMEZONE)
        date_str = now_italy.strftime('%d/%m/%Y')
        question = date_str
        answers = [str(t) for t in TIME_OPTIONS]
        
        poll_payload = {
            "question": {"text": question},
            "answers": [{"poll_media": {"text": str(answer)}} for answer in answers],
            "duration": POLL_DURATION_HOURS * 3600,
            "allow_multiselect": True
        }
        
        try:
            http_client = channel._state.http
            if hasattr(http_client, 'create_poll'):
                await http_client.create_poll(channel.id, poll_payload)
            else:
                route = discord.http.Route('POST', '/channels/{channel_id}/polls', channel_id=channel.id)
                await http_client.request(route, json=poll_payload)
            print(f"✅ Test poll created in {channel.name}!")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    if not TOKEN:
        print("ERROR: DISCORD_BOT_TOKEN not found!")
        exit(1)
    bot = TestBot(intents=discord.Intents.default())
    bot.run(TOKEN)
```

Run it:
```bash
python test_poll_creation.py
```

### Option B: Modify bot.py Temporarily

Add this to `bot.py` in the `on_ready` method (remove after testing):

```python
async def on_ready(self):
    print(f'{self.user} has logged in!')
    print(f'Bot is ready to post daily polls at midnight (GMT+1)')
    
    # TEST MODE: Create poll immediately (REMOVE AFTER TESTING)
    await self.wait_until_ready()
    for guild in self.guilds:
        channels = self.find_votazioni_channels(guild)
        if channels:
            print(f"[TEST] Creating test poll in {channels[0].name}")
            await self.create_daily_poll(channels[0])
            break
    # END TEST MODE
    
    if not self.post_poll.is_running():
        self.post_poll.start()
```

## Step 4: Verify Poll in Discord

After creating a test poll, check in Discord:

1. **Poll Appearance:**
   - ✅ Poll should appear as a native Discord poll (not a regular message)
   - ✅ Title should be the current date (DD/MM/YYYY format)
   - ✅ Should show 9 time options: 7, 9, 11, 13, 15, 17, 19, 21, 23
   - ✅ Should allow multiple selections
   - ✅ Should show duration (24 hours)

2. **Poll Functionality:**
   - ✅ Click on options to vote
   - ✅ Should be able to select multiple options
   - ✅ Vote count should update
   - ✅ Poll should show "X votes" and time remaining

3. **Check Console:**
   - ✅ Should see "[SUCCESS] Poll created successfully" message
   - ✅ No error messages

## Step 5: Test Midnight Scheduling

To verify the bot will post at midnight:

1. **Check Next Poll Time:**
   - When bot starts, it shows: "Bot will post first poll in X.XX hours (at midnight GMT+1)"
   - Verify this time is correct for your timezone

2. **Test Time Calculation:**
   - Current time in Italy (GMT+1): Check online
   - Bot should calculate next midnight correctly
   - Example: If it's 3:00 PM (15:00) GMT+1, next poll should be in ~9 hours

3. **Wait for Midnight (Optional):**
   - Keep bot running until midnight GMT+1
   - Verify poll is posted automatically
   - Check all votazioni channels receive polls

## Step 6: Test Multiple Channels

Verify the bot finds and posts to ALL votazioni channels:

1. **Create Test Channels:**
   - Create channels with "votazioni" in the name:
     - `votazioni-test-1`
     - `votazioni-test-2`
     - `votazioni-test-3`

2. **Run Bot:**
   - Bot should detect all 3 channels
   - Console should show: "Posting polls in 3 channel(s)"

3. **Verify:**
   - All channels should receive polls
   - Each poll should have the same date and options

## Troubleshooting Tests

### Test Suite Fails
- ✅ Ensure Python 3.8+ is installed
- ✅ Install dependencies: `pip install -r requirements.txt`
- ✅ Check Python version: `python --version`

### Bot Doesn't Connect
- ✅ Verify `.env` file exists and has correct token
- ✅ Check token format (no extra spaces)
- ✅ Verify bot is invited to server
- ✅ Check internet connection

### Poll Creation Fails
- ✅ Verify bot has "Send Messages" permission
- ✅ Check bot has proper intents enabled in Developer Portal
- ✅ Ensure discord.py version 2.3.0+: `pip install --upgrade discord.py`
- ✅ Check console for specific error messages

### Polls Don't Appear as Native Polls
- ✅ Update discord.py: `pip install --upgrade discord.py`
- ✅ Verify Discord server supports polls (Discord API v10+)
- ✅ Check bot permissions include "Send Messages"
- ✅ Try creating a poll manually in Discord to verify feature works

### Wrong Timezone
- ✅ Verify timezone in `bot.py`: `TIMEZONE = pytz.timezone('Europe/Rome')`
- ✅ Check current time calculation in console output
- ✅ Adjust timezone if needed (see README.md)

## Pre-Deployment Checklist

Before deploying the bot live:

- [ ] All automated tests pass (`python test_bot.py`)
- [ ] Bot connects successfully to Discord
- [ ] Test poll created successfully (manual test)
- [ ] Poll appears as native Discord poll
- [ ] All time options (7, 9, 11, 13, 15, 17, 19, 21, 23) are present
- [ ] Poll allows multiple selections
- [ ] Poll duration is 24 hours
- [ ] Bot finds all votazioni channels correctly
- [ ] Midnight calculation is correct
- [ ] Bot has proper permissions in all votazioni channels
- [ ] `.env` file is secure (not committed to git)
- [ ] Bot token is kept secret

## Next Steps

Once all tests pass:

1. **Deploy the bot** (see README.md for deployment options)
2. **Monitor first midnight** to ensure polls post correctly
3. **Check all votazioni channels** receive polls
4. **Verify polls are working** for users

---

**Note**: Remove any test code modifications before deploying to production!

