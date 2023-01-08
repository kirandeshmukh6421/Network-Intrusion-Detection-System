import os
import sys
from datetime import datetime
import smtplib

def today():
    return datetime.now().date()

print("Checking for intrusion...")
import em
import numpy as np
import pandas as pd
from datetime import datetime
from warnings import simplefilter
import joblib
import warnings
import os

warnings.filterwarnings("ignore")
simplefilter(action='ignore', category=FutureWarning)

def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)

unwanted = ['Flow ID', 'Src IP', 'Src Port', 'Dst IP', 'Protocol', 'Timestamp', 'Label']
test_dataset = clean_dataset(pd.read_csv(f"/home/ubuntu/Nokia/flows/{sys.argv[1]}/{today()}_Flow.csv").drop(unwanted, axis=1))
X_test = test_dataset.iloc[:, :]
classifier = joblib.load('/home/ubuntu/Nokia/model')

from collections import Counter
intrusion = Counter(classifier.predict(X_test))[0.0]
file = open(f"/home/ubuntu/Nokia/flows/{sys.argv[1]}/{today()}_{sys.argv[1]}.txt", "r+")
email_sent = file.read().strip()
print(email_sent)
if(intrusion>=10 and email_sent==""):
    s = smtplib.SMTP('smtp.gmail.com', 587)  
    s.starttls()
    s.login("andallarmy007@gmail.com", "mzkhjprmrzutezsn")
    message = "Intrusion detected in your network!"        
    s.sendmail("andallarmy007@gmail.com", sys.argv[1], message)     
    s.quit()
    file.write("0")
file.close()
print(Counter(classifier.predict(X_test)))
