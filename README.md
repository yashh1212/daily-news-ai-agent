# 🗞️ AI News Agent

A Python-based AI bot that fetches the latest news, summarizes it using Gemini, converts the summary to English voice, and sends it via **Telegram** (voice + text) and **Email**.

---

## 🚀 Features

- 📰 Fetches top news headlines
- 🤖 Summarizes using Google Gemini AI (Gemini 1.5/2.0)
- 🔊 Converts summary to natural English voice using `gTTS`
- 📤 Sends summary + voice as a **Telegram message**
- 📧 Sends daily email updates
- ⏱️ Runs automatically on a schedule (e.g. every 10 sec or daily)

---

## 📁 Project Structure

ai-news-agent/
├── ai_news_agent.py # All logic in one file
├── .env # Private API & email credentials
├── requirements.txt # Python dependencies
├── .gitignore # Ignored files and folders
└── README.md # This file

yaml
Copy
Edit

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-news-agent.git
cd ai-news-agent
2. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
Or install manually:

bash
Copy
Edit
pip install requests gTTS schedule python-dotenv
3. Add .env File
Create a .env file in the root folder with your email credentials:

env
Copy
Edit
SMTP_USER=your_email@gmail.com
SMTP_PASS=your_app_password
🔐 API Keys Required
✅ Gemini API Key: Get it from Google AI Studio

✅ Telegram Bot Token: Get it from @BotFather

✅ News API Key: From https://newsapi.org

Replace your keys in ai_news_agent.py.

✅ Running the Bot
Run once (test):
bash
Copy
Edit
python ai_news_agent.py
Run every 10 seconds:
python
Copy
Edit
schedule.every(10).seconds.do(job)
Run daily at 8 AM:
python
Copy
Edit
schedule.every().day.at("08:00").do(job)
☁️ Deployment Options
Platform	Notes
🔹 Render	Best for background worker bots
🔹 PythonAnywhere	Great for beginners & scheduling
🔹 Replit	Easy web-based testing
🔹 GitHub Actions	Scheduled daily workflows

🙋 Author
Yash Dhokane
📧 yashdhokane12@gmail.com
🔗 LinkedIn

