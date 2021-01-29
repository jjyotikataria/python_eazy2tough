## We are writing a program to generate "n" numbers from fibonacci series

def fibo(n):
  prev = 0
  curr = 1
  i=0
  print(prev)
  print(curr)

  while(i < n-2):
    next = prev + curr
    print(next)
    prev = curr
    curr = next 
    i += 1
  
