
""" Purpose: introduce some functions from module random
"""

import random 

# by default the random module produces different interactions everytime we use it

print( "three random values" )

f1 = random.random()     # returns a decimal number from the interval [0, 1 )
f2 = random.random()     
f3 = random.random()     

print( "f1 =", f1 )
print( "f2 =", f2 )
print( "f3 =", f3 )

print();
reply = input( "Enter when ready: " )
print();

# sometimes we need to have replicable random value sequences.  module random
# provides # function seed() for that purpose. the function with a single
# value produces a unique random value sequence, different values produce
# different sequences

print( "three random values gotten by resetting the seed" )
random.seed( 1112 )     # first random value will be 0.28143470043335006. how
r1 = random.random()    # do we know this, we ran the program and recorded the
                        # result
random.seed( 1112 )     
r2 = random.random()

random.seed( 1112 )     
r3 = random.random()

print( "r1 =", r1 )
print( "r2 =", r2 )
print( "r3 =", r3 )

print();
reply = input( "Enter when ready: " )
print();

# when seed() is not given a parameter it generates a non-replicable sequence

print( "three random values" )
random.seed()

n1 = random.random()
n2 = random.random()
n3 = random.random()

print( "n1 =", n1 )
print( "n2 =", n2 )
print( "n3 =", n3 )

print();
reply = input( "Enter when ready: " )
print();

# random function randrange( x, y ) returns random integer from interval [ x, y )

a = 0
b = 8

i1 = random.randrange( a, b )
i2 = random.randrange( a, b )
i3 = random.randrange( a, b )

print( "three random values from the interval [", a, ",", b, ")" )
print( "i1 =", i1 )
print( "i2 =", i2 )
print( "i3 =", i3 )

print();
reply = input( "Enter when ready: " )
print();

# function random.randrange( x, y, s ) returns random integer value from the
#      s-stepped interval [ x, y ) -- x, x+s, x+2s, ...

a =   0
b = 100
c =   5

s1 = random.randrange( a, b, c )
s2 = random.randrange( a, b, c )
s3 = random.randrange( a, b, c )

print( "three random values from the", c, "stepped interval [", a, ",", b, ")" )
print( "s1 =", s1 )
print( "s2 =", s2 )
print( "s3 =", s3 )

print();
reply = input( "Enter when ready: " )
print();

# function random.choice( s ) returns a random element of sequence s

keyboard = "qwertyuiopasdfghjklzxcvbnm"

k1 = random.choice( keyboard )
k2 = random.choice( keyboard )
k3 = random.choice( keyboard )

print( "three random values from character sequence", keyboard )

print( "k1 =", k1 )
print( "k2 =", k2 )
print( "k3 =", k3 )

print();
reply = input( "Enter when ready: " )
print();


days = [ "Su", "Mo", "Tu", "We", "Th", "Fr", "Sa" ]

d1 = random.choice( days )
d2 = random.choice( days )
d3 = random.choice( days )

print( "three random values from list", days )
print( "d1 =", d1 )
print( "d2 =", d2 )
print( "d3 =", d3 )

print();
reply = input( "Enter when ready: " )
print();

# random.shuffle( s ) if s is a list, randomly reorders s

random.shuffle( days )

print( "days =", days )
