"""
Local Testing Script - Run this to test the bot locally
This script helps you test the bot before deploying it live
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def check_setup():
    """Check if everything is set up correctly"""
    print("=" * 60)
    print("Checking Bot Setup...")
    print("=" * 60)
    print()
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("[WARNING] .env file not found!")
        print("Creating .env file from env_example.txt...")
        if os.path.exists('env_example.txt'):
            with open('env_example.txt', 'r') as f:
                content = f.read()
            with open('.env', 'w') as f:
                f.write(content)
            print("[OK] .env file created. Please add your bot token!")
        else:
            print("[ERROR] env_example.txt not found!")
        return False
    
    # Check if token is set
    token = os.getenv('DISCORD_BOT_TOKEN')
    if not token or token == 'your_bot_token_here':
        print("[ERROR] DISCORD_BOT_TOKEN not set in .env file!")
        print()
        print("Please:")
        print("1. Open .env file")
        print("2. Replace 'your_bot_token_here' with your actual bot token")
        print("3. Get token from: https://discord.com/developers/applications")
        return False
    
    print("[OK] Bot token found in .env")
    
    # Check dependencies
    print()
    print("Checking dependencies...")
    try:
        import discord
        print(f"[OK] discord.py version: {discord.__version__}")
        if discord.__version__ < "2.3.0":
            print("[WARNING] discord.py version is too old. Please update:")
            print("  pip install --upgrade discord.py")
    except ImportError:
        print("[ERROR] discord.py not installed!")
        print("Run: pip install -r requirements.txt")
        return False
    
    try:
        import pytz
        print("[OK] pytz installed")
    except ImportError:
        print("[ERROR] pytz not installed!")
        print("Run: pip install -r requirements.txt")
        return False
    
    try:
        from dotenv import load_dotenv
        print("[OK] python-dotenv installed")
    except ImportError:
        print("[ERROR] python-dotenv not installed!")
        print("Run: pip install -r requirements.txt")
        return False
    
    print()
    print("=" * 60)
    print("[SUCCESS] Setup looks good!")
    print("=" * 60)
    print()
    return True

def main():
    """Main function"""
    if not check_setup():
        print()
        print("Please fix the issues above and try again.")
        sys.exit(1)
    
    print("Starting bot...")
    print("Press Ctrl+C to stop the bot")
    print()
    print("-" * 60)
    print()
    
    # Import and run the bot
    try:
        from bot import DailyPollBot, TOKEN
        
        if not TOKEN:
            print("[ERROR] Bot token not found!")
            sys.exit(1)
        
        bot = DailyPollBot()
        bot.run(TOKEN)
    except KeyboardInterrupt:
        print()
        print()
        print("[INFO] Bot stopped by user")
    except Exception as e:
        print(f"[ERROR] Error running bot: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()

