import requests
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from blok_app.models import Task

@receiver(post_save, sender = Task)
def Task_signals_post(sender, instance, created, **kwargs):
    telegram_token = settings.TELEGRAM_BOT_TOKEN
    chat_id = 5145991019
    url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'

    message_text = f"user_id: {instance.user.id}\n title: {instance.title}"

    response = requests.post(
        url=url,
        data={'chat_id': chat_id, 'text': message_text}
    )
