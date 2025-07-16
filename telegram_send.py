# telegram_send.py
import requests
import dotenv
import os   
dotenv.load_dotenv()
def send_telegram_message( message):
    url = f"https://api.telegram.org/bot{os.getenv("bot_token") }/sendMessage"
    response = requests.post(url, data={
        "chat_id":os.getenv("chat_id"),
        "text": message
    })
    print("Text message:", response.json())

def send_telegram_voice(voice_file_path):
    url = f"https://api.telegram.org/bot{os.getenv("bot_token")}/sendVoice"
    with open(voice_file_path, 'rb') as voice:
        response = requests.post(url, data={"chat_id": os.getenv("chat_id")}, files={"voice": voice})
    print("Voice message:", response.json())
