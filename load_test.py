import requests
import ast
import os
import time

IFFTT_KEY = "AAGQ57iePd71iPLT6qJth"#os.environ.get('IFFTT_KEY')
URL =  "https://www.google.com/"#os.environ.get('URL')
#HEADERS = os.environ.get('HEADERS')
#headers = ast.literal_eval(HEADERS)

for j in range(5):
    for i in range(5):
        resp = requests.get(URL, verify=False)#, headers=headers)

        if resp.status_code==503 or "organization" in str(resp.content) or "organisation" in str(resp.content):
            requests.get("https://maker.ifttt.com/trigger/train_website_crash/with/key/"+IFFTT_KEY)
            break
        print("Executed ", resp.status_code)
        time.sleep(5)
    time.sleep(60) 

