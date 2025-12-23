# Local Setup Guide (हिंदी/English)

यह guide आपको bot को local पर run करने में मदद करेगी।

## 🚀 Quick Local Setup

### Step 1: Dependencies Install करें

```bash
pip install -r requirements.txt
```

या Python 3 के साथ:
```bash
python -m pip install -r requirements.txt
```

### Step 2: Bot Token Setup करें

1. **`.env` file बनाएं:**
   ```bash
   copy env_example.txt .env
   ```
   (Linux/Mac: `cp env_example.txt .env`)

2. **`.env` file खोलें और अपना bot token add करें:**
   ```
   DISCORD_BOT_TOKEN=your_actual_bot_token_here
   ```

3. **Bot Token कहाँ से मिलेगा:**
   - https://discord.com/developers/applications पर जाएं
   - New Application बनाएं
   - Bot section में जाएं
   - Token copy करें

### Step 3: Bot को Local पर Run करें

**Option A: Simple Script (Recommended)**
```bash
python run_local.py
```

यह script automatically check करेगी:
- ✅ .env file exists है या नहीं
- ✅ Bot token set है या नहीं
- ✅ सभी dependencies installed हैं या नहीं

**Option B: Direct Run**
```bash
python bot.py
```

## 📋 Local Testing Checklist

### Before Running:

- [ ] Python 3.8+ installed है
- [ ] `pip install -r requirements.txt` run किया है
- [ ] `.env` file बनाई है
- [ ] Bot token `.env` में add किया है
- [ ] Bot को Discord server में invite किया है
- [ ] Bot को proper permissions दी हैं (Send Messages)

### While Running:

1. **Console Output Check करें:**
   ```
   [Bot Name] has logged in!
   Bot is ready to post daily polls at midnight (GMT+1)
   ⏰ Bot will post first poll in X.XX hours (at midnight GMT+1)
   ```

2. **Discord में Check करें:**
   - Bot online दिखना चाहिए
   - Bot server member list में दिखना चाहिए

3. **Test Poll Create करें (Optional):**
   - `TESTING_GUIDE.md` देखें manual testing के लिए

## 🧪 Tests Run करें

Bot को run करने से पहले tests run करें:

```bash
python test_bot.py
```

सभी tests pass होने चाहिए।

## ⚠️ Common Issues (Local)

### Issue: "DISCORD_BOT_TOKEN not found"
**Solution:**
- `.env` file बनाएं
- Token add करें
- File name exactly `.env` होना चाहिए (not `.env.txt`)

### Issue: "ModuleNotFoundError"
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: Bot connect नहीं हो रहा
**Solution:**
- Token सही है या नहीं check करें
- Bot server में invite किया है या नहीं
- Internet connection check करें

### Issue: "Permission denied"
**Solution:**
- Bot को "Send Messages" permission दें
- Channel permissions check करें

## 🎯 Local vs Live

### Local Running:
- ✅ Testing के लिए perfect
- ✅ Development के लिए use करें
- ⚠️ Computer बंद होने पर bot stop हो जाएगा

### Live Deployment:
- ✅ 24/7 running के लिए
- ✅ Cloud server पर deploy करें
- ✅ README.md में deployment options देखें

## 📝 Next Steps

1. **Local पर test करें** - `python run_local.py`
2. **Tests run करें** - `python test_bot.py`
3. **Test poll create करें** - `TESTING_GUIDE.md` देखें
4. **Live deploy करें** - `README.md` में deployment section देखें

## 🔧 Configuration (Local)

Bot settings `bot.py` में हैं:

```python
TIMEZONE = pytz.timezone('Europe/Rome')  # GMT+1 (Italy)
TIME_OPTIONS = [7, 9, 11, 13, 15, 17, 19, 21, 23]
POLL_DURATION_HOURS = 24
```

अगर आप timezone या options change करना चाहते हैं, `bot.py` edit करें।

---

**Need Help?** 
- `README.md` - Complete documentation
- `TESTING_GUIDE.md` - Testing instructions
- `QUICK_START.md` - Quick setup

**Bot ready hai local run करने के लिए!** 🚀

