a=0 
b = 2
t = 2
s = 0
n=4000000

while t <= n:
    s+= t;
    t = a + 4 * b;
    a = b;
    b = t;
  
print(s)
