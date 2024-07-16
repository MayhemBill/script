def customCurrentTime():
    return datetime.now().strftime('%H:%M %p')

def currentWeatherIcon():
    icondata = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key=8214f5a2223c42a084e233902240603&q=34221&days=1").json()
    iconresponse = icondata['current']['condition']['icon']
    return f"https:{iconresponse}"

def currentWeatherTemp():
    tempdata = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key=8214f5a2223c42a084e233902240603&q=34221&days=1").json()
    tempresponse = round(tempdata['current']['feelslike_f'])
    return f"{tempresponse}°F"

def currentWeatherHumidity():
    humditydata = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key=8214f5a2223c42a084e233902240603&q=34221&days=1").json()
    humitidyresponse = humditydata['current']['humidity']
    return f"{humitidyresponse}%"

addDRPCValue("custom_time", customCurrentTime)
addDRPCValue("weathericon", currentWeatherIcon)
addDRPCValue("temperature", currentWeatherTemp)
addDRPCValue("humidity", currentWeatherHumidity)
