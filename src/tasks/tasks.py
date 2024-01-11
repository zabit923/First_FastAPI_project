import smtplib
from email.message import EmailMessage

from celery import Celery
from config import SMTP_USER, SMTP_PASS

SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 465

celery = Celery('tasks', broker='redis://localhost:6379')


def get_email_template(username: str):
    email = EmailMessage()
    email['Subject'] = 'Тест'
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER

    email.set_content(
        f'''<div>
                <h1 style="color: red;">
                    Здравствуйте, {username}
                </h1>
                <img src="https://smapse.ru/storage/2021/06/converted/895_0_shweicaria-smapse-1.jpg" width="600">
            </div>''',
        subtype='html'
    )
    return email

@celery.task
def send_email_report(username: str):
    email = get_email_template(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(email)
