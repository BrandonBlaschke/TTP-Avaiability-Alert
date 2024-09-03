import requests
import time
import sys
from twitterNotifier import postTweet
import user_agent


APPOINTMENTS_URL = "https://www.recreation.gov/api/permits/{locationId}/availability/month"
# Endpoint for info: https://www.recreation.gov/api/permits/233273
# Endpoint for appointments: https://www.recreation.gov/api/permits/233273/availability/month?start_date=2024-09-01T00:00:00Z

START_DATE = "2024-10-01T00:00:00.000Z"

LOCATION_IDS = {
  "233273": "Enchantment"
}

SITE_IDS = {
  "30": "Core",
  "29": "Colchuck",
  "23": "Snow",
  "27": "Stuart",
  "28": "Eightmile/Caroline"
}


def sendRequest(locationId, startDate):
  params = {"start_date": startDate}
  headers = {"User-Agent": user_agent.generate_user_agent()}
  url = APPOINTMENTS_URL.format(locationId=locationId)
  response = requests.get(url, params=params, headers=headers)
  jsonResponse = response.json()
  return jsonResponse

def checkAppointments(jsonResponse):
  appointments = []
  for siteId, availability in jsonResponse["payload"]["availability"].items():
    if siteId not in SITE_IDS:
      continue
    for date, details in availability["date_availability"].items():
      availableCount = details["remaining"]
      if availableCount > 0:
        siteName = SITE_IDS[siteId]
        appointments.append((siteName, formatDate(date), details["remaining"]))
  return appointments

def formatDate(date):
  return date.split('T')[0]

def createMessage(appointments):
  lines = []
  for siteName, date, availableCount in appointments:
    line = ", ".join([siteName, date, str(availableCount)])
    lines.append(line)
  return "\n".join(lines)


if __name__ == "__main__":
  try:
    while True:
      for locationId, locationName in LOCATION_IDS.items():
        try:
          jsonResponse = sendRequest(locationId, START_DATE)
          appointments = checkAppointments(jsonResponse)
        except Exception as e:
          print("Request failed: " + str(e))
          continue

        if appointments:
          message = createMessage(appointments)
          postTweet(message)
        else:
          print("No appointments available")
        time.sleep(1)

      # how often to run this check in seconds
      time.sleep(30)
  except KeyboardInterrupt:
    sys.exit(0)
    