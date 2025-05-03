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
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>BlueRelay: Weather Alerts</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 0;
                    color: #333;
                }
                header {
                    background-color: #000;
                    color: #fff;
                    text-align: center;
                    padding: 20px;
                    font-size: 2em;
                    font-weight: bold;
                }
                footer {
                    background-color: #000;
                    color: #fff;
                    text-align: center;
                    padding: 10px;
                    position: fixed;
                    width: 100%;
                    bottom: 0;
                }
                .container {
                    padding: 20px;
                    margin-bottom: 50px; /* To prevent content from being hidden behind footer */
                }
                .alert {
                    margin-bottom: 20px;
                    background-color: #fff;
                    padding: 15px;
                    border-radius: 5px;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                }
                a {
                    color: #007BFF;
                    text-decoration: none;
                }
                .about-button {
                    display: inline-block;
                    background-color: #007BFF;
                    color: white;
                    padding: 10px 20px;
                    border-radius: 5px;
                    text-decoration: none;
                    font-size: 1em;
                    margin-top: 20px;
                }
                .about-button:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <header>BlueRelay</header>
            <div class="container">
                <h1>Weather Alerts</h1>
                {% for a in alerts %}
                    <div class="alert">
                        <h2>{{ a.headline }}</h2>
                        <p><strong>Severity:</strong> {{ a.severity }}</p>
                        <p><strong>Area:</strong> {{ a.area }}</p>
                        <a href="{{ a.url }}" target="_blank">View full alert</a>
                    </div>
                {% endfor %}
                <a class="about-button" href="https://github.com/YourGitHubRepoLink" target="_blank">About</a>
            </div>
            <footer>
                <p>License: MIT</p>
            </footer>
        </body>
        </html>
        """, alerts=alerts)

    except Exception as e:
        return f"<h1>error</h1><p>{e}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
