from math import pi, exp, sqrt

def gaussian(m,s,x):
    const = 1/(sqrt(2*pi) * s)
    exp_term = exp(-1/2 * ((x-m)/s)**2)
    return const*exp_term

print(gaussian(0,2,1))