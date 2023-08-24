
#  File: Radix.py

#  Description: Find the maximum since we have to go through each digit then sort through each digit 

#  Student Name: hojung kim

#  Student UT EID: hk25322

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 10/23

#  Date Last Modified: 10/24

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings

#find the maxiumum from a and its length 
def max_str (a):
  max_a = max(a, key = len)
  length_max = len(max_a)
  return length_max 

def radix_sort (a):
  #empty list
  sort_list = []
  sorted = [] 
  #get the maximum length from the above 
  length_max = max_str(a) 
  #change all numbers and alphabets into numbers
  #DO NOT PUT END AS 36, it's 0 
  sorting = {'0':0, '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10, 'b':11,'c':12,'d':13,'e':14,'f':15,'g':16,'h':17,'i':18,'j':19,'k':20,'l':21,'m':22,'n':23,'o':24,'p':25,'q':26,'r':27,'s':28,'t':29,'u':30,'v':31,'w': 32,'x':33,'y':34,'z':35,'^':0}

  #numbers 0-9, 10 numbers
  #alphabet a-z, 26 alphabets
  #10+26 = 36
  #so the range would be 1,37
  for i in range(1,37):
    sort_list.append(Queue())

  for i in range(len(a)):
    #empty = length_max - len(a[i])
    #if empty >= 0: 
    while len(a[i]) < length_max:
      #add '^' to make the string size the same 
      #will be removed at the end 
      a[i] += '^'
      

  
  for j in range(length_max):
    for i in a:
      added = [] 
      each = len(i) - j - 1
      queue_sort = sorting[i[each]]
      #enqueue = insert at the end
      (sort_list[queue_sort]).enqueue(i) 
      if queue_sort >= len(i):
        i = 0 
      else: 
        pass
      
    #add it to the list 
    #dequeue from the sort_list[i] and then add it to the list 
    for i in range(0,36):
      while sort_list[i].is_empty() != True:
        #dequeue = remove from front
        added.append(sort_list[i].dequeue())
    #updated a 
    a = added[:]
    

  
  #remove the '^', giving the final list without the '^' 
  #easy way is to use replace() 
  for i in a:
    #sorted.append(i+''.join(""))
    #sorted.remove('^')
    sorted.append(i.replace('^',""))
  return sorted



def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  '''
  # print word_list
  print (word_list)
  '''

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()
