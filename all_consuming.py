
''' Purpose: estimates annual consumption of a commodity 

    Name: Jaden Stanford
    Computing ID: jgs8wh

    Checker: aez5uzy@virginia.edu
'''


# Important time constants

WEEK_PER_YEAR         = 52
WEEK_DAYS_PER_WEEK    =  5
WEEKEND_DAYS_PER_WEEK =  2

# Get input commodity of interest 
food = input('What is something that you eat on a daily basis? ')
# Determine weekday consumption and weekend day consumption prompts
amount_weekday = input('How much ' + food + ' do you consume on a regular weekday? ')
amount_weekend = input('How much ' + food + ' do you consume on a regular weekend day? ')
# Separately get weekday and weekend day consumptions
amount_weekday = int(amount_weekday)
amount_weekend = int(amount_weekend)
# Compute weekly consumption
weekly_consumption = amount_weekday * WEEK_DAYS_PER_WEEK * WEEK_PER_YEAR
weekend_consumption = amount_weekend * WEEKEND_DAYS_PER_WEEK * WEEK_PER_YEAR
# Compute yearly consumption
yearly_consumption = weekly_consumption + weekend_consumption
# Report yearly consumption
print('You consume',yearly_consumption, food , 'per year')
