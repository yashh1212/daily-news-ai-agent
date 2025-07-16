# send_mail.py
import smtplib
from email.mime.text import MIMEText
import dotenv
import os

dotenv.load_dotenv()

def send_email(summary, to_email):
    msg = MIMEText(summary)
    msg['Subject'] = 'Daily News Summary'
    msg['From'] = os.getenv('SMTP_USER')
    msg['To'] = to_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  
        server.login(os.getenv('SMTP_USER'), os.getenv('SMTP_PASS'))
        server.send_message(msg)
        print("Email sent successfully to", to_email)
