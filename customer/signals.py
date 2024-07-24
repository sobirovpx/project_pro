import json
import os

from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from config.settings import BASE_DIR
from .models import Customer

@receiver(pre_delete, sender=Customer)
def customer_pre_delete(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'app/delete_products/', f'product_{instance.id}.json')
    customer_data = {
        'name': instance.name,
        'email': instance.email
    }
    with open(file_path, 'w') as f:
        json.dump(customer_data, f)

    send_mail(
        'Customer Deletion Notification',
        f'The customer {instance.name} is about to be deleted.',
        'ali@gmail.com',
        [instance.email],
        fail_silently=False,
    )

@receiver(post_save, sender=Customer)
def customer_save(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Welcome!',
            f'Thank you for registering, {instance.name}!',
            'ali@gmail.com',
            [instance.email],
            fail_silently=False,
        )