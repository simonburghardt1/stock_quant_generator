import json
import csv
import os
import requests
import math


def find_cik(ticker):
    with open("ticker_cik.json") as file:
        parsed_json = json.load(file)

    for entry in parsed_json:
        if parsed_json[entry]["ticker"] == ticker:
            cik = str(parsed_json[entry]["cik_str"])
            while len(cik) < 10:
                cik = "0" + cik
            return cik


# Data Sources: sec edgar, yahoo finance
co_cik = find_cik("AAPL")
url = "https://data.sec.gov/submissions/CIK" + co_cik + ".json"

r = requests.get(
    url=url,
    headers={
        "User-Agent": "Mozilla/5.0 (Simon Burghardt Holding sb@simonburghardt.de)"
    },
).json()
print(r)
