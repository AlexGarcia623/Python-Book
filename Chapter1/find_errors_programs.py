# a
from math import sin, cos, pi
x = pi/4
l_val = sin(x)**2 + cos(x)**2
print(l_val)

# b 
v0 = 3 # m/s
t  = 1 # m
a  = 2 # m/s^2
s  = v0*t + 0.5*a*t**2
print(s)

# c
a  = 3
b  = 5
def checker(a,b):
    a2 = a ** 2
    b2 = b ** 2

    eq1_sum = a2 + 2*a*b + b2
    eq2_sum = a2 - 2*a*b + b2

    eq1_pow = (a+b)**2
    eq2_pow = (a-b)**2

    print('First equation: %g = %g' %(eq1_sum, eq1_pow))
    print('Second equation: %g = %g' %(eq2_sum, eq2_pow))

checker(3,3)
checker(3,5)