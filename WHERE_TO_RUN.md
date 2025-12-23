# Project कहाँ Run करें? (Where to Run the Bot)

यह guide बताएगी कि bot को कहाँ और कैसे run करना है।

## 🎯 दो Options हैं:

### Option 1: Local Computer पर (Testing के लिए) ✅
**कब use करें:**
- Testing करने के लिए
- Development के लिए
- Quick check करने के लिए

**कैसे Run करें:**
```bash
# Simple way:
python run_local.py

# या directly:
python bot.py
```

**⚠️ Limitation:**
- Computer बंद होने पर bot stop हो जाएगा
- 24/7 run नहीं होगा (जब तक computer हमेशा on न रखें)

---

### Option 2: Cloud Server पर (24/7 Live के लिए) ✅✅✅
**कब use करें:**
- Production/Live use के लिए
- 24/7 automatic running के लिए
- Client के server पर deploy करने के लिए

**कहाँ Deploy करें:**

#### A. Heroku (Free tier available) - सबसे आसान
```bash
# 1. Heroku account बनाएं: https://heroku.com
# 2. Heroku CLI install करें
# 3. Login करें:
heroku login

# 4. Project folder में:
heroku create your-bot-name

# 5. Token set करें:
heroku config:set DISCORD_BOT_TOKEN=your_token_here

# 6. Deploy करें:
git init
git add .
git commit -m "Initial commit"
git push heroku main
```

#### B. DigitalOcean / AWS / Azure (Paid, लेकिन reliable)
- Virtual server बनाएं
- Python install करें
- Bot files upload करें
- Run करें: `python bot.py` (background में)

#### C. Raspberry Pi / Home Server (अगर आपके पास है)
- Raspberry Pi पर Python install करें
- Bot files copy करें
- Run करें: `python bot.py`

#### D. Replit / Glitch (Online IDE)
- Replit.com पर account बनाएं
- New Python project बनाएं
- Bot files upload करें
- Environment variable में token add करें
- Run करें (24/7 के लिए paid plan चाहिए)

---

## 🚀 Recommended: Heroku (सबसे आसान)

### Heroku Setup (Step-by-Step):

1. **Account बनाएं:**
   - https://heroku.com पर जाएं
   - Free account बनाएं

2. **Heroku CLI Install करें:**
   - https://devcenter.heroku.com/articles/heroku-cli
   - Download और install करें

3. **Project में `Procfile` बनाएं:**
   ```
   worker: python bot.py
   ```

4. **Heroku में Deploy करें:**
   ```bash
   # Login
   heroku login
   
   # Create app
   heroku create your-bot-name
   
   # Set token
   heroku config:set DISCORD_BOT_TOKEN=your_actual_token
   
   # Deploy
   git init
   git add .
   git commit -m "Deploy bot"
   git push heroku main
   ```

5. **Bot 24/7 run होगा!** ✅

---

## 📋 Quick Comparison:

| Option | Cost | Difficulty | 24/7? | Best For |
|--------|------|------------|-------|----------|
| **Local Computer** | Free | Easy | ❌ No | Testing |
| **Heroku** | Free/Paid | Easy | ✅ Yes | Production |
| **DigitalOcean** | Paid | Medium | ✅ Yes | Production |
| **AWS** | Paid | Hard | ✅ Yes | Enterprise |
| **Raspberry Pi** | One-time | Medium | ✅ Yes | Home use |

---

## 🎯 आपके लिए Recommendation:

### Testing के लिए:
```bash
# Local computer पर:
python bot.py
```

### Live/Production के लिए:
**Heroku use करें** (सबसे आसान और free tier available)

---

## 📝 Step-by-Step: Local पर Run करें (अभी के लिए)

1. **Terminal/Command Prompt खोलें:**
   - Windows: PowerShell या CMD
   - Project folder में navigate करें:
     ```bash
     cd "C:\Users\Devang Dadhich\OneDrive\Desktop\Discord_bot"
     ```

2. **Dependencies Install करें (अगर नहीं किया):**
   ```bash
   pip install -r requirements.txt
   ```

3. **`.env` file check करें:**
   - `.env` file में token add किया है या नहीं check करें

4. **Bot Run करें:**
   ```bash
   python bot.py
   ```

5. **Check करें:**
   - Console में "Bot logged in" दिखना चाहिए
   - Discord में bot online दिखना चाहिए

---

## 🚀 Step-by-Step: Heroku पर Deploy करें (24/7 के लिए)

### Prerequisites:
- Heroku account
- Heroku CLI installed
- Git installed

### Steps:

1. **`Procfile` बनाएं** (project folder में):
   ```
   worker: python bot.py
   ```

2. **Heroku Login:**
   ```bash
   heroku login
   ```

3. **App Create करें:**
   ```bash
   heroku create your-bot-name
   ```

4. **Token Set करें:**
   ```bash
   heroku config:set DISCORD_BOT_TOKEN=your_actual_token_here
   ```

5. **Deploy करें:**
   ```bash
   git init
   git add .
   git commit -m "Deploy bot"
   git push heroku main
   ```

6. **Check करें:**
   ```bash
   heroku logs --tail
   ```

---

## ❓ FAQ

### Q: Local पर run कर सकते हैं 24/7 के लिए?
**A:** हाँ, लेकिन computer हमेशा on रखना होगा। Cloud server better है।

### Q: Heroku free है?
**A:** हाँ, free tier available है। लेकिन 24/7 के लिए paid plan better है।

### Q: कौन सा option सबसे अच्छा है?
**A:** 
- **Testing**: Local computer
- **Production**: Heroku (easy) या DigitalOcean (reliable)

### Q: Bot कहाँ run होगा?
**A:** 
- Local: आपके computer पर
- Heroku: Heroku के servers पर (cloud)
- DigitalOcean: आपके virtual server पर

---

## ✅ Summary

**अभी के लिए (Testing):**
```bash
cd "C:\Users\Devang Dadhich\OneDrive\Desktop\Discord_bot"
python bot.py
```

**Live के लिए (24/7):**
- Heroku पर deploy करें (सबसे आसान)
- या किसी cloud server पर deploy करें

**Bot ready है - बस run करना है!** 🚀

