#!/usr/bin/env python3
"""
A simple script to query https://icanhazdadjoke.com/api every 15 seconds for 60 seconds
"""

import time

import argparse
import requests

DAD_JOKE_BASE_URL = "https://icanhazdadjoke.com"
HEADERS = {"Accept": "application/json"}

def tell_joke(joke: str) -> None:
    print(joke)
    time.sleep(1)

def random_dad_joke() -> str:
    req = requests.get(DAD_JOKE_BASE_URL, headers=HEADERS)
    req_json = req.json()
    return req_json["joke"]

def random_query_loop(number: int) -> None:
    i = 0
    while i < number: 
        dad_joke = random_dad_joke()
        tell_joke(dad_joke)
        i += 1

def search_dad_jokes(search: str, page: int = 1, limit: int = 20) -> list[dict]:
    req = requests.get(f"{DAD_JOKE_BASE_URL}/search?page={page}&term={search}&limit={limit}", headers=HEADERS)
    req_json = req.json()
    return req_json["results"]

def search_query_loop(search: str, number: int, page: int) -> int:
    dad_jokes = search_dad_jokes(search, page=page, limit=number)
    page += 1

    length = len(dad_jokes)
    if length < number:
        page = 1
        dad_jokes += search_dad_jokes(search, page=page, limit=number-length)

    for dad_joke in dad_jokes:
        tell_joke(dad_joke["joke"])
    
    return page

def main(search: str, number: int) -> None:
    i = 0
    page = 1
    while i <= 60:
        if search:
            page = search_query_loop(search, number, page)
        else:
            random_query_loop(number)
    
        i += 15

        # Don't need to wait on the last loop
        if i < 60:
            print("--------------------------------------------------------------------------------------")
            time.sleep(5)

    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Also how to handle if number > 40, the API limit? Just error out?
    parser.add_argument("-n", "--number", help="The number of dad jokes to return in each set. Default is 1. Must be between 1 and 40.", default=1, type=int)
    parser.add_argument("-s", "--search", help="A search term to look up", type=str)
    args = parser.parse_args()

    if args.number > 0 and args.number <= 40: 
        main(args.search, args.number)
    else:
        print(f"You have entered an invalid number {args.number}. Please select a new number between 1 and 40")