import math
import sys

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
    return f'({self.x}, {self.y}, {self.z})'
  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
    return math.hypot(self.x - other.x, self.y - other.y, self.z - other.z)
  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    tol = 1.0e-6
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol)) 
class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
    self.center = Point(x,y,z)
    self.radius = float(radius)
  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
    return f'Center: ({self.center.x}, {self.center.y}, {self.center.z}), Radius: {self.radius}'
  # compute surface area of Sphere
  # returns a floating point number
  def get_sphere_coord(self):
    min_x = self.center.x - self.radius
    max_x = self.center.x + self.radius
    min_y = self.center.y - self.radius
    max_y = self.center.y + self.radius
    min_z = self.center.z - self.radius
    max_z = self.center.z + self.radius
    range_x = (min_x, max_x)
    range_y = (min_y, max_y)
    range_z = (min_z, max_z)
    self.range_x = range_x
    self.range_y = range_y
    self.range_z = range_z
  def area (self):
    return 4.0 * float(math.pi) * (float(self.radius) ** 2)
  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
    return (4.0 / 3.0) * math.pi * (float(self.radius) ** 3)
  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
    self.get_sphere_coord()
    if p.x > self.range_x[0] and p.x < self.range_x[1] and p.y > self.range_y[0] and p.y < self.range_y[1] and p.z > self.range_z[0] and p.z < self.range_z[1]:
      return True
    return False
  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
    dist_centers = self.center.distance(other.center)
    return (dist_centers + other.radius) < self.radius
  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    self.get_sphere_coord()
    a_cube.get_cube_coord()
    if a_cube.range_x[0] > self.range_x[0] and a_cube.range_x[1] < self.range_x[1] and a_cube.range_y[0] > self.range_y[0] and a_cube.range_y[1] < self.range_y[1] and a_cube.range_z[0] > self.range_z[0] and a_cube.range_z[1] < self.range_z[1]:
      return True
    return False
  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):
    dist_centers = self.center.distance(a_cyl.center)
    return (dist_centers + a_cyl.radius) < self.radius and (dist_centers + (a_cyl.height / 2.0) < self.radius) 
  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
    return
  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):
    return
  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
    circ_cube = Cube(self.center.x, self.center.y, self.center.z)
    #share the same center
    circ_cube.side = (2.0 * float(self.radius) / math.sqrt(3))
    #largest size of the cube, diagonal of the cube should go through the center of the sphere
    return circ_cube
class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
    self.center = Point(x, y, z)
    self.side = float(side)
  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__ (self):
    return f'Center: ({self.center.x}, {self.center.y}, {self.center.z}), Side: {self.side}'
  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def get_cube_coord(self):
    min_x = self.center.x - (self.side / 2)
    max_x = self.center.x + (self.side / 2)
    min_y = self.center.y - (self.side / 2)
    max_y = self.center.y + (self.side / 2)
    min_z = self.center.z - (self.side / 2)
    max_z = self.center.z + (self.side / 2)
    range_x = (min_x, max_x)
    range_y = (min_y, max_y)
    range_z = (min_z, max_z)
    self.range_x = range_x
    self.range_y = range_y
    self.range_z = range_z
  def area (self):
    return 6.0 * (float(self.side) ** 2)
  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
    return float(self.side) ** 3
  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
    self.get_cube_coord()
    if p.x > self.range_x[0] and p.x < self.range_x[1] and p.y > self.range_y[0] and p.y < self.range_y[1] and p.z > self.range_z[0] and p.z < self.range_z[1]:
      return True
    return False
  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    self.get_cube_coord()
    a_sphere.get_sphere_coord()
    if a_sphere.range_x[0] > self.range_x[0] and a_sphere.range_x[1] < self.range_x[1] and a_sphere.range_y[0] > self.range_y[0] and a_sphere.range_y[1] < self.range_y[1] and a_sphere.range_z[0] > self.range_z[0] and a_sphere.range_z[1] < self.range_z[1]:
      return True
    return False
  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
    self.get_cube_coord()
    other.get_cube_coord()
    if other.range_x[0] > self.range_x[0] and other.range_x[1] < self.range_x[1] and other.range_y[0] > self.range_y[0] and other.range_y[1] < self.range_y[1] and other.range_z[0] > self.range_z[0] and other.range_z[1] < self.range_z[1]:
      return True
    return False
  def is_outside_cube (self, other):
    self.get_cube_coord
    other.get_cube_coord()
    if other.range_x[0] > self.range_x[1] or other.range_x[1] < self.range_x[0]:
      return True
    return False
  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, a_cyl):
    self.get_cube_coord()
    a_cyl.get_cyl_coord()
    #check if min x,y,z of inside object are greater than min of outside object.
    #check if max x,y,z of inside object are less than max of outside object.
    if a_cyl.range_x[0] > self.range_x[0] and a_cyl.range_x[1] < self.range_x[1] and a_cyl.range_y[0] > self.range_y[0] and a_cyl.range_y[1] < self.range_y[1] and a_cyl.range_z[0] > self.range_z[0] and a_cyl.range_z[1] < self.range_z[1]:
      return True
    return False
  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
    if self.is_inside_cube(other) == False and self.is_outside_cube(other) == False:
      return True
    return False
  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
    return
  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
    ins_sphere = Sphere(self.center.x, self.center.y, self.center.z)
    ins_sphere.radius = self.side / 2
    return ins_sphere
