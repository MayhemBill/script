def currentWeather():
    data = requests.get('http://api.openweathermap.org/data/2.5/weather?appid=3e6826fb716810018759216195531995&units=imperial&q={city}').json()
    temperature = round(data['main']['feels_like'])
    return f"{temperature}°F"

def customCurrentTime():
    return datetime.now().strftime('%H:%M %p')

addDRPCValue("weather", currentWeather)
addDRPCValue("custom_time", customCurrentTime)
