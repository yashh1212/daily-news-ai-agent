# 🗞️ AI News Agent

A Python-based AI bot that fetches the latest news, summarizes it using Gemini, converts the summary to English voice, and sends it via **Telegram** (voice + text) and **Email**.

## 🚀 Features

- 📰 Fetches top news headlines
- 🤖 Summarizes using Google Gemini AI
- 🔊 Converts summary to natural English voice using `gTTS`
- 📤 Sends summary + voice as a **Telegram message**
- 📧 Sends daily email updates
- ⏱️ Runs automatically on a schedule (e.g. every 10 sec or daily at 8 AM)

## 📁 Project Structure

```
ai-news-agent/
├── ai_news_agent.py        # All logic in one file
├── .env                    # Private API & email credentials
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files and folders
└── README.md               # This file
```

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-news-agent.git
cd ai-news-agent
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

> Or install manually:
```bash
pip install requests gTTS schedule python-dotenv
```

### 3. Add `.env` File

```env
SMTP_USER=your_email@gmail.com
SMTP_PASS=your_app_password
```

## 🔐 Required API Keys

- ✅ **Gemini API Key**: [Get it from Google AI Studio](https://makersuite.google.com/app/apikey)
- ✅ **Telegram Bot Token**: From [@BotFather](https://t.me/BotFather)
- ✅ **News API Key**: From [https://newsapi.org](https://newsapi.org)

Update these keys inside `ai_news_agent.py` or load from `.env`.

## ✅ Run the Bot

```bash
python ai_news_agent.py
```

It will run daily at **8:00 AM** based on your system time.

## ☁️ Deployment Options

| Platform         | Notes                            |
|------------------|----------------------------------|
| 🔹 Render         | Best for background worker bots  |
| 🔹 PythonAnywhere | Great for beginners & scheduling |
| 🔹 Replit         | Easy web-based testing           |

## 🙋 Author

**Yash Dhokane**  
📧 yashdhokane12@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/yashdhokane)

## 📜 License

MIT License.