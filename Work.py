#  File: Work.py 

#  Description: Figure out minimum v lines of code while getting maximum hours of sleep before collapsing (using linear & binary search)

#  Student Name: Hojung Kim

#  Student UT EID: hk25322

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 9/29 

#  Date Last Modified: 9/30 

import sys, time

# 1 <= n <= 10 ** 6
# 2 <= k <= 10 


def productivity(v,k):
  #first v number of lines & drink coffee = v // k
  #write & another drink of coffee = v // k ** 2
  #write & another drink of coffee = v // k ** 3
  # this will be expressed as v // k ** num_coffee 
  num_coffee = 0 
  progress = 0 
  #since he will collapse when 0 
  while v // k ** num_coffee > 0:
    progress += (v // k ** num_coffee)
    #will increase each time by 1
    num_coffee += 1 
  return progress


# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
  for i in range(0,n+1):
    if productivity(i,k) >= n:
      return i




# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
  # use binary search here
  low = 0
  high = n

  while low <= high:
    mid = (high + low) // 2
    
    #point is LOWER than number of codes -> low = mid + 1
    if productivity(mid, k) < n:  
      low = mid + 1

    #point is HIGHER than number of codes -> high = mid - 1 
    elif productivity(mid, k) > n:
      high = mid - 1

    #point is SAME -> mid 
    else:
      return mid
    
  return mid





# main has been completed for you
# do NOT change anything below this line
def main():
  num_cases = int((sys.stdin.readline()).strip())

  for i in range(num_cases):
    inp = (sys.stdin.readline()).split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()#  File: Work.py 
