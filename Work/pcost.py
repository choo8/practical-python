# pcost.py
#
# Exercise 1.27
import csv

def portfolio_cost(filename):
    total_cost = 0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                _, num_shares, price = row
                total_cost += int(num_shares) * float(price)
            except ValueError as e:
                print(e)

    return total_cost

cost = portfolio_cost("Data/portfolio.csv")
print(f"Total cost {cost:.2f}")