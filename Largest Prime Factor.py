import math
num =600851475143
largest_prime=0

for i in range(3, int(math.sqrt(num))+1, 2):
    while num%i==0:
        if i>largest_prime:
            largest_prime=i
            
        num=num/i

print(largest_prime)      
