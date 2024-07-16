@bot.command()
async def weather(ctx, location: str, days: int = 1):
    await ctx.message.delete()
    try:
        response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key=8214f5a2223c42a084e233902240603&q={location}&days={days}")
        data = response.json()
        forecast_days = data['forecast']['forecastday']
        if len(forecast_days) < days: return await ctx.send("Error: Forecast data not available for all specified days.")
        weather_message = f"Weather forecast for {location} for the next {days} days:\n\n"
        for day in range(days):
            forecast_day = forecast_days[day]
            date, condition, max_temp, min_temp, humidity = forecast_day['date'], forecast_day['day']['condition']['text'], forecast_day['day']['maxtemp_f'], forecast_day['day']['mintemp_f'], forecast_day['day']['avghumidity']
            wind_speed = forecast_day['day']['maxwind_kph'] * (1000 / 3600)
            day_message = (f"```ini\nDay [ {day+1} ] ({date}):\n"f"Condition: [ {condition} ]\n"f"Max temperature: [ {max_temp}°F ]\n"f"Min temperature: [ {min_temp}°F ]\n"f"Humidity: [ {humidity}% ]\n"f"Wind speed: [ {wind_speed:.2f} m/s ]\n```\n")
            weather_message += day_message
        await ctx.send(weather_message)
    except: pass
