import requests

class WeatherModule:
    def __init__(self, location="Gwalior", api_key="7e182f22c2f21059417130c036c2df40"):
        self.location = location
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_real_time_weather(self):
        params = {
            'q': self.location,
            'appid': self.api_key,
            'units': 'metric'
        }

        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()

            if response.status_code != 200:
                raise Exception(data.get("message", "API Error"))

            weather_info = {
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'rainfall': data.get('rain', {}).get('1h', 0.0),
                'description': data['weather'][0]['description']
            }
            return weather_info

        except Exception as e:
            return {"error": str(e)}

    def generate_crop_advisory(self, crop):
        weather = self.get_real_time_weather()

        if 'error' in weather:
            return f"❌ Error fetching weather data: {weather['error']}"

        advisory = f"📍 Location: {self.location}\n🌾 Crop: {crop}\n"
        advisory += f"\n📊 Weather Data:\n🌡 Temp: {weather['temperature']}°C\n💧 Humidity: {weather['humidity']}%\n🌧 Rainfall (last 1h): {weather['rainfall']}mm\n🌤️ Condition: {weather['description'].capitalize()}\n"

        # Advisory logic
        if weather['rainfall'] < 2:
            advisory += "💧 Advice: Consider irrigating the crop.\n"
        if weather['temperature'] > 35:
            advisory += "🔥 Warning: High temperature! Apply mulch or provide shade.\n"
        if weather['humidity'] > 80:
            advisory += "⚠️ Caution: High humidity can lead to fungal infections. Monitor crops closely.\n"

        return advisory
