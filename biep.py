import time
import schedule

def sound():
    print("Biep!")

schedule.every().minute.at(":00").do(sound)

while True:
    schedule.run_pending()
    time.sleep(1)
