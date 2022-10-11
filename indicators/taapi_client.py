# Import the requests library
import requests


class taapi_client:
    # Define endpoint
    __endpoint = "https://api.taapi.io/bulk"
    __secret = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjM0NDg0ZjVmYzVhOGFkZmVjMjI5YzQ2IiwiaWF0I" \
               "joxNjY1NDM0ODY5LCJleHAiOjMzMTY5ODk4ODY5fQ.V2YGyD7MBHmaY-Zn3CTtluyYi1Cm8I1h6E1bEuxIh0A"

    def loan_indicator(indicator_construct):
        # Define a JSON body with parameters to be sent to the API
        parameters = {
            "secret": taapi_client.__secret,
            "construct": indicator_construct
        }

        # Send POST request and save the response as response object
        response = requests.post(url=taapi_client.__endpoint, json=parameters)
        # Extract data in json format
        result = response.json()
        # Print result
        # print(result)
        return result
