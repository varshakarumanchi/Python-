def keysWithValue(aDict, target):
    keys=aDict.keys()
    alist=[]
    values=aDict.values()
    for i in keys:
        if aDict[i]==target:
            alist.append(i)
    return alist
aDict={1:0,2:5,7:5}
print(keysWithValue(aDict, 5))