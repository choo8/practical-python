    # pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            try:
                _, num_shares, price = row
                total_cost += int(num_shares) * float(price)
            except ValueError as e:
                print(f'Row {rowno}: Bad row: {row}')

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f"Total cost {cost:.2f}")