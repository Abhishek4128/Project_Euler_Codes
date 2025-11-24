
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math
lcm=1
for i in range(1,21):
    lcm=lcm*i//math.gcd(lcm,i)
print(lcm)