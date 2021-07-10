def modInverse(a, m): #taken from internet
    m0 = m
    y = 0
    x = 1
 
    if (m == 1):
        return 0
 
    while (a > 1): 
        # q is quotient
        q = a // m 
        t = m
 
        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y
 
        # Update x and y
        y = x - q * y
        x = t
 
    # Make x positive
    if (x < 0):
        x = x + m0
 
    return x

def power(x, y, p) : #taken from internet
    res = 1     # Initialize result
 
    # Update x if it is more
    # than or equal to p
    x = x % p 
     
    if (x == 0) :
        return 0
 
    while (y > 0) :
         
        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1) :
            res = (res * x) % p
 
        # y must be even now
        y = y >> 1      # y = y/2
        x = (x * x) % p
         
    return res

    
p = 19807040628566084398385987581
y1 = 11226815350263531814963336315
y2 = 9190548667900274300830391220
y3 = 4138652629655613570819000497

y1inv = modInverse(y1, p)
y2inv = modInverse(y2, p)
y3inv = modInverse(y3, p)

a = 9189
m1 = (y3*y1inv)%p

b = 2021
m2 = (y2*y1inv)%p

while a > 1: #this is the loop for euclidean lemma
    q = a//b
    temp = b
    b = a%b
    a = temp
    
    temp = m1
    m1 = m2
    m2 = (temp * power((modInverse(m2, p)), q, p))%p

g = m1
x = (modInverse(power(g, 324, p), p)*y1)%p
print("g = ", g)
print("x = ", x)
