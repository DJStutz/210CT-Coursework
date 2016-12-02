def rec(n, i):
    value="" #1 BigO Runtime
    if i<len(b)-1:
        value=rec(n,i+1)
    return value+" "+n[i]
a="awesome is This"
b=a.split(' ')
print(rec(b,0))

#BigO Runtime 1

value <- empty value
if i < length of b then - 1
    value <- REC
return value
a <- user input
b <- function to reverse string
print REC
