#  File: Cipher.py

#  Description: Converting string into matrix, rotating the matrix, then converting matrix back to string

#  Student Name: Ho jung Kim 

#  Student UT EID: hk25322

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 9/10

#  Date Last Modified: 9/13


import sys
import math

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt ( strng ):
  L = len(strng)
  #M = smallest square number greater than or equal to L 
  K = int(math.ceil(math.sqrt(L)))
  #table size is M = K * K 
  M = K * K
  #add (M-L) asterisks to the message 
  for i in range (M-L):
    strng += '*' 
  matrix = [] 

  #convert string into matrix
  for i in range(K):
    row = []
    for j in range(K):
      row.append(strng[i * K + j])
    matrix.append(row)
  
  #rotate the matrix by 90 degrees
  rotated_matrix = [row[:] for row in matrix]
  for i in range(0,K):
    for j in range(0,K):
      rotated_matrix[j][K-1-i] = matrix[i][j]
  #return rotated_matrix
  
  #convert matrix into string
  return_strng = ''
  #row
  for i in range(K):
    #col
    for j in range(K):
      #if the corresponding point is '*', replace it with the next point
      if rotated_matrix[i][j] != '*':
        return_strng += rotated_matrix[i][j]
  return return_strng   



# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt (strng):
  L = len(strng)
  #M = smallest square number greater than or equal to L 
  K = int(math.ceil(math.sqrt(L)))
  #table size is M = K * K 
  M = K * K
  #add (M-L) asterisks to the message
  for i in range (M-L):
    strng += '*' 
  matrix = []

  #convert string into matrix
  for i in range(K):
    row = []
    for j in range(K):
      row.append(strng[i * K + j])
    matrix.append(row)

  #instead of rotating the matrix by 90 degrees counter clockwise, i'm going to rotate the matrix 90 degrees clockwise 3 times (TA told me that it's fine) 
  #first rotation
  clockwise_rotated = [row[:] for row in matrix]
  for i in range(K):
    for j in range(K):
      clockwise_rotated[j][K-1-i] = matrix[i][j]
  #return clockwise_rotated
  #second rotation 
  clockwise_rotated_again = [row[:] for row in clockwise_rotated]
  for i in range(K):
    for j in range(K):
      clockwise_rotated_again[j][K-1-i] = clockwise_rotated[i][j]
  #return clockwise_rotated_again
  #third rotation, which is equavalent to rotating the matrix 90 degrees counter clockwise 
  clockwise_rotated_last = [row[:] for row in clockwise_rotated_again]
  for i in range(K):
    for j in range(K):
      clockwise_rotated_last[j][K-1-i] = clockwise_rotated_again[i][j]
  #return clockwise_rotated_last
 
  #convert matrix into string
  return_strng = ''
  #row
  for i in range(K):
    #col
    for j in range(K):
      #if the corresponding point is '*', replace it with the next point
      if clockwise_rotated_last[i][j] != '*':
        return_strng += clockwise_rotated_last[i][j]
  return return_strng 



def main(): 
  # read the two strings P and Q from standard imput
  P = sys.stdin.readline().strip()
  Q = sys.stdin.readline().strip()
  # encrypt the string P
  encrypt_P = encrypt(P)
  # decrypt the string Q
  decrypt_Q = decrypt(Q)
  # print the encrypted string of P and the 
  # decrypted string of Q to standard out
  print(encrypt_P)
  print(decrypt_Q)


if __name__ == "__main__":
  main() 