from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import pandas
import os

# Load Water Source CSV
current_dir = os.getcwd()
above_dir = os.path.split(current_dir)[0]
data_dir = os.path.join(above_dir, "Webpage","water_sources_data.csv")
water_sources_df = pandas.read_csv(data_dir)
print("loaded water sources data")


# Load Secure Twilio Credentials
desktop_dir = os.path.split(os.path.split(os.getcwd())[0])[0]
credentials_path = os.path.join(desktop_dir, "twilio_credentials")
credentials_file = open(credentials_path, "r")
credentials_content = credentials_file.read()

credentials_content = credentials_content.split("\n")
account_sid = credentials_content[0]
auth_token = credentials_content[1]
twilio_number = credentials_content[2]

account_sid = account_sid.split(" = ")[1]
auth_token = auth_token.split(" = ")[1]
twilio_number = twilio_number.split(" = ")[1]

account_sid = str(account_sid)
auth_token = str(auth_token)
twilio_number = str(twilio_number)
print("loaded twilio credentials")


app = Flask(__name__)

# Initiate Twilio Client
# client = Client(account_sid, auth_token)

@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    water_source = water_sources_df[water_sources_df['ID'] == message_body]
    if water_source.shape[0]==0:
        response = "Water source "+message_body+" was not found."
    elif water_source.shape[0]==1:
        response = "Water source "+message_body+" is located at Lat: "+water_source['Latitude']+" Lng: "+water_source['Longitude']+". It is rated as "+water_source['Grade']+" ("+water_source['WQI']+"), and was last updated on: "+water_source_['Updated']+"."
    else:
        response = "Sorry, we had a database error!"
    resp = MessagingResponse()
    resp.message(response)
    return str(resp)

#message = client.api.account.messages.create(to="+12018741921",from_="+<account phone number>", body="What's Gucci Fam?")
if __name__ == '__main__':
    # app.run(host = '0.0.0.0', port=80, debug=False)
    app.run()