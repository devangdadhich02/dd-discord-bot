import discord
from discord.ext import tasks
import asyncio
from datetime import datetime, time, timedelta
import pytz
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot configuration
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
TIMEZONE = pytz.timezone('Europe/Rome')  # GMT+1 (Italy)
TIME_OPTIONS = [7, 9, 11, 13, 15, 17, 19, 21, 23]
POLL_DURATION_HOURS = 24

class DailyPollBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True
        super().__init__(intents=intents)
        # Don't start task here - will start in on_ready() when event loop is running

    async def on_ready(self):
        """Called when bot successfully connects to Discord"""
        print(f'\n{"="*60}')
        print(f'✅ Bot logged in: {self.user}')
        print(f'✅ Bot ID: {self.user.id}')
        print(f'{"="*60}')
        
        # Show connected servers
        print(f'\n📋 Connected to {len(self.guilds)} server(s):')
        for guild in self.guilds:
            votazioni_channels = self.find_votazioni_channels(guild)
            print(f'   - {guild.name}: {len(votazioni_channels)} votazioni channel(s) found')
        
        print(f'\n🤖 Bot Task: Create daily surveys at midnight (GMT+1, Italy timezone)')
        print(f'   - Survey title: Current date (DD/MM/YYYY)')
        print(f'   - Time options: {TIME_OPTIONS}')
        print(f'   - Multi-select: Enabled')
        print(f'   - Duration: {POLL_DURATION_HOURS} hours')
        print(f'   - Uses: Discord native survey/poll feature')
        print(f'\n{"="*60}\n')
        
        # Ensure the task is running
        if not self.post_poll.is_running():
            self.post_poll.start()

    def find_votazioni_channels(self, guild):
        """
        Find all channels with 'votazioni' in their name.
        The bot will post the same survey to all these different chat channels.
        """
        votazioni_channels = []
        for channel in guild.text_channels:
            # Case-insensitive search for 'votazioni' in channel name
            if 'votazioni' in channel.name.lower():
                votazioni_channels.append(channel)
        return votazioni_channels

    async def create_daily_poll(self, channel):
        """
        Create a daily poll in the specified channel using Discord's native poll feature.
        This replaces manual work by automating the survey creation process.
        """
        # Get current date in Italy timezone (GMT+1)
        now_italy = datetime.now(TIMEZONE)
        date_str = now_italy.strftime('%d/%m/%Y')
        
        # Survey title = current date (as per client requirement)
        question = date_str
        
        # Create time options as strings (clock times: 7, 9, 11, 13, 15, 17, 19, 21, 23)
        answers = [str(time_option) for time_option in TIME_OPTIONS]
        
        # Create the poll using Discord's native poll/survey feature
        try:
            # Prepare poll payload according to Discord API v10
            # This uses Discord's built-in survey function
            poll_payload = {
                "question": {
                    "text": question  # Survey title = current date
                },
                "answers": [{"poll_media": {"text": str(answer)}} for answer in answers],  # Multiple clock time options
                "duration": POLL_DURATION_HOURS * 3600,  # Duration in seconds (24 hours)
                "allow_multiselect": True  # Users can check multiple answers
            }
            
            # Use Discord's HTTP API to create poll (native survey feature)
            http_client = channel._state.http
            
            # Method 1: Try using discord.py's built-in method if available (v2.3+)
            if hasattr(http_client, 'create_poll'):
                try:
                    await http_client.create_poll(channel.id, poll_payload)
                    print(f"[SUCCESS] Survey created in #{channel.name} - Date: {date_str}")
                    return True
                except Exception as e:
                    print(f"[WARNING] create_poll method failed, trying direct API: {e}")
            
            # Method 2: Use Discord API endpoint directly (most reliable)
            # POST /channels/{channel.id}/polls
            route = discord.http.Route('POST', '/channels/{channel_id}/polls', channel_id=channel.id)
            await http_client.request(route, json=poll_payload)
            print(f"[SUCCESS] Survey created in #{channel.name} - Date: {date_str}")
            return True
                
        except discord.errors.Forbidden:
            print(f"[ERROR] Permission denied in #{channel.name} - Bot needs 'Send Messages' permission")
            return False
        except discord.errors.HTTPException as http_error:
            error_msg = str(http_error)
            print(f"[ERROR] HTTP error creating survey in #{channel.name}: {error_msg}")
            
            # Provide specific error messages
            if http_error.status == 400:
                print(f"   [INFO] This might indicate:")
                print(f"   - Discord API version issue (need API v10+)")
                print(f"   - Poll format issue")
                print(f"   - Server doesn't support polls yet")
            elif http_error.status == 403:
                print(f"   [INFO] Bot lacks permissions. Ensure bot has:")
                print(f"   - Send Messages permission")
                print(f"   - Proper channel access")
            elif http_error.status == 404:
                print(f"   [INFO] Channel not found or bot not in server")
            return False
        except Exception as e:
            print(f"[ERROR] Unexpected error creating survey in #{channel.name}: {str(e)}")
            import traceback
            traceback.print_exc()
            return False

    @tasks.loop(time=time(0, 0))  # Midnight (00:00)
    async def post_poll(self):
        """
        Post surveys daily at midnight (GMT+1, Italy timezone).
        This automates the daily survey creation task.
        """
        # Wait until we're connected
        await self.wait_until_ready()
        
        # Get current time in Italy timezone (GMT+1)
        now_italy = datetime.now(TIMEZONE)
        print(f"\n{'='*60}")
        print(f"🕛 Daily Survey Task - {now_italy.strftime('%Y-%m-%d %H:%M:%S %Z')}")
        print(f"{'='*60}")
        
        # Post surveys to all guilds (servers) the bot is in
        total_polls_created = 0
        total_polls_failed = 0
        
        for guild in self.guilds:
            # Find all channels with 'votazioni' in their name
            votazioni_channels = self.find_votazioni_channels(guild)
            
            if not votazioni_channels:
                print(f"[INFO] No 'votazioni' channels found in server: {guild.name}")
                continue
            
            print(f"[INFO] Found {len(votazioni_channels)} channel(s) in {guild.name}")
            print(f"[INFO] Creating surveys in {len(votazioni_channels)} different chat channels...")
            
            # Create the same survey in all different chat channels
            for channel in votazioni_channels:
                success = await self.create_daily_poll(channel)
                if success:
                    total_polls_created += 1
                else:
                    total_polls_failed += 1
                
                # Small delay between posts to avoid rate limiting
                await asyncio.sleep(1)
        
        # Summary
        print(f"\n{'='*60}")
        print(f"📊 Daily Survey Summary:")
        print(f"   ✅ Successfully created: {total_polls_created} survey(s)")
        if total_polls_failed > 0:
            print(f"   ❌ Failed: {total_polls_failed} survey(s)")
        print(f"{'='*60}\n")

    @post_poll.before_loop
    async def before_post_poll(self):
        """Wait until midnight GMT+1 before starting the loop"""
        await self.wait_until_ready()
        
        # Calculate next midnight in Italy timezone
        now_italy = datetime.now(TIMEZONE)
        midnight_italy = now_italy.replace(hour=0, minute=0, second=0, microsecond=0)
        
        # If it's already past midnight today, schedule for tomorrow
        if now_italy >= midnight_italy:
            midnight_italy += timedelta(days=1)
        
        # Calculate seconds until next midnight
        wait_seconds = (midnight_italy - now_italy).total_seconds()
        
        print(f"⏰ Bot will post first poll in {wait_seconds/3600:.2f} hours (at midnight GMT+1)")
        await asyncio.sleep(wait_seconds)

