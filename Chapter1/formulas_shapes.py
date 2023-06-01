from math import pi

h = 5.0 # height
b = 2.0 # base
r = 1.5 # radius

area_parallelogram = h * b
print('The area of a parallalogram is %.3f' %area_parallelogram)

area_square = b**2
print('The area of a square is %.3f' %area_square )

area_circle = pi*r**2
print('The area of a circle is %.3f' %area_circle)

volume_cone = 1.0/3.0 * pi * r**2 * h
print('The volume of a cone is %.3f' %volume_cone)