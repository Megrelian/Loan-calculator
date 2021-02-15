import math
print("Enter the loan principal:")
principal = int(input())
print("What do you want to calculate?")
print("type 'm' for number of monthly payments,\ntype 'p' for the monthly payment")
what_to_calculate = input()
if what_to_calculate == "m":
    montly_payment = int(input("Enter the monthly payment:\n"))
    number_of_month = round(principal / montly_payment)
    if number_of_month > 1:
        print(f"It will take {number_of_month} months to repay the loan")
    else:
        print(f"It will take {number_of_month} month to repay the loan")
elif what_to_calculate == "p":
    number_of_month = int(input("Enter the number of months: \n"))
    monthly_payment = math.ceil(principal / number_of_month)
    last_month = principal - (number_of_month -1) * monthly_payment
    print(f"Your monthly payment = {monthly_payment} and the last payment = {last_month}.")