# Run the bot
if __name__ == "__main__":
    if not TOKEN:
        print("\n" + "="*60)
        print("❌ ERROR: DISCORD_BOT_TOKEN not found!")
        print("="*60)
        print("\nPlease check:")
        print("1. .env file exists in the project folder")
        print("2. .env file contains: DISCORD_BOT_TOKEN=your_actual_token")
        print("3. Token is correct (no extra spaces)")
        print("\nSteps to fix:")
        print("1. Open .env file")
        print("2. Replace 'your_bot_token_here' with your actual bot token")
        print("3. Save the file")
        print("4. Run again: python bot.py")
        print("\n" + "="*60 + "\n")
        exit(1)
    
    # Check if token is still placeholder
    if TOKEN == "your_bot_token_here" or len(TOKEN) < 20:
        print("\n" + "="*60)
        print("❌ ERROR: Invalid Bot Token!")
        print("="*60)
        print("\nYour token appears to be invalid or still a placeholder.")
        print("\nPlease:")
        print("1. Go to: https://discord.com/developers/applications")
        print("2. Select your application")
        print("3. Go to 'Bot' section")
        print("4. Click 'Reset Token' or 'Copy' to get your token")
        print("5. Update .env file with the correct token")
        print("\nToken should look like: MTIzNDU2Nzg5MDEyMzQ1Njc4OQ.ABCDEF.xyz123...")
        print("(Long string with dots)")
        print("\n" + "="*60 + "\n")
        exit(1)
    
    try:
        bot = DailyPollBot()
        bot.run(TOKEN)
    except discord.errors.LoginFailure as e:
        print("\n" + "="*60)
        print("❌ ERROR: Bot Login Failed!")
        print("="*60)
        print(f"\nError: {str(e)}")
        print("\nPossible reasons:")
        print("1. Bot token is incorrect or expired")
        print("2. Token has extra spaces (check .env file)")
        print("3. Token was reset in Discord Developer Portal")
        print("\nSolution:")
        print("1. Go to: https://discord.com/developers/applications")
        print("2. Select your application → Bot section")
        print("3. Click 'Reset Token' to get a new token")
        print("4. Copy the new token")
        print("5. Update .env file: DISCORD_BOT_TOKEN=new_token_here")
        print("6. Make sure there are NO spaces around the = sign")
        print("7. Save and run again")
        print("\n" + "="*60 + "\n")
        exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        import traceback
        traceback.print_exc()
        exit(1)

