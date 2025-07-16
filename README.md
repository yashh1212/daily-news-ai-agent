Absolutely Yash! Here's a complete and clean `README.md` file for your project: **AI News Agent** that fetches news, summarizes it, converts it to voice, and sends it via Telegram and Email.

---

## 📄 `README.md`

````markdown
# 🗞️ AI News Agent

A smart AI agent that fetches the latest news, summarizes it using Gemini AI, converts it to speech, and sends it to you daily via **Telegram** and **Email**. Built with Python.

---

## ✨ Features

- 🔍 Fetches latest news headlines
- 🧠 Summarizes news using Gemini AI
- 🔊 Converts summary to **natural English voice**
- 📤 Sends voice & text message to **Telegram**
- 📧 Sends summary to **Email**
- ⏰ Runs automatically on a schedule (every X seconds or daily)

---

## 🛠️ Tech Stack

- Python 3
- `requests` for APIs
- `gTTS` for text-to-speech
- `google.generativeai` (Gemini API)
- `schedule` for task automation
- `smtplib` for email sending
- Telegram Bot API

---

## 📦 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/ai-news-agent.git
cd ai-news-agent
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, install manually:

```bash
pip install requests gTTS schedule python-dotenv
```

### 3. Create `.env` File

Create a `.env` file in the root folder:

```
SMTP_USER=your_gmail@gmail.com
SMTP_PASS=your_email_app_password
```

---

## 🔐 Required API Keys

### ✅ Gemini API (for summarizing)

* Get it from [Google AI Studio](https://makersuite.google.com/app/apikey)
* Replace your key in `ai_summarizer.py`

### ✅ Telegram Bot Token

* Create bot via [@BotFather](https://t.me/BotFather)
* Paste the token & chat ID in `main.py`

---

## ✅ Running the Agent

### Run Once:

```bash
python main.py
```

### Run Every 10 Seconds (test):

```python
schedule.every(10).seconds.do(job)
```

### Run Daily at 8 AM:

```python
schedule.every().day.at("08:00").do(job)
```

---

## 📁 Project Structure

```
📦 ai-news-agent
├── main.py                # Entry point
├── news_fetcher.py        # Fetch headlines
├── ai_summarizer.py       # Summarize using Gemini
├── voice_generator.py     # Convert text to speech
├── telegram_send.py       # Send text + voice via Telegram
├── send_mail.py           # Send email
├── .env                   # Email credentials
└── requirements.txt
```

---

## 📤 Deployment Options

| Platform          | Notes                            |
| ----------------- | -------------------------------- |
| 🔹 Render         | Best for background workers      |
| 🔹 PythonAnywhere | Great for beginners & scheduling |
| 🔹 Replit         | For light testing                |

---

## 🔒 Security Note

* Never commit `.env` or API keys to GitHub.
* Add `.env` to your `.gitignore`.

---

## 🙋‍♂️ Author

**Yash Dhokane**
📧 [yashdhokane12@gmail.com](mailto:yashdhokane12@gmail.com)
🔗 [LinkedIn](https://linkedin.com/in/yashdhokane)

---

## 📜 License

MIT License. Feel free to use or modify this project.

---

## 🚀 Want to improve it?

* Add news categories (tech, politics, etc.)
* Support multiple languages (Hindi, Marathi)
* Deploy with a front-end dashboard

PRs and suggestions are welcome!

```

---

Would you like me to:
- Create this file for you?
- Help you push it to GitHub?
- Add a `requirements.txt` or `Procfile` for deployment?

Let me know how you'd like to proceed next 🚀
```
