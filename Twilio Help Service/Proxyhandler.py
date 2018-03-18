# Get the Python helper library from https://twilio.com/docs/libraries/python
from twilio.rest import Client
import uuid
from configparser import ConfigParser

config = ConfigParser()
config.read('config.cfg')
account = config.get('auth', 'account')
token = config.get('auth', 'token')
servicesid = config.get('auth', 'servicesid')


# Get your Account SID and Auth Token from https://twilio.com/console

client = Client(account, token)



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

