import smtplib, ssl
import os
from dotenv import load_dotenv


load_dotenv()

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    user_name = os.getenv('GMAIL_SEND_USER_NAME')
    password = os.getenv('GMAIL_APP_PASSWORD')

    receiver = os.getenv('GMAIL_RECEIVE_USER_NAME')
    context1 = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context1) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)