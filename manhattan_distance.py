
''' Purpose: Compute distance between two Manhattan corners

    Name: Jaden Stanford
    Computing ID: jgs8wh
'''

# important problem related-constants
AVERAGE_STREET_LENGTH = 0.05   # miles
AVERAGE_AVENUE_LENGTH = 0.15   # miles

# prompt for first street and avenue location
first_location  = input('Please enter street number and avenue number of first location: ')
street1, avenue1 = first_location.split()

# convert input to integers
street1, avenue1 = int(street1) , int(avenue1)

# prompt for second street and avenue location
second_location = input('Please enter street number and avenue number of second location: ')
street2, avenue2 = second_location.split()

# convert input to integers
street2, avenue2 = int(street2), int(avenue2)
# compute inter-street distance
street_distance = (AVERAGE_STREET_LENGTH * abs(street1 - street2))

# compute inter-avenue distance
avenue_distance = (AVERAGE_AVENUE_LENGTH * abs(avenue1 - avenue2))

# compute distance between the two locations -- sum of the inter-street and inter-avenue distances
total_distance = street_distance + avenue_distance

# display result
print('The distance between the two corners is approximately', total_distance, 'miles')
