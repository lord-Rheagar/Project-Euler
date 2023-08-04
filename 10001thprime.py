print("Enter the nth Prime number")
n=int(input())
count=0
prime_number=2

def is_prime(num):
     for i in range(2, int(num/2)+1):
         if num%i==0:
             return False
             break
         
     return True
             
     
while count<n:
    
    if is_prime(prime_number)==True:
        count+=1
        
    prime_number+=1    
        
print(prime_number-1)
