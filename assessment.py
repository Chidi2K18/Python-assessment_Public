import math
import random
import numpy as np
nums = []
#solution for non repeating numbers
def grid_test(width, height):
    count_of_increments = 1
    count_of_groups = 0
    greatest_sum = 0
    current_sum = []

    test_array = np.random.randint(1, 100, size=(height, width))
    test = test_array.flatten()

    for i in test:
        current_sum.append(i)
        count_of_increments += 1
        if count_of_increments == 3: #count in lists of 3
            count_of_increments -= 3
            count_of_groups += 1
            if len(current_sum) <= 2: #first list often has 2 elements
                current_sum.clear()
            elif len(current_sum) == 3: #ensure that only groups of 3 are taken into consideration
                if sum(current_sum) > greatest_sum: #check if the current sum is the greatest available
                    greatest_sum = sum(current_sum)
                    current_sum.clear()
    print("The number of groups of 3 = " + str(count_of_groups))
    print("The greatest sum available = " + str(greatest_sum))

grid_test(100,100)
