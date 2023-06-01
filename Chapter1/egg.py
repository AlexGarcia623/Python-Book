from math import pi, log
def egg( M, T0 ):
    T0 += 273.15 # K

    rho = 1.038 # g / cm^3
    c   = 3.7   # J / g / K
    K   = 5.4E-3 # W / cm / K
    Tw  = 100 # C
    Tw  += 273.15 # K
    Ty  = 70 # C
    Ty  += 273.15 # K

    const = M**(2/3) * c * rho**(1/3) / ( K * pi * (4*pi/3)**(2/3) )
    log_term = log( 0.76 * (T0 - Tw) / ( Ty - Tw ) )

    return const*log_term

print('Large egg 4 C: %.3f s' %egg(67, 4))
print('Large egg 20 C: %.3f s' %egg(67, 20))