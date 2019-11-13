def count(myList,x):
    num=0
    #look through the list
    for i in myList:
        if i == x:
            num=num+1
    return num
print (count([1,2,1,1,3,4],1))
