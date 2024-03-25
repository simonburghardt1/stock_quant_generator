import json
import csv
import os
import requests
import math
from sec_edgar_api import EdgarClient


def find_cik(ticker):
    with open("ticker_cik.json") as file:
        parsed_json = json.load(file)

    for entry in parsed_json:
        if parsed_json[entry]["ticker"] == ticker:
            cik = parsed_json[entry]["cik_str"]
            return cik


# Data Sources: sec edgar, yahoo finance
co_cik = find_cik("ELF")


edgar = EdgarClient(user_agent="Simon Burghardt Holding; sb@simonburghardt.de")
facts = edgar.get_company_facts(cik=co_cik)


with open("data.json", "w", encoding="utf-8") as f:
    json.dump(facts, f, ensure_ascii=False, indent=4)
