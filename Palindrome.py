#  File: Palindrome.py
 
#  Description: Create the shortest palindrome by taking the last character of the string and adding it to the beginning if it is not already a palindrome 

#  Student Name: Hojung Kim

#  Student UT EID: hk25322

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 10/2

#  Date Last Modified: 10/3

import sys


# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the smallest palindrome that can be 
#         made by adding characters to the start of the input string
def smallest_palindrome(str):
  input_string = 0
  #if the input is already a palindrome, return the same 
  if input_string == len(str):
    return str 
  #i in range reverse of string
  for i in range(len(str)-1, -1, -1):
    #if the reversed string is same as the string 
    if (str[i] == str[input_string]):
      input_string += 1




  reverse_string = str[::-1]
  #check if input string starts with reversed string
  if str[:input_string-1] == reverse_string[(len(str) - input_string):len(str) - 1]:
    # take the last character that is needed to make it a palindrome and add it to the beginning
    # cbabcde reverse is edcbabc; ed is the remainder and this will be added to the beginning of cbabcde
    # 0 to the part that overlaps 
    last_char = reverse_string[0:len(str) - input_string]
    return last_char + str




# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases
  assert smallest_palindrome('ccg') == ('gccg')
  assert smallest_palindrome('baaba') == ('abaaba')
  assert smallest_palindrome('doodle') == ('eldoodle')

  return "all test cases passed"

def main():
    #str = int((sys.stdin.readline()).strip())
    #res = smallest_palindrome(str) 

    # run your test cases
    '''
    print (test_cases())
    '''

    for line in sys.stdin:
      #print the smallest
      print(smallest_palindrome(line.strip()))

    # read the data

    # print the smallest palindromic string that can be made for each input

if __name__ == "__main__":
  main()