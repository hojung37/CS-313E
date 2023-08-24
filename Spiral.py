#  File: Spiral.py

#  Description: Infinite Spiral of Numbers

#  Student Name: Ho jung Kim 

#  Student UT EID: hk25322

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 8/30

#  Date Last Modified: 9/2

import sys
# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
# create a spiral starting from the center 
def create_spiral ( n ):
    spiral = [[0] * n for x in range(n)]
    spiral[n//2][n//2] = 1
    count = 2
    m = n//2
    # move around box that is m distance from the center
    for i in range(1, m + 1):
        for j in range(m - i + 1, m + i + 1):
            spiral[j][m + i] = count
            count += 1
        count -= 1
        for j in range(m + i, m - i, -1):
            spiral[m + i][j] = count
            count += 1
        for j in range (m + i, m - i - 1, -1):
            spiral[j][m - i] = count
            count += 1
        count -= 1
        for j in range (m - i, m + i + 1):
            spiral[m - i][j] = count
            count += 1
    return spiral

# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
# add the numbers around n that are in the spiral 
def sum_adjacent_numbers (spiral, n):
    s = len(spiral)
    sum = 0
    for i, j in enumerate(spiral):
        if n in j:
            row = i
            col = j.index(n)
    if n > s ** 2: 
        return 0 
    else: 
        if row != 0:
            sum += spiral[row-1][col]
        if row != s-1:
            sum += spiral[row+1][col]
        if col != 0:
            sum += spiral[row][col-1]
        if col != s-1:
            sum += spiral[row][col+1]
        if row != 0 and col != 0:
            sum += spiral [row-1][col-1]
        if row != 0 and col != s-1:
            sum += spiral [row-1][col+1]
        if row != s-1 and col != 0:
            sum += spiral [row+1][col-1]
        if row != s-1 and col != s-1:
            sum += spiral[row+1][col+1]
        return sum



def main():
    # read the input file
    n = int(sys.stdin.readline())
    # create the spiral
    spiral = create_spiral(n)
    val = []
    for i in sys.stdin.readlines():
        val.append(int(i.strip()))
    # add the adjacent numbers
    # print the result
    for i in val:
        print(sum_adjacent_numbers(spiral, i))
    

if __name__ == "__main__":
    main()