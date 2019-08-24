import time
from sense_hat import SenseHat

sense = SenseHat()

def grab_data():
    grab_enviro_sensors = {
        "time": time.strftime('%a-%d-%b-%Y %H:%M:%S GMT', time.localtime()),
        "temp": sense.get_temperature(),
        "humidity": sense.get_humidity(),
        "pressure": sense.get_pressure()
    }
    
    return (grab_enviro_sensors)
