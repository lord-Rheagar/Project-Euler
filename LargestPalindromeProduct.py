def is_palindrome(n):
    return str(n)==str(n)[::-1]

large_num=999
small_num=100
largest_palindrome=0

for i in range(large_num, small_num-1, -1):
    for j in range(i, small_num-1,-1):
        product = i*j
        if(is_palindrome(product) and product>largest_palindrome):
            largest_palindrome=product



print(largest_palindrome)
