
''' Purpose: print the sum of a user-supplied list of values

    Email id: jgs8wh@virginia.edu
    Name: Jaden Stanford
'''

# get the values
reply =input('Please enter a list of integers: ')

# convert the values
list1 = [ ]
list1 = reply.split()

integer_list = [ ]

for n in list1:
    n = int(n)
    integer_list.append(n)

print(integer_list)

# sum the values

total = 0

for i in integer_list:
    total = i + total


print('The sum of the values is:', total)
