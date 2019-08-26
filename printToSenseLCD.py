from sense_hat import SenseHat
from getEnvSenseData import grab_data

sense = SenseHat()

# Takes 3 params (float, string, list)
def message_print(sensor_data, sensor_data_type, text_colour_rgb):
    print(grab_data()["time"])
    print(sensor_data_type + " : ", end="")
    print(float("{0:.1f}".format(sensor_data)), end="")
    sense.set_rotation(0)
    sense.show_message(str(float("{0:.1f}".format(sensor_data))), 0.05 ,text_colour_rgb)
    print("\n")
