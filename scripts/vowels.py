s= 'Anniee'
i=0
count=0
while i<len(s):
#if (s[i] == 'a'or s[i]=='e' or'i' or s[i]=='o' or s[i]=='u' or s[i]=='A'or s[i]=='E'or s[i]=='I'or s[i]=='O'or s[i]=='U'):
    if(s[i] in 'aeiouAEIOU'):
        count =count+1
    i=i+1
print('Number of vowels:'+' '+str(count))
    