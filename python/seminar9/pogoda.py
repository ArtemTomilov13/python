from pyowm import OWM

 
owm = OWM('9042f06879c292fdb0f3af4517ebfa99')
mgr = owm.weather_manager()
 
 
observation = mgr.weather_at_place('Moscow, RU')
w = observation.weather
 
print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9