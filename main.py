import schedule, time
from news_fetcher import get_news
from ai_summarizer import summarize_news
from send_mail import send_email
from telegram_send import send_telegram_message,send_telegram_voice
from voice_generate import text_to_speech
import dotenv
import os
dotenv.load_dotenv()

def job():
    news = get_news()
    summary = summarize_news(news)
    voice_path = text_to_speech(summary)

    # Send to Telegram
    send_telegram_message(
        message=summary
    )
    send_telegram_voice(
        voice_file_path=voice_path
    )

    # Send to Email
    send_email(summary, os.getenv('Email'))
    print("Job executed successfully.\n")


schedule.every().day.at("08:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)