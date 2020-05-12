
''' Purpose: determine the worth of a piggy bank
     User id: jgs8wh

    Problem statement:
        Prompt user respectively for four values: a number of quarters,
        dimes, nickels, and pennies.  Then compute and display how much the
        indicated coins are worth.

    Checker(s): aez5uzy@virginia.edu
'''
coins = input('Please enter the number of quarters, dimes, nickels, and pennies (in order): ')
q, d, n, p = coins.split()
q = int(q)
d = int(d)
n = int(n)
p = int(p)
quarter_value = 0.25
dime_value = 0.1
nickel_value = 0.05
penny_value = 0.01
total_q = q * quarter_value
total_d = d * dime_value
total_n = n * nickel_value
total_p = p * penny_value
total_money = total_q + total_d + total_n + total_p
total_money = round(total_money, 2)
print('Coinage')
print('\t', q, 'quarters')
print('\t', d, 'dimes')
print('\t', n, 'nickels')
print('\t', p, 'pennies')
print('There is a total of', total_money, 'dollars')
