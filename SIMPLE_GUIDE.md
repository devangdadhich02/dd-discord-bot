# सबसे Simple Guide (Easiest Way)

अगर आपको कुछ समझ नहीं आ रहा, यह सबसे आसान guide है:

## 🎯 3 Simple Steps

### Step 1: Bot Token लें (5 min)
1. https://discord.com/developers/applications पर जाएं
2. "New Application" → Name दें → Create
3. "Bot" section → "Add Bot" → Confirm
4. "Token" copy करें (यही जरूरी है!)
5. "Message Content Intent" enable करें → Save

### Step 2: Bot को Server में Add करें (2 min)
1. "OAuth2" → "URL Generator"
2. "bot" tick करें
3. "Send Messages" permission tick करें
4. URL copy करें → Browser में open करें
5. Server select करें → Authorize

### Step 3: Bot Run करें (2 min)
1. `.env` file बनाएं (env_example.txt को copy करके)
2. `.env` में अपना token paste करें:
   ```
   DISCORD_BOT_TOKEN=आपका_टोकन_यहाँ
   ```
3. Dependencies install करें:
   ```bash
   pip install -r requirements.txt
   ```
4. Bot run करें:
   ```bash
   python bot.py
   ```

**बस! Bot ready है!** ✅

## 📝 Files क्या करते हैं?

- `bot.py` - Main bot code (इसे run करना है)
- `requirements.txt` - Dependencies list
- `.env` - आपका bot token (यहाँ add करना है)
- `README.md` - Complete documentation
- `NEXT_STEPS.md` - Detailed steps

## 🚀 Quick Commands

```bash
# Dependencies install
pip install -r requirements.txt

# Tests run करें
python test_bot.py

# Bot run करें
python bot.py
```

## ❓ अगर Problem आए

1. **Token नहीं मिल रहा?**
   - Discord Developer Portal → Bot → Token → Copy

2. **Bot connect नहीं हो रहा?**
   - `.env` file check करें
   - Token सही paste किया है या नहीं

3. **Error आ रहा है?**
   - Console में error message देखें
   - `README.md` में Troubleshooting देखें

## ✅ Success Signs

जब सब ठीक होगा:
- Console में दिखेगा: "Bot logged in"
- Discord में bot online दिखेगा
- Console में दिखेगा: "Bot will post first poll in X hours"

**बस इतना ही! Simple है!** 😊

