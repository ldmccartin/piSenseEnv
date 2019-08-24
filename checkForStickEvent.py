from sense_hat import SenseHat
from runThreaded import run_threaded
from getEnvSenseData import grab_data
from printToSenseLCD import message_print

sense = SenseHat()

def run_display():
    event = sense.stick.get_events()
    if len(event) > 0:
        if event[0].direction == "middle" and event[0].action == "pressed":
            run_threaded(message_print(grab_data()["temp"],"temperature", [255,0,0]))
        elif event[0].direction == "up" and event[0].action == "pressed":
            message_print(grab_data()["humidity"],"humidity", [0,255,0])
        elif event[0].direction == "down" and event[0].action == "pressed":
            message_print(grab_data()["pressure"], "pressure", [0,0,255])
