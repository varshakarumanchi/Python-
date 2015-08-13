def sumDigits(N):
    num=N
    N=N/10
    if N==0:
        return num
    else:
        return num%10 + sumDigits(N)