from twilio.rest import Client


def send_sms(to, body):
    account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    auth_token = '1234567890abcdef1234567890abcdef'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_='+998901712006',
        to=to
    )
    return message.sid
