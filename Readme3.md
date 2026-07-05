# Weather Information App

## Overview

The Weather Information App is a simple Python application that allows users to check the current weather of any city using the command line. It retrieves live weather information from the wttr.in weather service and displays important weather details in an easy-to-read format.

## Features

- Search weather by city name
- Displays current temperature
- Shows humidity percentage
- Displays weather condition
- Shows "Feels Like" temperature
- Displays wind speed
- Simple command-line interface
- Basic error handling for connection issues

## Technologies Used

- Python
- Requests Library
- wttr.in Weather API

## Project Structure

```
Weather Information App/
│── weather_app.py
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Weather-Information-App.git
```

2. Navigate to the project folder:

```bash
cd Weather-Information-App
```

3. Install the required package:

```bash
pip install requests
```

## How to Run

Run the application using:

```bash
python weather_app.py
```

## Example Output

```
===== Weather Information App =====

Enter city name: Hyderabad

------ Current Weather ------
Location      : Hyderabad
Temperature   : 31°C
Feels Like    : 35°C
Humidity      : 68%
Weather       : Partly cloudy
Wind Speed    : 12 km/h
```

## Learning Outcomes

- Working with APIs
- Making HTTP requests using Python
- Parsing JSON data
- Exception handling
- Command-line application development

## Future Improvements

- Add weather forecast for multiple days
- Support ZIP code search
- Display sunrise and sunset timings
- Add a graphical user interface (GUI)
- Save weather reports to a file

## Author

**Jahnavi Gopisetty**