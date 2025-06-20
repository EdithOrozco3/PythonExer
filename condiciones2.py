
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

if n % 2 != 0:
        # Condition 1: If n is odd
        print("Weird")
else:
    # n is even, now check the ranges
    if 2 <= n <= 5:
        # Condition 2: If n is even and in the range of 2 to 5
        print("Not Weird")
    elif 6 <= n <= 20:
        # Condition 3: If n is even and in the range of 6 to 20
        print("Weird")
    elif n > 20:
        # Condition 4: If n is even and greater than 20
        print("Not Weird")