import requests
print("===== Weather Information App =====")
location = input("Enter city name: ").strip()
url = f"https://wttr.in/{location}?format=j1"
try:
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()

        current = weather_data["current_condition"][0]
        temperature = current["temp_C"]
        humidity = current["humidity"]
        description = current["weatherDesc"][0]["value"]
        feels_like = current["FeelsLikeC"]
        wind_speed = current["windspeedKmph"]

        print("\n------ Current Weather ------")
        print(f"Location      : {location.title()}")
        print(f"Temperature   : {temperature}°C")
        print(f"Feels Like    : {feels_like}°C")
        print(f"Humidity      : {humidity}%")
        print(f"Weather       : {description}")
        print(f"Wind Speed    : {wind_speed} km/h")

    else:
        print("Unable to fetch weather details.")

except Exception as e:
    print("Something went wrong!")
    print("Error:", e)