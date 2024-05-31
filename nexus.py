import requests
import time
import sys
from datetime import datetime, timedelta
from twilio.rest import Client
from credentials import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TEXT_TO_NUMBER, TEXT_FROM_NUMBER 

# Idea and details located here. I just added SMS capability
# https://packetlife.net/blog/2019/aug/7/apis-real-life-snagging-global-entry-interview/

# API URL
APPOINTMENTS_URL = "https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&limit=1&locationId={}&minimum=1"

# List of Global Entry locations
LOCATION_IDS = {
    "Blaine NEXUS": 5220,
    "SEAFO-Blaine": 16764,

}

# How often to run this check in seconds
TIME_WAIT = 30

# Number of days into the future to look for appointments
DAYS_OUT = 90

# Dates
now = datetime.now()
future_date = now + timedelta(days=DAYS_OUT)


def send_text(to_number, from_number, message, sid, token):
    client = Client(sid, token)

    message = client.messages.create(
        to=to_number, 
        from_=from_number,
        body =message)

    return message.sid

def check_appointments(city, id):
    url = APPOINTMENTS_URL.format(id)
    appointments = requests.get(url).json()
    return appointments

def appointment_in_timeframe(now, future_date, appointment_date):
    if now <= appt_datetime <= future_date:
        return True
    else:
        return False


try:
    while True:
        for city, id in LOCATION_IDS.items():
            try:
                appointments = check_appointments(city, id)
            except Exception as e:
                print("Could not retrieve appointments from API.")
                appointments = []
            if appointments:
                appt_datetime = datetime.strptime(appointments[0]['startTimestamp'], '%Y-%m-%dT%H:%M')
                if appointment_in_timeframe(now, future_date, appt_datetime):
                    message = "{}: Found an appointment at {}!".format(city, appointments[0]['startTimestamp'])
                    print(message)
                    # try:
                    #     sms_sid = send_text(TEXT_TO_NUMBER, TEXT_FROM_NUMBER, message, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
                    #     print(message, "Sent text successfully! {}".format(sms_sid))
                    # except Exception as e:
                    #     print(e)
                    #     print(message, "Failed to send text")
                else:
                    print("{}: No appointments during the next {} days".format(city, DAYS_OUT))
            else:
                print("{}: No appointments during the next {} days".format(city, DAYS_OUT))
            time.sleep(1)
        time.sleep(TIME_WAIT)
except KeyboardInterrupt:
    sys.exit(0)