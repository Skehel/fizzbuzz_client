import requests
import json
import argparse

def get_fizzbuzz_paginated(page_number, integers_per_page):
    url = "http://localhost:4000/fizzbuzz"
    params = {"page": page_number, "integers_per_page": integers_per_page}
    response = requests.get(url, params=params)
    if response.status_code == 201:
        return response.json()
    else:
        print("Error:", response.text)

def add_fav_number(number):
    url = "http://localhost:4000/fav_number"
    headers = {"Content-Type": "application/json"}
    payload = {"number": number}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        return response.json()["favourites"]
    else:
        print("Error:", response.text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--page", type=int, help="page number for get_fizzbuzz_paginated function")
    parser.add_argument("-i", "--integers", type=int, help="number of integers per page for get_fizzbuzz_paginated function")
    parser.add_argument("-n", "--number", type=int, help="number to add to favourites list for add_fav_number function")
    args = parser.parse_args()

    if args.page and args.integers:
        results = get_fizzbuzz_paginated(args.page, args.integers)
        print(results)

    if args.number:
        fav_numbers = add_fav_number(args.number)
        print(fav_numbers)