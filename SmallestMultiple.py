import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def smallest_divisible_by_range(limit):
    result = 1
    for i in range(2, limit + 1):
        result = lcm(result, i)
    return result

# Example usage for finding the smallest number divisible by numbers from 1 to 20:
smallest_number = smallest_divisible_by_range(20)
print("The smallest positive number divisible by all numbers from 1 to 20 is:", smallest_number)
