from math import pi

V_hard = 120 # km/hr
V_soft = 30  # km/hr

V_hard *= 100 / (60 * 60)
V_soft *= 100 / (60 * 60)

def F_drag(C,rho,A,v):
    return 1/2 * C * rho * A * v**2

def F_grav(m,g=9.81):
    return m*g

def ratio(C,rho,A,v,m,g=9.81):
    return F_drag(C,rho,A,v)/F_grav(m,g)

rho = 1.2 # kg / m^3
a   = 11  # cm

A   = pi * (a / 100)**2 # m^2

m = 0.43 # kg

C = 0.4

print('Hard')
print('F drag: %.3f' %F_drag(C,rho,A,V_hard))
print('F grav: %.3f' %F_grav(m))
print('Ratio: %.3f' %ratio(C,rho,A,V_hard,m))

print('Soft')
print('F drag: %.3f' %F_drag(C,rho,A,V_soft))
print('F grav: %.3f' %F_grav(m))
print('Ratio: %.3f' %ratio(C,rho,A,V_soft,m))