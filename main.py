import schedule
import time
from SensorClass import EnvSenseData
from getEnvSenseData import grab_data
from checkForStickEvent import run_display
from runThreaded import run_threaded

MyEnvClass = EnvSenseData()
schedule.every(30).seconds.do(run_threaded, MyEnvClass.store_data)
schedule.every(15).seconds.do(run_threaded, MyEnvClass.print_data)


while True:
    schedule.run_pending()
    run_threaded(run_display)
    time.sleep(1)
