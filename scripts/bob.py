'''program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
'''
s = 'azcbobobobeggbobhakl'
count=0
i=0
while i<len(s)-2:
    if (s[i]=='b' and s[i+1]=='o' and s[i+2]=='b'):
        count=count+1
    i=i+1
print('Number of times bob occurs is:'+' '+str(count))