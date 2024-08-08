#!/usr/bin/env python3
"""
A simple script to query https://icanhazdadjoke.com/api every 15 seconds for 60 seconds
"""

import time

import argparse
import requests

DAD_JOKE_BASE_URL = "https://icanhazdadjoke.com"
HEADERS = {
    "Accept": "application/json",
    "User-Agent": "My Library (https://github.com/dvaneson/icanhazdadjoke)"    
}

def tell_joke(joke: str) -> None:
    # Print the joke and give a small delay before the next joke is told
    print(joke)
    time.sleep(.1)

def random_dad_joke() -> str:
    req = requests.get(DAD_JOKE_BASE_URL, headers=HEADERS)
    if req.status_code == 200:
        req_json = req.json()
        return req_json["joke"]
    else:
        # If the request fails for some reason, wait a second and try again
        time.sleep(1)
        return random_dad_joke()

def search_dad_jokes(search: str, page: int = 1, limit: int = 20) -> list[dict]:
    req = requests.get(f"{DAD_JOKE_BASE_URL}/search?page={page}&term={search}&limit={limit}", headers=HEADERS)
    req_json = req.json()
    return req_json["results"]


def search_query_loop(search: str, number: int, page: int) -> int:
    # Search for dad jokes based on the term, up to the number specified
    dad_jokes = search_dad_jokes(search, page=page, limit=number)
    page += 1

    # If the number of jokes requested was not met, keep querying until the number has been hit
    length = len(dad_jokes)
    while length < number:
        page = 1
        dad_jokes += search_dad_jokes(search, page=page, limit=number-length)
        length = len(dad_jokes)

    for dad_joke in dad_jokes:
        tell_joke(dad_joke["joke"])
    
    return page

def main(search: str, number: int) -> None:
    # Repeat the loop after the interval (time in seconds), until the total time has been reached
    i = 0
    interval = 15
    total = 60

    # For tracking the page number with search results 
    page = 1

    while i <= total:
        # If a search term was specified, use it, otherwise get n random jokes
        if search !="" or number > 1:
            page = search_query_loop(search, number, page)
        else:
            dad_joke = random_dad_joke()
            tell_joke(dad_joke)
    
        i += interval
        # Don't need to wait on the last loop
        if i <= total:
            print("--------------------------------------------------------------------------------------")
            time.sleep(interval)

    return

if __name__ == "__main__":
    # Configuring CLI arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", help="The number of dad jokes to return in each set. Default is 1. Must be between 1 and 40.", default=1, type=int)
    parser.add_argument("-s", "--search", help="A search term to look up", default="", type=str)
    args = parser.parse_args()

    # Validate the number arg
    if args.number > 0 and args.number <= 40: 
        main(args.search, args.number)
    else:
        print(f"ERROR: You have entered an invalid number, {args.number} \nPlease select a new number between 1 and 40")