#  File: Hull.py

#  Description: With given points, create a convex hull and get the area of it 

#  Student Name: hojung kim

#  Student UT EID: hk25322

#  Partner Name: n/a

#  Partner UT EID: n/a 

#  Course Name: CS 313E

#  Unique Number: 52530 

#  Date Created: 9/25

#  Date Last Modified: 9/26

import sys
import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))
  
  #not equal 
  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  #lower than
  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  #lower and equal
  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  #greater than 
  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  #greater and equal 
  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
  #px  py
  #qx  qy
  #rx  ry
  #det = (x1 * y2 + x2 * y3 + ... + xn * y1 - y1 * x2 - y2 * x3 - ... - yn * x1)
  return p.x * q.y + q.x * r.y + r.x * p.y - p.y * q.x - q.y * r.x - r.y * p.x


# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
  upper_hull = []
  #append first two points p_1 and p_2 in order 
  upper_hull.append(sorted_points[0])
  upper_hull.append(sorted_points[1])
  #since p_1,p_2..p_n, n is going to be len(sorted_points) 
  for i in range(2,len(sorted_points)):
    #append p_i to upper_hull 
    upper_hull.append(sorted_points[i])
    #While upper_hull contains three or more points and the last three
    #points in upper_hull do not make a right turn
    #another way to solve; 
    #while len(upper_hull) >= 3:
    #  if det(upper_hull[-1],upper_hull[-2], upper_hull[-3]) > 0:
    #    upper_hull.pop(-2) 
    #QUESTION: why does -3,-2,-1 order matter?? 
    while len(upper_hull) >= 3 and det(upper_hull[-3],upper_hull[-2], upper_hull[-1]) >= 0:
      #delete the middle of last three points, which would be [-2]
      upper_hull.pop(-2) 
  
  lower_hull = []
  #append last two points in order
  lower_hull.append(sorted_points[-1])
  lower_hull.append(sorted_points[-2])
  #for i going from n-2 down to 1
  for i in range(len(sorted_points) - 2, -1, -1):
    lower_hull.append(sorted_points[i])
    #While lower_hull contains three or more points and the last three
    #points in the lower_hull do not make a right turn
    #USE WHILE NOT IF !!!
    while len(lower_hull) >= 3 and det(lower_hull[-3],lower_hull[-2], lower_hull[-1]) >= 0:
      lower_hull.pop(-2)
    
  #remove first and last point of lower_hull 
  lower_hull.pop(0) 
  lower_hull.pop(-1) 
    
  #append the points in the lower_hull to the points in the upper_hull 
  #and call those points the convex_hull
  convex_hull = upper_hull 
  for points in lower_hull: 
    convex_hull.append(points)
 

  #return the convex_hull 
  return convex_hull

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
#area = (1/2) * abs (det)
def area_poly (convex_poly):
  convex_poly.append(convex_poly[0]) 
  #for i in range(len(convex_poly) - 1): 
    #return (1/2) * abs(p.x * q.y + q.x * r.y + r.x * p.y - p.y * q.x - q.y * r.x - r.y * p.x)
    #using i; 
    #det = sum((p.x * q.y) - (p.y * q.x))
  for_det = 0 
  for i in range(len(convex_poly)-1): 
    for_det += sum([((convex_poly[i].x * convex_poly[i + 1].y) - (convex_poly[i].y * convex_poly[i + 1].x))])
  area = (1/2) * abs(for_det) 

  return area 

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases
  #test square.in
  assert convex_hull([(0,4),(4,0),(0,0),(1,2),(0,3),(3,2),(4,4)]) == [(0,0),(0,4),(4,4),(4,0)]
  #test triangle.in
  assert convex_hull([(0,8),(0,0),(8,0),(3,2),(0,7),(1,4)]) == [(0,0),(0,8),(8,0)]
  #test square.in 
  assert convex_hull([(0,10),(0,0),(10,0),(10,10),(0,7),(1,4),(5,5),(6,6),(8,0)]) == [(0,0),(0,10),(10,10),{10,0}]

  return "all test cases passed"

def main():
  # create an empty list of Point objects
  points_list = []

  # read number of points
  line = sys.stdin.readline()
  line = line.strip()
  num_points = int(line)

  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    x = int (line[0])
    y = int (line[1])
    points_list.append(Point(x, y))

  # sort the list according to x-coordinates
  points_list.sort(key = lambda point:(point.x)) 
  sorted_points = sorted(points_list)
  #points_list.sort(key = lambda point:(point.x)) 


  '''
  # print the sorted list of Point objects
  for p in sorted_points:
    print (str(p))
  '''

  # get the convex hull
  final_convex_hull = convex_hull(sorted_points) 

  # run your test cases
  #print(test_cases())

  # print your results to standard output
  # print the convex hull
  print("Convex Hull") 
  for m in final_convex_hull:
    print(m) 

  # get the area of the convex hull
  area_of_convex_hull = area_poly(final_convex_hull)
  print() 

  # print the area of the convex hull
  print("Area of Convex Hull =", area_of_convex_hull)



if __name__ == "__main__":
  main()