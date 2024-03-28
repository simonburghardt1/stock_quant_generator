import json
import csv
import os
import requests
import yfinance as yf
import datetime

msft = yf.Ticker("DKNG")

# get historical market data
hist = msft.history(period="max", interval="1wk").drop(
    columns=["Open", "High", "Low", "Volume", "Dividends", "Stock Splits"]
)

counter = 0
prices = []
for index, row in hist.iterrows():

    if counter == 0:
        entry = {"Date": index, "Close": round(float(row["Close"]), 2), "w/w": 0}

    else:
        ww = (float(row["Close"]) / (float(prices[counter - 1]["Close"]))) - 1
        ww = round(float(ww) * 100, 2)
        entry = {"Date": index, "Close": round(float(row["Close"]), 2), "w/w": ww}

    prices.append(entry)
    counter = counter + 1


# show share count
msft.get_shares_full(start="2022-01-01", end=None)

# show financials:
# - income statement
# msft.income_stmt
# msft.quarterly_income_stmt
# - balance sheet
# .balance_sheet
# msft.quarterly_balance_sheet
# - cash flow statement
# msft.cashflow
# msft.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options

# show holders
# msft.major_holders
# msft.institutional_holders
# msft.mutualfund_holders
# msft.insider_transactions
# msft.insider_purchases
# msft.insider_roster_holders

# show recommendations
# msft.recommendations
# msft.recommendations_summary
# .upgrades_downgrades


# show news
# msft.news
