

    

def isin(myList,x):
    for i in myList:
        if i==x:
            return True
        
    return False
print (isin([1,2,1,1,3,4],3))
