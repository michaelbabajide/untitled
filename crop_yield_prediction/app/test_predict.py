import requests

# Example input matching your dataset structure
test_input = {
    'region': 'north',
    'soil_type': 'loam',
    'crop': 'wheat',
    'rainfall_mm': 500,
    'temperature_celsius': 25,
    'fertilizer_used': True,
    'irrigation_used': True,
    'weather_condition': 'sunny',
    'days_to_harvest': 120
}

# Send prediction request
response = requests.post('http://0.0.0.0:9696/predict', json=test_input, timeout=10)
print(response.json())