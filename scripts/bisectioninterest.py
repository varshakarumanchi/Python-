'''program that uses upper and lower bounds and bisection search to find the smallest monthly payment to the cent such that we can pay off the debt within a year
'''
balance=999999
annualInterestRate=0.18
lowerbound=balance/12.0
upperbound=(balance+(balance*annualInterestRate))/12.0
lowestpayment=(lowerbound+upperbound)/2.0
unpaid=balance-lowestpayment
while True:
    b=balance
    for month in range(1,13):
        unpaid=b-lowestpayment
        Interest=(unpaid*annualInterestRate)/12.0
        b=unpaid+Interest
    if unpaid>(-0.01) and unpaid<0:
        break
    elif unpaid>0:
        lowerbound=lowestpayment
        lowestpayment=(lowerbound+upperbound)/2
    else:
        upperbound=lowestpayment
        lowestpayment=(lowerbound+upperbound)/2
print("Lowest Payment: "+str(round(lowestpayment,2)))