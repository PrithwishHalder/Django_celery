from celery import shared_task
from django.core.mail import send_mail
from time import sleep

@shared_task
def send_email_task(sender):
    sleep(5)
    send_mail("CELERY Working", "Mail sent using Celery", 'prithwishtesting@gmail.com', [sender,])
    return "Mail Sent"