import time 
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from apscheduler.schedulers.background import BackgroundScheduler
import os
import sys

def today():
    datetime_obj = datetime.now()
    date = datetime_obj.date()
    return date

sched = BackgroundScheduler()
EC2_IP = "65.0.18.127"

def send_file():
    print(sys.argv[1])
    os.system(f"scp -i awskeypair.pem CICIDS/CICFlowMeter/bin/data/daily/{today()}_Flow.csv ubuntu@{EC2_IP}:/home/ubuntu/Nokia/flows/{sys.argv[1]}/{today()}_Flow.csv")

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Created file: {event.src_path}") 
        
    def on_modified(self, event):
        print(f'Modified file : {event.src_path}')

# Folder Monitor
observer = Observer()
event_handler = MyHandler() 
observer.schedule(event_handler, path='CICIDS/CICFlowMeter/bin/data/daily')
observer.start()

# File Monitor
observer2 = Observer()
event_handler2 = MyHandler()
observer2.schedule(event_handler2, path=f"CICIDS/CICFlowMeter/bin/data/daily/{today()}_Flow.csv", recursive=False)
observer2.start()

sched.add_job(send_file, 'interval', seconds=15)
sched.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    sched.shutdown()
    observer.stop()

observer.join()