class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
    self.center = Point(x, y, z)
    self.radius = float(radius)
    self.height = float(height)
  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
    return f'Center: ({self.center.x}, {self.center.y}, {self.center.z}), Radius: {self.radius}, Height: {self.height}'
  # compute surface area of Cylinder
  # returns a floating point number
  def get_cyl_coord(self):
    min_x = self.center.x - self.radius
    max_x = self.center.x + self.radius
    min_y = self.center.y - (self.height / 2)
    max_y = self.center.y + (self.height / 2)
    min_z = self.center.z - self.radius
    max_z = self.center.z + self.radius
    range_x = (min_x, max_x)
    range_y = (min_y, max_y)
    range_z = (min_z, max_z)
    self.range_x = range_x
    self.range_y = range_y
    self.range_z = range_z
  def area (self):
    return (2.0 * math.pi * float(self.radius) * float(self.height)) + (2.0 * math.pi * float(self.radius) ** 2)
  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
    return math.pi * float(self.radius) ** 2 * float(self.height)
  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
    self.get_cyl_coord()
    if p.x > self.range_x[0] and p.x < self.range_x[1] and p.y > self.range_y[0] and p.y < self.range_y[1] and p.z > self.range_z[0] and p.z < self.range_z[1]:
      return True
    return False
  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    self.get_cyl_coord()
    a_sphere.get_sphere_coord()
    if a_sphere.range_x[0] > self.range_x[0] and a_sphere.range_x[1] < self.range_x[1] and a_sphere.range_y[0] > self.range_y[0] and a_sphere.range_y[1] < self.range_y[1] and a_sphere.range_z[0] > self.range_z[0] and a_sphere.range_z[1] < self.range_z[1]:
      return True
    return False
  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    self.get_cyl_coord()
    a_cube.get_cube_coord()
    if a_cube.range_x[0] > self.range_x[0] and a_cube.range_x[1] < self.range_x[1] and a_cube.range_y[0] > self.range_y[0] and a_cube.range_y[1] < self.range_y[1] and a_cube.range_z[0] > self.range_z[0] and a_cube.range_z[1] < self.range_z[1]:
      return True
    return False
  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
    dist_centers = self.center.distance(other.center)
    return ((dist_centers + other.radius < self.radius) and (dist_centers + float(other.height / 2.0) < float(self.height / 2.0)))
  def is_outside_cylinder (self, other):
    dist_centers = self.center.distance(other.center)
    return ((dist_centers > other.radius + self.radius) and (dist_centers > (other.height / 2.0 + self.height / 2.0)))
  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder (self, other):
    return (not self.is_inside_cylinder(other) and not self.is_outside_cylinder(other))
