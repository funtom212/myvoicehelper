import datetime
import pyowm

def get_time():
    now = datetime.datetime.now()
    return "сейчас " + str(now.hour) + ":" + str(now.minute)

def tell_joke():
    return 'Британскими учеными установлено, что спать четыре часа в сутки несложно, Сложнее не спать остальные двадцать.'

def say_hi():
    return 'здравствуйте, сэр'

def trigger():
    return 'triggered'

def i_not_understand():
    return 'я вас не понимаю'

def i_m_ok():
    return 'у меня всё хорошо спасибо'

def weather() :
    owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc',language="ru") 
    observation = owm.weather_at_place('Нижний Новгород')
    w = observation.get_weather()
    return "сейчас в Нижнем Новгроде " + w.get_detailed_status() + ",на улице," + str(int(w.get_temperature('celsius')['temp'])) + ",градуса цельсия"

def well_done():
    return 'спасибо, сэр'