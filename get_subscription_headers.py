import requests


def get_subsription_headers():
    # fetch public subscription key
    response = requests.get("http://dataminer2.pjm.com/config/settings.json")
    settings = response.json()
    key = settings["subscriptionKey"]

    # create header with subscription key
    headers = {
        "Ocp-Apim-Subscription-Key": key,
    }
    return headers
