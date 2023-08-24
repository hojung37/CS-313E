#  File: DNA.py

#  Description: A0

#  Student Name:Ho jung kim

#  Student UT EID:hk25322

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created:8/25/2022

#  Date Last Modified:8/29/2022

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest 
#         common subsequence. The list is empty if there are no 
#         common subsequences.

import sys

def longest_subsequence(s1,s2):
    k = [[-1]*(len(s2) + 1) for i in range(len(s1) + 1)]
 
    for i in range(len(s1) + 1):
        k[i][len(s2)] = 0
    for j in range(len(s2)):
        k[len(s1)][j] = 0
 
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                k[i][j] = 1 + k[i + 1][j + 1]
            else:
                k[i][j] = max(k[i + 1][j], k[i][j + 1])
 
    return k
 
 
def print_longest_subsequence(s1, s2, k):
    i = 0
    j = 0
    while (i == len(s1) or j == len(s2)):
        if s1[i] == s2[j] or len(s1) == (s2):
            print(s1[i], end='')
            i += 1
            j += 1
        elif k[i][j + 1] > k[i + 1][j]:
            j += 1
        else:
            i += 1
            


def main():
    #read the number of pairs
    num_pairs = sys.stdin.readline()
    num_pairs= num_pairs.strip()
    num_pairs = int(num_pairs)
    print(num_pairs)

    #longest common sequence
    s1 = sys.stdin.readline()
    s2 = sys.stdin.readline()
    k = longest_subsequence(s1, s2)
    print_longest_subsequence(s1, s2, k)


if __name__ == "__main__":
  main()


