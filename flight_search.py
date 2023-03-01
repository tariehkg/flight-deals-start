import requests

#TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_API_KEY = "F_bokK6SisaamT1mJMuBRy6tVuk4GbQc"


class FlightSearch:

    def get_destination_code(self, city_name):
        # set the query parameters
        params = {
            "term": city_name, #the city name your want to search
            "location_type": "city", #the type of location you want to search
            "limit": 1 # limit the number of results returned to 1
        }

        # set the headers, including the API Key
        headers = {
            "apikey": TEQUILA_API_KEY,
            "accept": "application/json"
        }

        # send the GET request to the API endpoint
        response = requests.get(TEQUILA_ENDPOINT, params=params, headers=headers)

        # Get the JSON resonse
        json_response = response.json()

        # Print the json response
        print(json_response)

        # Get the IATA code from the response
        iata_code = json_response["locations"][0]["code"]

        # return the IATA code
        return iata_code


