'''program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
'''
balance=3926
annualInterestRate=0.2
fixedmonthlypayment=0
unpaid=balance-fixedmonthlypayment
while unpaid>0:
    b=balance
    fixedmonthlypayment=fixedmonthlypayment+10
    for month in range(1,13):
        unpaid=b-fixedmonthlypayment
        Interest=(unpaid*annualInterestRate)/12
        b=unpaid+Interest
print("Lowest Payment: "+str(fixedmonthlypayment))