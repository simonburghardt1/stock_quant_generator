import json
import csv
import os
import requests
import yfinance as yf
import datetime
import statistics
import math

stock = yf.Ticker("DKNG")


# takes in price history, returns a list of dicts with price history and w/w returns
# REWRITE
def get_weekly_returns(price_history):
    counter = 0
    prices = []
    for index, row in price_history.iterrows():

        if counter == 0:
            entry = {
                "Date": index,
                "Close": round(float(row["Close"]), 2),
                "w/w": float(0),
            }

        else:
            ww = (float(row["Close"]) / (float(prices[counter - 1]["Close"]))) - 1
            ww = round(float(ww) * 100, 2)
            entry = {"Date": index, "Close": round(float(row["Close"]), 2), "w/w": ww}

        prices.append(entry)
        counter = counter + 1
    return prices


def isolate_ww(price_history):
    ww_returns = []
    counter = 0
    last_weeks_row = 0

    for index, row in price_history.iterrows():

        if counter == 0:
            ww = float(0)
        else:
            ww = (float(row["Close"]) / (float(last_weeks_row["Close"]))) - 1
            ww = round(float(ww) * 100, 2)

        last_weeks_row = row
        ww_returns.append(ww)
        counter = counter + 1
    return ww_returns


# Kurtosis and skewness missing
def descriptive_statistics(ww_list):
    return {
        "mean": statistics.mean(ww_list),
        "sterr": statistics.stdev(ww_list) / math.sqrt(len(ww_list)),
        "median": statistics.median(ww_list),
        "mode": statistics.mode(ww_list),
        "standard dev": statistics.stdev(ww_list),
        "variance": statistics.variance(ww_list),
        "kurtosis": 0,
        "skewness": 0,
        "minimum": min(ww_list),
        "maximum": max(ww_list),
        "range": max(ww_list) - min(ww_list),
        "count": len(ww_list),
    }


# get historical market data
hist = stock.history(period="max", interval="1wk").drop(
    columns=["Open", "High", "Low", "Volume", "Dividends", "Stock Splits"]
)
# calculate weekly returns
weekly_returns = isolate_ww(hist)
# calculate descriptive statistics
desciptive_stats = descriptive_statistics(weekly_returns)


# show share count
stock.get_shares_full(start="2022-01-01", end=None)

# show financials:
# - income statement
# stock.income_stmt
# stock.quarterly_income_stmt
# - balance sheet
# .balance_sheet
# stock.quarterly_balance_sheet
# - cash flow statement
# stock.cashflow
# stock.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options

# show holders
# stock.major_holders
# stock.institutional_holders
# stock.mutualfund_holders
# stock.insider_transactions
# stock.insider_purchases
# stock.insider_roster_holders

# show recommendations
# stock.recommendations
# stock.recommendations_summary
# .upgrades_downgrades


# show news
# stock.news
