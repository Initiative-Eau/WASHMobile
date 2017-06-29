from flask import Flask, reqiest, redorect
import twilio
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import pandas
import os

water_sources_df = pandas.read_csv(os.path.join(os.getcwd(), "water_sources_data.csv"))
print("loaded_data")

app = Flask(__name__)

account_sid = "<account>"
auth_token = "<auth>"
client = Client(accound_sid, auth_token)

@app.rout('/sms', methods=['POST']
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    water_source = water_sources_df[water_sources_df['ID'] == message_body]
    if water_source.shape[0]==0:
        response = "Water source "+message_body+" was not found."
    elif water_source.shape[0]==1:
        response = "Water source "+message_body+" is located at Lat: "+water_source['Latitude']+" Lng: "+water_source['Longitude']+". It is rated as "+water_source['Grade']+" ("+water_source['WQI']+"), and was last updated on: "+water_source_['Updated']+"."
    else:
        resposne = "Sorry, we had a database error!"
    resp = twiml.Response()
    resp.message(response)
    return str(resp)

#message = client.api.account.messages.create(to="+12018741921",from_="+<account phone number>", body="What's Gucci Fam?")
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=80, debug=False)
