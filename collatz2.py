# Copyright 2024 Robert Destefano

#define collatz function
def collatz(x):
    #when x = 1 appear , loop break
    while(x!=1):
      if(x%2==0):
          x=x//2
          list1.append(x)
      else:
          x=3*x+1
          list1.append(x)


#User input:
lower_limit=int(input("Enter a natural number 2 or greater for the lower limit:"))
upper_limit=int(input("Enter a larger natural number for the upper limit:"))
upper_limit+=1

# main program
import time
start_time = time.time()
for x in range(lower_limit,upper_limit):
  list1=[]
  n=collatz(x)
  if list1[-1]!=1:
    print("The following list does not end with 1")
    print("\n The input number is:",x)
    print("\n The Collatz sequence is:")
    print(list1)
  else:
    continue
end_time = time.time()
elapsed_time = end_time - start_time

#Output for else argument
print("all lists within the range from",lower_limit,"to",upper_limit-2, "ended with 1")
print("Elapsed time:", elapsed_time, "seconds")
print("--------------")
print("Copyright 2024 Robert Destefano")