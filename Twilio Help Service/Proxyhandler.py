# Get the Python helper library from https://twilio.com/docs/libraries/python
from twilio.rest import Client
import uuid

# Get your Account SID and Auth Token from https://twilio.com/console
account = "AC6171934216186661cda5e8c49c82db24"
token = "3d9dc7d0ccf72dd486af6a95ec69e4eb"

client = Client(account, token)

servicesid = "KS041c20c7b86072133d4053883b04a8b6"

def connect(body, userNumber, volNumber):
  

    session = client.proxy \
        .services(servicesid) \
        .sessions \
        .create(unique_name=str(uuid.uuid4()), ttl=90)

    participant = client.proxy \
        .services(servicesid) \
        .sessions(session.sid) \
        .participants.create(identifier=volNumber, friendly_name="Volunteer")
    volunteerSID = participant.fetch().sid


    participant2 = client.proxy \
        .services(servicesid) \
        .sessions(session.sid) \
        .participants.create(identifier=userNumber, friendly_name="User")



    message_interaction = client.proxy \
        .services(servicesid) \
        .sessions(session.sid) \
        .participants(volunteerSID) \
        .message_interactions.create(body="Someone needs assistance. They said: " + body)

