import os
import sys
import time 
from apscheduler.schedulers.background import BackgroundScheduler
sched = BackgroundScheduler()
print("Checking")

def run_model():
    os.system(f"python3 /home/ubuntu/Nokia/predict.py {sys.argv[1]}")

sched.add_job(run_model, 'interval', seconds=25)
sched.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    sched.shutdown()

