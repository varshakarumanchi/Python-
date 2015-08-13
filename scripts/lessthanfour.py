def lessThan4(aList):
    bList=[]
    count=0
    for element in aList:
        if len(element)<4:
          bList.append(element)  
    return bList
aList=["ape", "cat", "dog", "ba"]
print(lessThan4(aList))