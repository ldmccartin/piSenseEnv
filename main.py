import schedule
import time
from SensorClass import EnvSenseData
from getEnvSenseData import grab_data
from checkForStickEvent import run_display
from runThreaded import run_threaded

MyEnvClass = EnvSenseData()
schedule.every(0.5).seconds.do(run_threaded, MyEnvClass.store_data)


while True:
    schedule.run_pending()
    print(MyEnvClass.get_data())
    run_threaded(run_display)
    time.sleep(2.5)

'''
MyFile=open('output.txt','w')
MyFile.writelines(my_list)
MyFile.close()
'''
