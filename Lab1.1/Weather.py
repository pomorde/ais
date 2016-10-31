import pyowm
owm = pyowm.OWM('27ee236faf689f70eeeee34a91a83f04')
rnd = owm.weather_at_place('Rostov-on-don,ru')
weather = rnd.get_weather()
associateArray = {"Rostov-na-Donu": 'Ростов-на-дону'}
def Clouds():
    if 0 <= weather.get_clouds() <= 10:
        return "ясная"
    if 10 <= weather.get_clouds() <= 30:
        return "немного облачная"
    if 30 <= weather.get_clouds() <= 70:
        return "облачная"
    if 70 <= weather.get_clouds() <= 100:
        return "пасмурная"
def Wind():
    if 338 <= weather.get_wind()['deg'] <= 22:
        return 'северный'
    if 23 <= weather.get_wind()['deg'] <= 68:
        return 'северо-восточный'
    if 69 <= weather.get_wind()['deg'] <= 114:
        return 'восточный'
    if 115 <= weather.get_wind()['deg'] <= 160:
        return 'юго-восточный'
    if 161 <= weather.get_wind()['deg'] <= 206:
        return 'южный'
    if 207 <= weather.get_wind()['deg'] <= 252:
        return 'юго-западный'
    if 253 <= weather.get_wind()['deg'] <= 298:
        return 'западный'
    if 299 <= weather.get_wind()['deg'] <= 339:
        return 'северо-западный'
print("Сегодня " + weather.get_reference_time('iso') + " погода в " + associateArray[rnd.get_location().get_name()] + " " + Clouds() + ' ,облачность составляет ' + str(weather.get_clouds()) + "% ,давление "  + str(weather.get_pressure()['press']*0.75) + " мм.рт.ст,температура " + str(weather.get_temperature('celsius')['temp']) + 'градусов Цельсия, ночью ' + str(weather.get_temperature('celsius')['temp_min']) +', днем ' + str(weather.get_temperature('celsius')['temp']) + ',ветер '+ str(weather.get_wind()['speed'])+'м/c,направление ' + Wind() )


