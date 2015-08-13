'''program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
'''
balance=5000
annualInterestRate=0.18
monthlyPaymentRate=0.02
totalpaid=0
for month in range(1,13):
    min_payment=balance*monthlyPaymentRate
    totalpaid=totalpaid+min_payment
    balance=balance-min_payment
    interest=(balance*annualInterestRate)/12
    balance=balance+interest
    print("month: "+str(month))
    print("Minimum monthly payment: "+str(round(min_payment,2)))
    print("Remaining balance: "+str(round(balance,2)))
print("Total paid: "+str(round(totalpaid,2)))
print("Remaining balance: "+str(round(balance,2)))
    