import requests
import random
import datetime

API_URL = "https://analytics-api-eu.piano.io/import/measurements/v1"
API_KEY = "c27d9f09dc98_82c3a18de25db3375ea5d7afeeb378ac0b0e2c72"

def generate_measurements():
    today = datetime.date.today()
    measurements = []

    for i in range(1, 8):  # Past 7 days (not including today)
        day = today - datetime.timedelta(days=i)
        measurement = {
            "key": "ota_viewership",
            "period": day.strftime("%Y-%m-%d"),
            "values": {
                "ota_viewership": random.randint(8000, 22000),
                "ota_average_viewing_time": random.randint(2500, 13000)
            }
        }
        measurements.append(measurement)

    return {"measurements": measurements}

def post_data():
    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY
    }
    payload = generate_measurements()
    response = requests.post(API_URL, json=payload, headers=headers)
    print("Status Code:", response.status_code)
    print("Response:", response.text)

if __name__ == "__main__":
    post_data()
