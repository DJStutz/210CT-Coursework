#ask = list(input("Enter list of integers"))
import random
ask=[1,2,5,9,6,9,4,2,6,5,8,7,5,1,2,6,5,9,6] # 1
empty = [] # 1
print (len(ask)) # 1
while len(ask) > 0:
    rnd=random.randint(0,len(ask)-1) #BigO (N) Run time
    empty.append(ask[rnd])
    ask.pop(rnd)
print(empty)

#shuffle = [5,3,8,6,1,9,2,7]
#shuffle.insert(4,shuffle.pop(0))
#shuffle.insert(6,shuffle.pop(0))
#shuffle.insert(3,shuffle.pop(0))
#shuffle.insert(9,shuffle.pop(0))
#print(shuffle)
