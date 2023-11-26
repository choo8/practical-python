# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    total_cost = 0

    with open(filename, "rt") as f:
        lines = f.readlines()
        for line in lines[1:]:
            try:
                _, num_shares, price = line.strip().split(",")
                total_cost += int(num_shares) * float(price)
            except ValueError as e:
                print(e)

    return total_cost

cost = portfolio_cost("Data/portfolio.csv")
print(f"Total cost {cost:.2f}")