#!/usr/bin/env python3
"""
A simple script to query https://icanhazdadjoke.com/api every 15 seconds for 60 seconds
"""

import time

import argparse
import requests

DAD_JOKE_BASE_URL = "https://icanhazdadjoke.com"
HEADERS = {"Accept": "application/json"}

def random_dad_joke() -> str:
    req = requests.get(DAD_JOKE_BASE_URL, headers=HEADERS)
    req_json = req.json()
    return req_json["joke"]

def search_dad_jokes(search: str, page: int = 1, limit: int = 20) -> list[dict]:
    req = requests.get(f"{DAD_JOKE_BASE_URL}/search?page={page}&term={search}&limit={limit}", headers=HEADERS)
    req_json = req.json()
    return req_json["results"]

def main(search: str, number: int) -> None:
    i = 0
    page = 1
    while i <= 60:
        j = 0
        while j < number: 
            if search:
                dad_jokes = search_dad_jokes(args.search, page=page, limit=number)
                page += 1

                length = len(dad_jokes)
                if length < number:
                    print("In length < number")
                    page = 1
                    dad_jokes += search_dad_jokes(args.search, page=page, limit=number-length)

                for dad_joke in dad_jokes:
                    print(dad_joke["joke"])
                j += number
            else:
                dad_joke = random_dad_joke()
                print(dad_joke)
                j += 1
    
        i += 15
        time.sleep(5)
        print("")

    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", help="The number of dad jokes to return in each set", type=int, default=1)
    parser.add_argument("-s", "--search", help="A search term to look up", type=str)
    args = parser.parse_args()

    main(args.search, args.number)