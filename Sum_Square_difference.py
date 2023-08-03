import math

print("Enter sum of squares natural numeber")
n= int(input())

print("Enter the sum of the natural number")
m= int(input())

sum_of_squares= n*(n+1)*(2*n+1)/6

sum_natural_number=m*(m+1)/2

ans= sum_natural_number*sum_natural_number - sum_of_squares

print(ans)
