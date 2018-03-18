from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import importlib
from Proxyhandler import connect
from NumbersList import addnum, removenum, RetRandomNum

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    resp =MessagingResponse()
    if(str(body) == "Commands" or str(body) == "?"):
        resp.message("If you are in need, simply send any message to this number. To Volunteer, text REGISTER. If you are already registered, text DEREGISTER to remove yourself from the volunteer list.")
        return str(resp)

    elif str(body).lower() == "register":
        resp.message("Thank you for your kindness.")
        addnum(request.values.get('From'))
        return str(resp)

    elif str(body).lower() == "deregister":
        resp.message("We are sorry to see you go.")
        removenum(request.values.get('From'))
        return str(resp)

    else:
    # Start our TwiML response
        resp.message("Thank you for your bravery, please wait shortly for someone to reach out.")

        print(request.values.get('From', None))
        connect(body, request.values.get('From'), RetRandomNum())

    return str(resp)
 

if __name__ == "__main__":
    app.run(debug=True)
