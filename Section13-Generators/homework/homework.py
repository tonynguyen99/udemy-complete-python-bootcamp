# Problem 1
def gensquares(N):
    for number in range(N):
        yield number**2

for x in gensquares(10):
    print(x)

# Problem 2
import random

def rand_num(low,high,n):
    
    for number in range(n):
        yield random.randint(low,high)
    
for num in rand_num(1,10,12):
    print(num)

    
# Problem 3
s = 'hello'

s_iter = iter(s)
next(s_iter)