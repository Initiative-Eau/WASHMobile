import twilio
from twilio.rest import Client
import pandas
import os

water_sources_df = pandas.read_csv(os.path.join(os.getcwd(), "water_sources_data.csv"))
print("loaded_data")

account_sid = "<account>"
auth_token = "<auth>"
client = Client(accound_sid, auth_token)

message = client.api.account.messages.create(to="+12018741921",from_="+<account phone number>", body="What's Gucci Fam?")
