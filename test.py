import requests
import random
import json

# Flask API endpoint
url = "http://172.25.31.124:5000/predictx"  # Replace with your Flask server's URL if hosted elsewhere

# Function to generate random data
def generate_random_data():
    random_data = {
        "inputs": [
            {
                "distance": round(random.uniform(1, 100), 2),  # Random distance between 1 and 100 km
                "fuel_price": round(random.uniform(1.0, 5.0), 2),  # Random fuel price between $1.0 and $5.0
                "trips_per_day": random.randint(1, 5),  # Random trips per day between 1 and 5
                "peak_off_peak": random.choice([0, 1])  # Randomly 0 (Off-Peak) or 1 (Peak)
            }
        ]
    }
    return random_data

# Function to send data to the Flask API and log the response
def test_random_data():
    for _ in range(10):  # Generate and test 10 random samples
        random_data = generate_random_data()
        print(f"Testing with input: {json.dumps(random_data, indent=2)}")
        
        try:
            # Send POST request to the Flask API
            response = requests.post(url, json=random_data)
            # Check response status
            if response.status_code == 200:
                print(f"Response: {response.json()}\n")
            else:
                print(f"Error: {response.status_code}, {response.text}\n")
        except Exception as e:
            print(f"An error occurred: {e}")

# Run the test
if __name__ == "__main__":
    test_random_data()
