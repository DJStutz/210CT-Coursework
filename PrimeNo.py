def primez(n, n2):
#Recursive #BigO (N)
    while n2 >= 2: #BigO (N)
        if n % n2 == 0:  #Base case 
            print ("This is a prime number")
            return False
        else:
            return primez(n, n2-1) #Calling itself
    else:
        print ("This number is not a prime number")
        return 'True'

primez(7,3)
primez(5,4)
primez(6,5)


def PRIMEZ(N,N2)
    while n2 >= 2
        if n % n2 = 0
            print is prime
            return False
        else
            return PRIMEZ(N. N2-1)
    else
        print not prime
        return True
            
