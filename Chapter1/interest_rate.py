def interest( amount, rate, n_years ):
    return amount * (1 + rate/100) ** n_years

print( interest(1000, 5, 3) )