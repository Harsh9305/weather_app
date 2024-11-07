from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# OpenWeatherMap API URL
API_KEY = 'b24753d908e3fcd35c036f096e4abbf0'  # Replace with your actual API Key

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get('city')  # Get city name from form input
        weather = get_weather_data(city)  # Fetch weather data
        if weather:
            return render_template("index.html", weather=weather)
        else:
            error = "City not found. Please try again."

    return render_template("index.html", weather=weather, error=error)

def get_weather_data(city):
    # Fetch weather data from OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print(f"Error: {data.get('message', 'Unknown error')}")
            return None

        # Parse weather data to send to the template
        weather_info = {
            "city": data["name"],
            "description": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "icon": data["weather"][0]["icon"],  # Icon code
        }
        return weather_info

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
