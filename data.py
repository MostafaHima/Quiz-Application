import requests
import random

url_endpoint = "https://opentdb.com/api.php"
paramters = {
    "amount": random.randint(10, 20),
    "type": "boolean",
    "category":19
}

response = requests.get(url=url_endpoint, params=paramters)
question_data = response.json()["results"]

