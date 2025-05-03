import requests

def fetch_weather_alerts():
    url = "https://api.weather.gov/alerts/active"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        print("Current Alerts:")
        for alert in data['features'][:5]:  # limit to first 5 for testing
            props = alert['properties']
            print(f"- {props['headline']}")
            print(f"  Severity: {props['severity']}")
            print(f"  Area: {props['areaDesc']}")
            print(f"  More info: {props['web']}")
            print()
    except Exception as e:
        print("error fetching alerts:", e)

if __name__ == "__main__":
    fetch_weather_alerts()
