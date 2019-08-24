import schedule
from printHello import print_hello
from checkForStickEvent import run_display
from runThreaded import run_threaded
            
schedule.every(0.5).seconds.do(run_threaded, print_hello)

while True:
    schedule.run_pending()
    run_threaded(run_display)
