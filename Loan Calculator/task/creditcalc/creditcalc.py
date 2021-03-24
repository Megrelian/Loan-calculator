import math
import argparse

parse = argparse.ArgumentParser()
parse.add_argument("-t", "--type", choices=["diff", "annuity"], help="please enter type. example diff, or annuity" )
parse.add_argument("-pa", "--payment", type=float)
parse.add_argument("-pr", "--principal", type=float)
parse.add_argument("-pe", "--periods", type=int)
parse.add_argument("-i", "--interest", type=float)
arg = parse.parse_args()
all_parameters = [arg.type, arg.payment, arg.principal, arg.periods, arg.interest]


def check_for_arguments_count():
    x = 0
    for value in all_parameters:
        if value is not None:
            x += 1
    return x

if arg.type == "diff" and arg.principal is not None and arg.periods is not None and arg.interest is not None:
    inte = arg.interest /(12 * 100)
    pr = arg.principal
    n = arg.periods
    d3 = 0
    for i in range(1, arg.periods + 1):
        d1 =pr / n + inte * (pr - (pr * (i-1)) / n)
        d2 = int(math.ceil(d1))
        d3 += d2
        print(f"Month {i}: payment is {d2}")

    print(f"\noverpayment {int(d3 - pr)}")

elif arg.type == "annuity" and arg.principal is not None and arg.periods is not None\
        and arg.interest is not None and arg.payment is None:
        loan_principal = arg.principal
        periods = arg.periods
        interest = arg.interest
        i = interest / (12 * 100)
        a = (i * (1+i) ** periods) / ((1+i)**periods - 1)
        monthly_payment = math.ceil(loan_principal * a)
        print(f"Your annuity payment = {monthly_payment}!")
        overpayment = monthly_payment * periods - loan_principal
        print(f"\n overpayment {int(overpayment)}")

elif arg.type == "annuity" and arg.periods is not None and arg.payment is not None\
        and arg.interest is not None and arg.principal is None:

    annuity_payment = arg.payment
    periods = arg.periods
    interest = arg.interest
    i = interest / (12 * 100)
    a = (i * (1 + i) ** periods) / ((1 + i) ** periods - 1)
    loan_principal = math.floor(annuity_payment / a)
    print(f"Your loan principal = {int(loan_principal)}!")
    overpayment = periods * annuity_payment - loan_principal
    print(f"\noverpayment {int(overpayment)}")

elif arg.type == "annuity" and arg.principal is not None and arg.payment is not None\
        and arg.interest is not None and arg.periods is None:
    loan_principal = arg.principal
    monthly_payment = arg.payment
    interest = arg.interest
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
    overpayment = n * monthly_payment - loan_principal
    print(f"\n overpayment {int(overpayment)}")
else:
    print("Incorrect parameters")

































# print(arg)
#
# choose = input()
#
# if choose == "n":
#     loan_principal = float(input("Enter the loan principal:\n"))
#     monthly_payment = float(input("Enter the monthly payment:\n"))
#     interest = float(input("Enter the loan interest:\n"))
#     i = interest / (12 * 100)
#     lg = monthly_payment / (monthly_payment - i * loan_principal)
#     base = 1 + i
#     n = math.ceil(math.log(lg, base))
#
#     if n == 12:
#         print("It will take 1 year to repay this loan!")
#     elif n < 12:
#         print(f"It will take {n} months to repay this loan!")
#     else:
#         year = n // 12
#         month = n % 12
#         if month == 0:
#             print(f"It will take {year} years to repay this loan!")
#         else:
#             print(f"It will take {year} years and {month} months to repay this loan!")
#
# elif choose == "a":
#     loan_principal = float(input("Enter the loan principal:\n"))
#     periods = float(input("Enter the number of periods:\n"))
#     interest = float(input("Enter the loan interest:\n"))
#     i = interest / (12 * 100)
#     a = (i * (1+i) ** periods) / ((1+i)**periods - 1)
#     monthly_payment = math.ceil(loan_principal * a)
#     print(f"Your monthly payment = {monthly_payment}!")
#
# elif choose == "p":
#     annuity_payment = float(input("Enter the annuity payment:\n"))
#     periods = float(input("Enter the number of periods:\n"))
#     interest = float(input("Enter the loan interest:\n"))
#     i = interest / (12 * 100)
#     a = (i * (1 + i) ** periods) / ((1 + i) ** periods - 1)
#     loan_principal = round(annuity_payment / a)
#     print(f"Your loan principal = {loan_principal}!")
