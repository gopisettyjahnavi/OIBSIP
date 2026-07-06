import requests
print(" Weather Information App ")
city = input("Enter city name: ").strip()
url = f"https://wttr.in/{city}?format=j1"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    current = data["current_condition"][0]
    temperature = current["temp_C"]
    humidity = current["humidity"]
    weather = current["weatherDesc"][0]["value"]
    print("\n Weather Report ")
    print("City         :", city.title())
    print("Temperature  :", temperature, "°C")
    print("Humidity     :", humidity, "%")
    print("Condition    :", weather)

else:
    print("Unable to fetch weather information. Please try again.")