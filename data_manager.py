import requests
from pprint import pprint


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
    # Use the Sheety API to Get all the data in taht sheet and print it out

        GOOGLE_SHEET_NAME = "prices"
        sheet_endpoint = "https://api.sheety.co/35eee830991c22f8d195d5bdad73dfee/flightDeals/prices"
        response = requests.get(sheet_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_iata_codes(self):
        """Update the Google Sheet with teh IATA Codes"""



