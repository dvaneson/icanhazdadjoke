#!/usr/bin/env python3
"""
A simple script to query https://icanhazdadjoke.com/api every 15 seconds for 60 seconds
"""

import json
import requests

DAD_JOKE_URL = "https://icanhazdadjoke.com/"
DAD_JOKE_HEADERS = {"Accept": "application/json"}

def random_dad_joke():
    req = requests.get(DAD_JOKE_URL, headers=DAD_JOKE_HEADERS)
    # print(json.dumps(req.json()))
    print(req.text)

if __name__ == "__main__":
    random_dad_joke()