# Problem 1

import pandas as pd

import numpy as np

threes = np.arange(start=1,stop=1000,step=3)

# essentially gives us an array of every multiple of 3 from 1-1000

fives = np.arange(start=1,stop=1000,step=5)

# same process as before, except with multiples of 5

# can then just find the total sum of each array and add the two values together to get the answer
sum(sum(threes),sum(fives))


# Problem 2

