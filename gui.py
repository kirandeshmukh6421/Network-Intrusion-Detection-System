import os
import time
from tkinter import *
from tkinter import messagebox
from datetime import datetime

# <-----------------------------------WORKING-----------------------------------> #

EC2_IP = "65.0.18.127"

def today():
    datetime_obj = datetime.now()
    date = datetime_obj.date()
    return date

def start():
    if email_input.get():
        email = email_input.get()
        with open(f'CICIDS/Emails/{today()}_{email}.txt', 'w') as file:
            pass
        time.sleep(3)
        os.system(
            f'start cmd /c ssh -i "awskeypair.pem" ssh -i "awskeypair.pem" ubuntu@ec2-65-0-18-127.ap-south-1.compute.amazonaws.com "mkdir /home/ubuntu/Nokia/flows/{email} && touch /home/ubuntu/Nokia/flows/{email}/{today()}_{email}.txt"')
        os.system(
            f"start cmd /c scp -i awskeypair.pem CICIDS/CICFlowMeter/bin/data/daily/{today()}_Flow.csv ubuntu@{EC2_IP}:/home/ubuntu/Nokia/flows/{email}/{today()}_Flow.csv && scp -i awskeypair.pem CICIDS/Emails/{today()}_{email}.txt ubuntu@{EC2_IP}:/home/ubuntu/Nokia/flows/{email}/{today()}_{email}.txt")
        os.system(
            f'start cmd /k ssh -i "awskeypair.pem" ubuntu@ec2-65-0-18-127.ap-south-1.compute.amazonaws.com "python3 /home/ubuntu/Nokia/monitor.py {email}"')
        time.sleep(5)
        os.system('start cmd /k python monitor.py ' + email)
    else:
        messagebox.showwarning(
            "Warning", "Please make sure to enter your email.")
# && scp -i awskeypair.pem CICIDS/Emails/{today()}_{email}.txt ubuntu@{EC2_IP}:/home/ubuntu/Nokia/flows/{email}/{today()}_{email}.txt
# <-------------------------------------UI-------------------------------------> #


BLUE = "#caf0f8"
# Screen Setup
root = Tk()
root.resizable(0, 0)
# Set position of window on screen
root.geometry('+%d+%d' % (430, 120))
root.title(" NIDS")
# root.minsize(width=500, height=500)
root.config(padx=50, pady=30, bg=BLUE)
root.iconbitmap('NIDS.ico')

# Adding Image
canvas = Canvas(root, width=128, height=128,
                bg=BLUE, highlightthickness=0)
img = PhotoImage(file="NIDS.png")
canvas.create_image(64, 64, image=img)
canvas.grid(row=0, column=1, pady=(0, 30), padx=(0, 65))

# Email Input
email_label = Label(root, text="Email: ", font=(
    "Montserrat", 10), bg=BLUE, highlightthickness=0)
email_label.grid(row=3, column=0)
email_input = Entry(root)
email_input.grid(row=3, column=1, columnspan=2, sticky=W+E+N, padx=5, pady=5)

# Username Input
username_label = Label(root, text="Username: ", font=(
    "Montserrat", 10), bg=BLUE, highlightthickness=0)
username_label.grid(row=4, column=0)
username_input = Entry(root)
username_input.grid(row=4, column=1, columnspan=2,
                    sticky=W+E+N, padx=5, pady=5)

# Save Button
save_btn = Button(root, text="Start IDS", font=(
    "Montserrat", 7, "bold"), command=start)
save_btn.grid(row=6, column=1, columnspan=2, sticky=W+E, padx=5, pady=5)

root.mainloop()
