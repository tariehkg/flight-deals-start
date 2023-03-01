import requests

from data_manager import DataManager
from flight_search import FlightSearch

SHEET_NAME = "prices2"
SHEETY_ENDPOINT = "https://api.sheety.co/35eee830991c22f8d195d5bdad73dfee/flightDeals/"
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
print(sheet_data)
for row in sheet_data:
    if not row['iataCode']:
        city = row['city']
        flight_search = FlightSearch()
        iata_code = flight_search.search_flights(city)
        row['iataCode'] = iata_code

        # Update the Google Sheet with the new IATA COde using Sheety
        sheet_id = row['id']
        sheet_url = f"{SHEETY_ENDPOINT}/{SHEET_NAME}/{sheet_id}"
        new_data = {"price": {"iataCode": row['iataCode']}}
        response = requests.put(sheet_url, json=new_data)
        print(response.json())



print("This is after the For call")
print(sheet_data)



#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.