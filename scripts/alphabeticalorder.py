'''program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print beggh'''
#s='abcab'
s='yusspzxzhdombirzj'
s1=s[0]
for i in range(len(s)-2):
    s2=s[i]
    for j in range(len(s)-1):
        if(s[j]<=s[j+1]):
            s2=s2+s[j+1]
            if(len(s2)>len(s1)):
                s1=s2
        else:
            s2=s[j+1]
print('Longest substring in alphabetical order is: '+s1)