import twilio
from twilio.rest import Client
import pandas
import os

water_sources_df = pandas.read_csv(os.path.join(os.getcwd(), "water_sources_data.csv"))
print("loaded_data")

account_sid = "AC36878ead4766e4b1ebd76dd4ae4ded4a"
auth_token = "9084ae0bf6b06a52fd5c3b102d57a515"
client = Client(accound_sid, auth_token)

message = client.api.account.messages.create(to="+12018741921",from_="+<account phone number>", body="What's Gucci Fam?")
