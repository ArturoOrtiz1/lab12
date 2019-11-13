def index(myList,x):
    
    for i in range(len(myList)):
        #return position
        if x==myList[i]:
            return i
        
    return None


print (index([1,2,1,1,3,4],3))