def main():
  # read data from standard input
  # read the coordinates of the first Point p
  coord_list = sys.stdin.readline().strip().split()
  # create a Point object 
  p_point = Point(coord_list[0], coord_list[1], coord_list[2])
  # read the coordinates of the second Point q
  coord_list = sys.stdin.readline().strip().split()
  # create a Point object 
  q_point = Point(coord_list[0], coord_list[1], coord_list[2])
  # read the coordinates of the center and radius of sphereA
  coord_list = sys.stdin.readline().strip().split()
  # create a Sphere object 
  sphere_a = Sphere(coord_list[0], coord_list[1], coord_list[2], coord_list[3])
  # read the coordinates of the center and radius of sphereB
  coord_list = sys.stdin.readline().strip().split()
  # create a Sphere object
  sphere_b = Sphere(coord_list[0], coord_list[1], coord_list[2], coord_list[3])
  # read the coordinates of the center and side of cubeA
  coord_list = sys.stdin.readline().strip().split()
  # create a Cube object 
  cube_a = Cube(coord_list[0], coord_list[1], coord_list[2], coord_list[3])
  # read the coordinates of the center and side of cubeB
  coord_list = sys.stdin.readline().strip().split()
  # create a Cube object 
  cube_b = Cube(coord_list[0], coord_list[1], coord_list[2], coord_list[3])
  # read the coordinates of the center, radius and height of cylA
  coord_list = sys.stdin.readline().strip().split()
  # create a Cylinder object 
  cyl_a = Cylinder(coord_list[0], coord_list[1], coord_list[2], coord_list[3], coord_list[4])
  # read the coordinates of the center, radius and height of cylB
  coord_list = sys.stdin.readline().strip().split()
  # create a Cylinder object
  cyl_b = Cylinder(coord_list[0], coord_list[1], coord_list[2], coord_list[3], coord_list[4])
  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin
  origin = Point()
  if p_point.distance(origin) > q_point.distance(origin):
    print('Distance of Point p from the origin is greater than the distance of Point q from the origin')
  else:
    print('Distance of Point p from the origin is not greater than the distance of Point q from the origin')
  print()
  # print if Point p is inside sphereA
  if sphere_a.is_inside_point(p_point):
    print('Point p is inside sphereA')
  else:
    print('Point p is not inside sphereA')
  # print if sphereB is inside sphereA
  if sphere_a.is_inside_sphere(sphere_b):
    print('sphereB is inside sphereA')
  else: 
    print('sphereB is not inside sphereA')
  # print if cubeA is inside sphereA
  if sphere_a.is_inside_cube(cube_a):
    print('cubeA is inside sphereA')
  else:
    print('cubeA is not inside sphereA')
  # print if cylA is inside sphereA
  if sphere_a.is_inside_cyl(cyl_a):
    print('cylA is inside sphereA')
  else:
    print('cylA is not inside sphereA')
  # print if sphereA intersects with sphereB
  if sphere_a.does_intersect_sphere(sphere_b):
    print('sphereA does intersect sphereB')
  else:
    print('sphereA does not intersect sphereB')
  # print if cubeB intersects with sphereB
  if sphere_b.does_intersect_cube(cube_b):
    print('cubeB does intersect sphereB')
  else:
    print('cubeB does not intersect sphereB')
  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA
  circ_cube = sphere_a.circumscribe_cube()
  if circ_cube.volume() > cyl_a.volume():
    print('Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA')
  else:
    print('Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA')
  print()
  # print if Point p is inside cubeA
  if cube_a.is_inside_point(p_point):
    print('Point p is inside cubeA')
  else:
    print('Point p is not inside cubeA')
  # print if sphereA is inside cubeA
  if cube_a.is_inside_sphere(sphere_a):
    print('sphereA is inside cubeA')
  else:
    print('sphereA is not inside cubeA')
  # print if cubeB is inside cubeA
  if cube_a.is_inside_cube(cube_b):
    print('cubeB is inside cubeA')
  else:
    print('cubeB is not inside cubeA')
  # print if cylA is inside cubeA
  if cube_a.is_inside_cylinder(cyl_a):
    print('cylA is inside cubeA')
  else:
    print('cylA is not inside cubeA')
  # print if cubeA intersects with cubeB
  if cube_b.does_intersect_cube(cube_a):
    print('cubeA does intersect cubeB')
  else:
    print('cubeA does not intersect cubeB')
  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
  if cube_b.intersection_volume(cube_a) > sphere_a.volume():
    print('Intersection volume of cubeA and cubeB is greater than the volume of sphereA')
  else:
    print('Intersection volume of cubeA and cubeB is not greater than the volume of sphereA')
  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA
  ins_sphere = cube_a.inscribe_sphere()
  if ins_sphere.area() > cyl_a.area():
    print('Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA')
  else:
    print('Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA')
  print()
  # print if Point p is inside cylA
  if cyl_a.is_inside_point(p_point):
    print('Point p is inside cylA')
  else:
    print('Point p is not inside cylA')
  # print if sphereA is inside cylA
  if cyl_a.is_inside_sphere(sphere_a):
    print('sphereA is inside cylA')
  else:
    print('sphereA is not inside cylA')
  # print if cubeA is inside cylA
  if cyl_a.is_inside_cube(cube_a):
    print('cubeA is inside cylA')
  else:
    print('cubeA is not inside cylA')
  # print if cylB is inside cylA
  if cyl_a.is_inside_cylinder(cyl_b):
    print('cylB is inside cylA')
  else:
    print('cylB is not inside cylA')
  # print if cylB intersects with cylA
  if cyl_a.does_intersect_cylinder(cyl_b):
    print('cylB does intersect cylA')
  else:
    print('cylB does not intersect cylA')
if __name__ == "__main__":
  main()
