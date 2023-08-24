
import sys

class Link (object):
  def __init__ (self, coeff = 1, exp = 1, next = None):
    self.coeff = coeff
    self.exp = exp
    self.next = next

  def __str__ (self):
    return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
  def __init__ (self):
    self.first = None

  # create a string representation of the polynomial
  def __str__ (self):
    curr = self.first 
    string = '' 
    if curr == None:
        return string
    
    while curr != None: 
        if curr.next != None:
            string += '(' + str (curr.coeff) + ', ' + str (curr.exp) + ') + '
        else:
            string += '(' + str (curr.coeff) + ', ' + str (curr.exp) + ')'
        curr = curr.next

    return string 


    


  # keep Links in descending order of exponents
  def insert_in_order (self, coeff, exp):
    new_linked = Link(coeff, exp)
    curr = self.first
    prev = self.first 

    #if the LinkedList is empty
    if self.first is None:
      new_linked.next = curr
      curr = new_linked
      self.first = new_linked
    
    else: #when LinkedList is not empty 
    #when the exponent is smaller than the current exponent, x^4 > x^5
      while curr != None and exp <= curr.exp:
        #tranverse until a smaller exponent is found 
          prev = curr
          curr = curr.next
          #if curr is empty, it's going to be added at end 
          if curr == None: 
            prev.next = new_linked 
      #when it's not empty and current is self.first, 
      if curr == self.first:
          new_linked.next = curr
          self.first = new_linked
      #when it's not empty and current is not self.first,
      else:
        prev.next = new_linked
        new_linked.next = curr

  # add polynomial p to this polynomial and return the sum
  #using reference from geeksforgeeks.org (adding two polynomials using linkedlist)
  def add (q, p): 
    new_list = LinkedList()
    q_curr = q.first
    p_curr = p.first  

    while q_curr is not None or p_curr is not None:
        #if all of q is added
        if q_curr is None:
            while p_curr is not None:
                new_list.insert_in_order(p_curr.coeff, p_curr.exp)
                p_curr = p_curr.next
        #if all of q is added
        if p_curr is None:
            while q_curr is not None:
                new_list.insert_in_order(q_curr.coeff, q_curr.exp)
                q_curr = q_curr.next
        #if neither are fully added
        if p_curr is not None and q_curr is not None:
            if q_curr.exp == p_curr.exp:
                new_coeff = int(q_curr.coeff) + int(p_curr.coeff)
                if new_coeff != 0:
                    new_list.insert_in_order(new_coeff, q_curr.exp)
                q_curr = q_curr.next
                p_curr = p_curr.next
            elif q_curr.exp > p_curr.exp:
                new_list.insert_in_order(q_curr.coeff, q_curr.exp)
                q_curr = q_curr.next
            else:
                new_list.insert_in_order(p_curr.coeff, p_curr.exp)
                p_curr = p_curr.next

    return new_list   
 
  # multiply polynomial p to this polynomial and return the product
  #when multiplying, you have to add each of the exponents as well
  #also not just adding the ones that has the same exponents but all of them 
  def mult (q, p):
    new_list = LinkedList()
    q_curr = q.first
    p_curr = p.first  
    list_of_lists = list()
    combined = LinkedList()

    #creates and fills lists of the distributive property products
    while q_curr is not None:
        while p_curr is not None:
            new_coeff = int(q_curr.coeff) * int(p_curr.coeff)
            new_exp = int(q_curr.exp) + int(p_curr.exp)
            new_list.insert_in_order(new_coeff, new_exp)
            p_curr = p_curr.next
        list_of_lists.append(new_list)
        new_list = LinkedList()
        p_curr = p.first
        q_curr = q_curr.next

    #adds the distributively calculated lists together
    for i in range(len(list_of_lists)):
        combined = combined.add(list_of_lists[i])

    return combined

def main():
  # read data from file poly.in from stdin
  linked = sys.stdin.readline()
  linked = linked.strip()
  num = int (linked)
  #print(num)

  # create polynomial p

  p = LinkedList()
  list_of_links = list()
  for i in range (num):
    linked = sys.stdin.readline().strip().split()
    list_of_links.append(linked)

  idxs = list()
  combined_list = list()
  for i in range(len(list_of_links)):
    for j in range(len(list_of_links)):
        if list_of_links[i][1] == list_of_links[j][1]:
            idxs.append(j)
    coeff_sum = 0
    #add coeff at the idxs where exp is the same
    for num in idxs:
        coeff_sum += int(list_of_links[num][0])
    combined_list.append((coeff_sum, list_of_links[i]))
    idxs.clear()

  sums = list()
  final_list = list()

  for i in range(len(combined_list)):
    #dont want to add duplicates of same expo
    if (combined_list[i][0], combined_list[i][1][1]) not in sums:
        sums.append((combined_list[i][0], combined_list[i][1][1]))
        final_list.append((combined_list[i][0],combined_list[i][1][1]))

  #creates q polynomial if the coeff of final list is not 0
  for i in range(len(final_list)):
    if final_list[i][0] != 0:
        p.insert_in_order(int(final_list[i][0]), int(final_list[i][1]))

  # create polynomial q
  blank = sys.stdin.readline()
  q = LinkedList()
  linked = sys.stdin.readline()
  linked = linked.strip()
  num = int (linked)
  list_of_links = list()
  for i in range (num):
    linked = sys.stdin.readline().strip().split()
    list_of_links.append(linked)

  idxs = list()
  combined_list = list()
  for i in range(len(list_of_links)):
    for j in range(len(list_of_links)):
        if list_of_links[i][1] == list_of_links[j][1]:
            idxs.append(j)
    coeff_sum = 0
    for num in idxs:
        coeff_sum += int(list_of_links[num][0])
    combined_list.append((coeff_sum, list_of_links[i]))
    idxs.clear()

  sums = list()
  final_list = list()
  for i in range(len(combined_list)):
    if (combined_list[i][0], combined_list[i][1][1]) not in sums:
        sums.append((combined_list[i][0], combined_list[i][1][1]))
        final_list.append((combined_list[i][0],combined_list[i][1][1]))

  for i in range(len(final_list)):
    if final_list[i][0] != 0:
        q.insert_in_order(int(final_list[i][0]), int(final_list[i][1]))

  # get sum of p and q and print sum
  sum = q.add(p)
  print (sum)

  # get product of p and q and print product
  product = p.mult(q)
  print(product)

if __name__ == "__main__":
  main()
