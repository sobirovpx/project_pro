from .sms_utils import send_sms
from .email_utils import send_notification


def notify_user_via_sms_and_email(phone_number, sms_body, email_subject, email_message, recipient_email):
    sms_sid = send_sms(phone_number, sms_body)
    email_body = f"{email_message}\n\nSMS SID: {sms_sid}"
    send_notification(email_subject, email_body, [recipient_email])
