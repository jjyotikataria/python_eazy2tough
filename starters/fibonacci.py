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
  

--------------------------------------------------------------------------------------------------------------------------------------------------- 
  ## Explanation:  
  
  # First lets forget about the loop, most of us know that we need to put some loop here, but lets learn to make a pseudocode here of what we want. We want first two numbers to be present first of all because fibo series will start from 0 and 1 right? If you don't understand, watch this out this  # https://www.mathsisfun.com/numbers/fibonacci-sequence.html#:~:text=It%20is%20that%20simple!,out%20the%20next%20few%20numbers%3F
  
  
  
  # Now comes the third no. which has to be the sum of the first two so lets just put third = first + second
  
  #so, lets put some code here
    first = 0
    second = 1
    print(first)
    print(second)
    third = first + second
    print(third)
   
  # This will give us the third number, how about getting the fourth no. and so on..! We need to write that again and again, that now my second no. becomes my first and my third no. becomes my second. To avoid writing that multiple times, lets use a while loop here. Why not for loop? Because we don't have a range to mention here, as our question is not restricted till a certain number, lets work with while which takes into account a certain condition.
  
  # So, how many times a loop should run, we need to think that and put that restriction for while loop! Considering n =3 we want 0,1,1 as the output since 0 and 1 are already initialized we want now the loop to run one time for getting three fibo numbers, so looks like the loop runs n-2 times for a particular n. Thats it! 
  
  
  
