# Problem 1

import pandas as pd

import numpy as np

threes = np.arange(start=3,stop=1000,step=3)

# essentially gives us an array of every multiple of 3 from 1-1000

fives = np.arange(start=5,stop=1000,step=5)

# same process as before, except with multiples of 5

# can then just find the total sum of each array and add the two values together to get the answer
sum(threes)+sum(fives)

# Problem 2

fibo = [1,2]
# generates the Fibonacci sequence up until a value exceeds 4 million
while True:
    fibo.append(fibo[-1]+fibo[-2])
    if fibo[-1]>4000000:
        break

even_fibo = filter(lambda a: a % 2 ==0,fibo)

sum(even_fibo)


# Question 3

def find_factors(x):
    f_list = []
    for i in range(1,x+1):
        if x % i == 0:
            f_list.append(i)
    np.asarray(f_list)
    return(f_list)

factors_of_12 = find_factors(12)

def am_prime(y):
    p_list = find_factors(y)
    if len(p_list)<=2:
        print("prime")
    else:
        print("composite")

prob_3 = find_factors(600851475143)


def some_prime_factors(z):
    x_list = []
    for i in range(z,z+1):
        if z % i == 0:
            x_list.append(i)
    np.asarray(x_list)
    return(x_list)

pri_list = find_factors(600851475143)