import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/35eee830991c22f8d195d5bdad73dfee/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to Get all the data in taht sheet and print it out
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    # 6 In the DataManager Class make a put request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes (Do this using code.).

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data)
            print(response.text)

