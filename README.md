# TTP-Avaiability-Alert

This software retrieves appointment availability from the Trusted Traveler Programs' website for various programs like Global Entry, NEXUS, SENTRI, US/Mexico FAST, and US/Canada FAST without needing TTP account login details. It also includes the capability to alert users via tweets (using Twitter API 2.0) or SMS (using Twilio API).

## Usage

Run the script with `python`: `python3 main.py`


## Interview center codes

* [Global Entry location list](https://ttp.cbp.dhs.gov/schedulerapi/locations/?temporary=false&inviteOnly=false&operational=true&serviceName=Global%20Entry)

* [NEXUS location list](https://ttp.cbp.dhs.gov/schedulerapi/locations/?temporary=false&inviteOnly=false&operational=true&serviceName=NEXUS)

* [SENTRI location list](https://ttp.cbp.dhs.gov/schedulerapi/locations/?temporary=false&inviteOnly=false&operational=true&serviceName=SENTRI)

* [US/Mexico FAST location list](https://ttp.cbp.dhs.gov/schedulerapi/locations/?temporary=false&inviteOnly=false&operational=true&serviceName=U.S.%20%2F%20Mexico%20FAST)

* [US/Canada FAST location list](https://ttp.cbp.dhs.gov/schedulerapi/locations/?temporary=false&inviteOnly=false&operational=true&serviceName=U.S.%20%2F%20Canada%20FAST)
