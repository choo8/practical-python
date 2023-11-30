# report.py
#
# Exercise 2.4
import csv
import sys

def read_portfolio(filename):
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            holding = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            portfolio.append(holding)

    return portfolio

def read_prices(filename):
    prices = {}

    with open(filename, "rt") as f:
        rows = csv.reader(f)

        for row in rows:
            if row != []:
                prices[row[0]] = float(row[1])

    return prices

def make_report(portfolio, prices):
    report = []

    for share in portfolio:
        report.append((share["name"], int(share["shares"]), float(prices[share["name"]]), float(prices[share["name"]]) - float(share["price"])))

    return report

if len(sys.argv) == 3:
    portfolio_filename, prices_filename = sys.argv[1], sys.argv[2]
else:
    portfolio_filename, prices_filename = "Data/portfolio.csv", "Data/prices.csv"

portfolio = read_portfolio(portfolio_filename)
prices = read_prices(prices_filename)

cost = 0
market_value = 0

for share in portfolio:
    cost += share["shares"] * share["price"]
    market_value += share["shares"] * prices[share["name"]]

print(f"Current value {market_value:.2f}")
print(f"Gain {market_value - cost:.2f}")

report = make_report(portfolio, prices)

print("      Name     Shares      Price      Change")
print("---------- ---------- ---------- -----------")

for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {f"${price:.2f}":>10} {change:>10.2f}')