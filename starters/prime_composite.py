## Checking whether an inputted number is prime or not, this one took me less time to figure out! Lets first prompt the user for entering the number first!


num = input("Enter a number")
x  = range(1, num//2)
count = 0

for i in x:
  if(num % i) == 0:
    count += 1

if(count > 1):
  print("Number is composite!!!")
else:
  print("Number is prime")
    

----------------------------------------------------------------------------------------------------------
# Explanation:
## While taking the input in python, we need to be sure that whats the datatype of input being taken into account, lets say here we want the input to be taken 

