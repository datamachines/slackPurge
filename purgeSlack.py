#!/usr/bin/python
import os
import requests
import json
from datetime import datetime, timedelta
import time

days_old = 7
cutoffDate = datetime.now() - timedelta(days=days_old)
cutoffEpoch = int(cutoffDate.strftime('%s'))

token = os.environ['SLACK_TOKEN']

payload = { 'token': token, 'count': 99999 }
url = 'https://slack.com/api/files.list'
r = requests.get(url, params=payload)
data = json.loads(r.text)
#print json.dumps(data, indent=2)
for sFile in data['files']:
    fileID = sFile['id']
    createdEpoch = int(sFile['created'])
    print fileID, createdEpoch
    if createdEpoch < cutoffEpoch:
        print "\t DELETING File:", fileID
        deletePayload = { 'token': token, 'file': fileID }
        url = 'https://slack.com/api/files.delete'
        r = requests.get(url, params=deletePayload)
        deleteResponse = json.loads(r.text)
        print json.dumps(deleteResponse)
        # https://api.slack.com/docs/rate-limits
        time.sleep(1)
