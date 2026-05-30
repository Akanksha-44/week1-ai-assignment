import requests

url = "https://catfact.ninja/fact"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("\n🐱 Cat Fact:")
    print(data["fact"])

else:
    print("Failed to fetch data.")