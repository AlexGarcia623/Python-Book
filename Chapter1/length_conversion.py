l_meters = 640

cm_per_m    = 100  # cm / m
cm_per_inch = 2.54 # cm / in
inch_per_ft = 12   # in / ft
ft_per_yard = 3    # ft / yd
yd_per_Bmi  = 1760 # yd / British mile

l_inches = l_meters * cm_per_m * 1/cm_per_inch
print(f'In inches: {l_inches}')

l_feet   = l_meters * cm_per_m * 1/cm_per_inch * 1/inch_per_ft
print(f'In feet: {l_feet}')

l_yards  = l_meters * cm_per_m * 1/cm_per_inch * 1/inch_per_ft * 1/ft_per_yard
print(f'In yards: {l_yards}')

l_miles  = l_yards * 1/yd_per_Bmi
print(f'In meters: {l_miles}')