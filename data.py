import requests
import html


parameters = {
    "amount": 10,
    "type": "boolean"
}


response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
