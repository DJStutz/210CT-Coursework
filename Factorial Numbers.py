def fact(x): #Finds Factorial
    if (x >1): #1 BigO
        return x * fact(x-1)
    else:
        return 1

print (fact(15))

def count (x): #Counts trailing 0s
    i = 5
    zeros = 0
    while x / i >= 1: #N BigO 
        zeros += x // i
        i *= 5
    return zeros

print(count(15))











