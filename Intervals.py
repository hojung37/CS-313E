#  File: Intervals.py

#  Description: Merging intervals that are overlapping each other 

#  Student Name: Ho jung Kim 

#  Student UT EID: hk25322

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 9/6

#  Date Last Modified: 9/9

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
import sys

def merge_tuples(tuples_list):
  #sorting tuples_list
  intervals = sorted(tuples_list)
  #empty list for merge_interval 
  merging_int = []
  for i in range(len(intervals)-1):
    #if end of first interval is greater than first of second interval 
    if intervals[i][1] >= intervals [i+1][0]:
      #replace second interval to start of first interval and max of end of second interval
      intervals[i+1] = (intervals[i][0], max(intervals[i][1],intervals[i+1][1]))
    else: 
      merging_int.append(intervals[i])
  #add the last interval outside of the for loop since it is not included inside the for loop 
  merging_int.append(intervals[i+1])
    
  return merging_int

# Input: tuples_list is a list of tuples denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size(tuples_list):
  #get the absolute value of the difference between start and end of the interval and sort it 
  interval_size = sorted(tuples_list, key = lambda x: abs(x[1]-x[0]))
  return interval_size

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  # write your own test cases
  assert merge_tuples([(1,2)]) == [(1,2)]
  #merge overlapping intervals 
  assert merge_tuples([(1,3),(2,4),(3,7),(8,10)]) == [(1,7),(8,10)]
  assert merge_tuples([(13,18),(14,17),(16,20),(23,30)]) == [(13,20),(23,30)]

  # write your own test cases
  assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
  #sort by interval size by calculating the absolute value of the difference between start and end of the interval 
  assert sort_by_interval_size([(2,4),(-3,-10),(4,13),(8,9)]) == [(8,9),(2,4),(-3,-10),(4,13)]
  assert sort_by_interval_size([(-3,-13),(14,15),(20,22),(7,15)]) == [(14,15),(20,22),(7,15),(-3,-13)]


  return "all test cases passed"
    


def main():
  # open file intervals.in and read the data and create a list of tuples

  # merge the list of tuples

  # sort the list of tuples according to the size of the interval

  # run your test cases
  '''
  print (test_cases())
  '''
  # write the output list of tuples from the two functions

  num_tuples = int(sys.stdin.readline().strip())
  tuples_list = []
  for i in range(num_tuples):
    #strip and split the lines from intervals.in file
    a = sys.stdin.readline().strip().split(' ')
    num1, num2 = a
    #change num1 and num2 into an interval 
    x = int(num1)
    y = int(num2)
    t = (x,y)
    tuples_list.append(t)
  merging_int = merge_tuples(tuples_list) 
  print(merging_int)
  print(sort_by_interval_size(merging_int))




if __name__ == "__main__":
  main()

