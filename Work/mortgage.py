# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
cur_month = 1

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if extra_payment_start_month <= cur_month and cur_month <= extra_payment_end_month:
        cur_payment = payment + extra_payment
    else:
        cur_payment = payment
    cur_payment = min(cur_payment, principal * (1+rate/12))
    principal = principal * (1+rate/12) - cur_payment
    total_paid = total_paid + cur_payment
    print(f"{cur_month} {total_paid:.2f} {principal:.2f}")
    cur_month += 1

print(f'Total paid {total_paid:.2f}')
print(f'Months {cur_month - 1}')