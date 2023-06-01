n_seconds = 1E+09

seconds_per_day = 60 * 60 * 24 # 60 seconds in 1 minute, 60 minutes in 1 hour, 24 hours in 1 day
days_per_year   = 365.25       # 365.25 days per year

n_years = n_seconds * 1/seconds_per_day * 1/days_per_year

print(f'Number of years in {n_seconds}: {n_years:0.3f} years')