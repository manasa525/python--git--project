def isPerfectSquare(x):
 
    
    if(x >= 0):
        sr = math.sqrt(x)
        
    
        return ((sr*sr) == float(x))
    return false
 

 
 
x = 2502
if (isPerfectSquare(x)):
    print("Yes")
else:
    print("No")
 