import math

print("""
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
""")

choose = input()

if choose == "n":
    loan_principal = float(input("Enter the loan principal:\n"))
    monthly_payment = float(input("Enter the monthly payment:\n"))
    interest = float(input("Enter the loan interest:\n"))
    i = interest / (12 * 100)
    lg = monthly_payment / (monthly_payment - i * loan_principal)
    base = 1 + i
    n = math.ceil(math.log(lg, base))

    if n == 12:
        print("It will take 1 year to repay this loan!")
    elif n < 12:
        print(f"It will take {n} months to repay this loan!")
    else:
        year = n // 12
        month = n % 12
        if month == 0:
            print(f"It will take {year} years to repay this loan!")
        else:
            print(f"It will take {year} years and {month} months to repay this loan!")

elif choose == "a":
    loan_principal = float(input("Enter the loan principal:\n"))
    periods = float(input("Enter the number of periods:\n"))
    interest = float(input("Enter the loan interest:\n"))
    i = interest / (12 * 100)
    a = (i * (1+i) ** periods) / ((1+i)**periods - 1)
    monthly_payment = math.ceil(loan_principal * a)
    print(f"Your monthly payment = {monthly_payment}!")

elif choose == "p":
    annuity_payment = float(input("Enter the annuity payment:\n"))
    periods = float(input("Enter the number of periods:\n"))
    interest = float(input("Enter the loan interest:\n"))
    i = interest / (12 * 100)
    a = (i * (1 + i) ** periods) / ((1 + i) ** periods - 1)
    loan_principal = round(annuity_payment / a)
    print(f"Your loan principal = {loan_principal}!")
