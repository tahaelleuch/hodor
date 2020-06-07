#!/usr/bin/python3
import requests

url = "http://158.69.76.135/leve0.php"
my_vote = {
    "id": "1444",
    "holdthedoor": "Submit"
}

for i in range(0, 1024):
    requests.post(url, data=my_vote)

print("Done!")
