from twilio.rest import Client
from credentials import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TEXT_TO_NUMBER, TEXT_FROM_NUMBER

def send_text(to_number, from_number, message, sid, token):
    client = Client(sid, token)
    message = client.messages.create(
        to=to_number, 
        from_=from_number,
        body =message)
    return message.sid

def sendSMS(message):
    try:
        sms_sid = send_text(TEXT_TO_NUMBER, TEXT_FROM_NUMBER, message, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        print(message, "Sent text successfully! {}".format(sms_sid))
    except Exception as e:
        print(e)
        print(message, "Failed to send text")
        