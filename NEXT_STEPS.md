# अब क्या करना है? (Next Steps Guide)

यह guide आपको step-by-step बताएगी कि bot को कैसे setup और run करना है।

## 📋 Step-by-Step Process

### Step 1: Discord Bot Token लें (5 minutes)

1. **Discord Developer Portal खोलें:**
   - Browser में जाएं: https://discord.com/developers/applications
   - Login करें अपने Discord account से

2. **New Application बनाएं:**
   - "New Application" button click करें
   - Name दें (जैसे: "Daily Poll Bot")
   - "Create" click करें

3. **Bot बनाएं:**
   - Left sidebar में "Bot" section click करें
   - "Add Bot" button click करें
   - "Yes, do it!" confirm करें

4. **Token Copy करें:**
   - "Token" section में "Reset Token" या "Copy" click करें
   - ⚠️ **IMPORTANT**: Token को कहीं safe जगह save कर लें (क्योंकि दोबारा नहीं दिखेगा)

5. **Permissions Enable करें:**
   - Scroll down करें "Privileged Gateway Intents" section में
   - ✅ "Message Content Intent" enable करें (जरूरी है!)
   - "Save Changes" click करें

### Step 2: Bot को Server में Invite करें (2 minutes)

1. **OAuth2 URL Generator:**
   - Left sidebar में "OAuth2" → "URL Generator" click करें

2. **Scopes Select करें:**
   - ✅ "bot" checkbox tick करें

3. **Bot Permissions Select करें:**
   - ✅ "Send Messages" (जरूरी!)
   - ✅ "Read Message History" (optional)
   - ✅ "View Channels" (optional)

4. **Invite Link Copy करें:**
   - नीचे generated URL copy करें
   - Browser में paste करें और Enter press करें
   - अपने Discord server select करें
   - "Authorize" click करें
   - ✅ Bot आपके server में add हो गया!

### Step 3: Bot Token Setup करें (2 minutes)

1. **`.env` file बनाएं:**
   ```bash
   # Windows PowerShell में:
   copy env_example.txt .env
   
   # या manually:
   # env_example.txt को copy करके .env नाम से save करें
   ```

2. **`.env` file खोलें:**
   - Notepad या किसी text editor में खोलें
   - Line 4 पर जाएं जहाँ लिखा है: `DISCORD_BOT_TOKEN=your_bot_token_here`
   - `your_bot_token_here` को अपने actual token से replace करें
   
   **Example:**
   ```
   DISCORD_BOT_TOKEN=YOUR_ACTUAL_TOKEN_HERE
   ```
   (Replace YOUR_ACTUAL_TOKEN_HERE with your actual bot token from Discord Developer Portal)

3. **File Save करें:**
   - File को save करें
   - ⚠️ File name exactly `.env` होना चाहिए (`.env.txt` नहीं!)

### Step 4: Dependencies Install करें (1 minute)

```bash
# PowerShell या Command Prompt में:
pip install -r requirements.txt
```

यह command install करेगी:
- discord.py (Discord bot library)
- python-dotenv (environment variables के लिए)
- pytz (timezone के लिए)

### Step 5: Bot Test करें (2 minutes)

1. **Automated Tests Run करें:**
   ```bash
   python test_bot.py
   ```
   
   ✅ सभी tests pass होने चाहिए

2. **Bot Run करें (Local Testing):**
   ```bash
   python run_local.py
   ```
   
   या directly:
   ```bash
   python bot.py
   ```

3. **Check करें:**
   - Console में दिखना चाहिए: "Bot logged in: [Bot Name]"
   - Discord में bot online दिखना चाहिए
   - Console में दिखेगा: "Bot will post first poll in X.XX hours"

### Step 6: Bot को Live Deploy करें (24/7 के लिए)

**Option A: Local Computer (अगर 24/7 on रख सकते हैं)**
- Bot को run करें: `python bot.py`
- Computer को हमेशा on रखें
- ⚠️ Computer बंद होने पर bot stop हो जाएगा

**Option B: Cloud Server (Recommended - 24/7)**
- Heroku, DigitalOcean, AWS, या किसी cloud service पर deploy करें
- `README.md` में "Deployment" section देखें
- Bot 24/7 run करेगा automatically

## 🎯 Quick Checklist

Setup complete है जब:
- [ ] Discord bot token मिल गया
- [ ] Bot server में invite हो गया
- [ ] `.env` file में token add हो गया
- [ ] `pip install -r requirements.txt` run हो गया
- [ ] `python test_bot.py` - सभी tests pass
- [ ] `python bot.py` - bot connect हो गया
- [ ] Discord में bot online दिख रहा है

## ❓ Common Issues & Solutions

### Issue: "DISCORD_BOT_TOKEN not found"
**Solution:**
- `.env` file बनाई है या नहीं check करें
- Token सही add किया है या नहीं check करें
- File name exactly `.env` है (`.env.txt` नहीं)

### Issue: "ModuleNotFoundError"
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: Bot connect नहीं हो रहा
**Solution:**
- Token सही है या नहीं verify करें
- Bot server में invite किया है या नहीं check करें
- Internet connection check करें

### Issue: "Permission denied"
**Solution:**
- Bot को "Send Messages" permission दें
- Channel permissions check करें

## 📞 Need Help?

अगर कोई problem आए:
1. Console में error message देखें
2. `README.md` में "Troubleshooting" section देखें
3. `TESTING_GUIDE.md` देखें

## 🎉 Success!

जब सब कुछ setup हो जाए:
- ✅ Bot daily midnight (00:00 GMT+1) पर automatically survey post करेगा
- ✅ Survey title current date होगा
- ✅ सभी "votazioni" channels में same survey post होगा
- ✅ Users multiple time options select कर सकेंगे
- ✅ Fully automated - कोई manual work नहीं!

---

**अब Step 1 से शुरू करें और step-by-step follow करें!** 🚀

