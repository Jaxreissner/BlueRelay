from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://api.weather.gov/alerts/active"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        alerts = []
        for alert in data['features'][:5]:
            props = alert['properties']
            alerts.append({
                'headline': props['headline'],
                'severity': props['severity'],
                'area': props['areaDesc'],
                'url': props['web']
            })

        return render_template_string("""
        <h1>BlueRelay: Weather Alerts</h1>
        {% for a in alerts %}
            <h2>{{ a.headline }}</h2>
            <p><strong>Severity:</strong> {{ a.severity }}</p>
            <p><strong>Area:</strong> {{ a.area }}</p>
            <a href="{{ a.url }}" target="_blank">View full alert</a>
            <hr>
        {% endfor %}
        """, alerts=alerts)

    except Exception as e:
        return f"<h1>error</h1><p>{e}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
