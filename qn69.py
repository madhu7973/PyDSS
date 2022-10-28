import math
def is_perfect_square(x):
 
    #if x >= 0,
    if(x >= 0):
        sr = int(math.sqrt(x))
        # sqrt function returns floating value so we have to convert it into integer
        #return boolean T/F
        return ((sr*sr) == x)
    return False
 
# Driver code
x = 101
if (is_perfect_square(x)):
    print("True")
else:
    print("False")