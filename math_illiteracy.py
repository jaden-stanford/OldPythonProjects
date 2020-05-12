
''' Purpose: naming allows abstraction
'''

# get access to Python math comutational resources
import math             


# demonstrate the two math constants
print( 'Python approximation of pi:', math.pi )
print( 'Python approximation of Euler\'s number:', math.e )

print()
print()

# show some math computation
a = math.radians( 30 )
b = math.radians( 45 )

sin_a = math.sin( a )
tan_b = math.tan( b )

print( 'sin( 30 degrees ):', sin_a )
print( 'tan( 45 degrees ):', tan_b )

print()

# show some helpful built-in math / math-like functions

reply = input( 'Enter two numbers: ' )
n1, n2 = reply.split()
n1, n2 = int( n1 ), int( n2 )

print( 'n1 =', n1 )
print( 'n2 =', n2 )

print()
input( 'Enter when ready. ' )

bigger  = max( n1, n2 )
smaller = min( n1, n2 )

print( 'max( n1, n2 ):', bigger )
print( 'min( n1, n2 ):', smaller )

print()
input( 'Enter when ready. ' )

pos_n1 = abs( n1 )
pos_n2 = abs( n2 )

print( 'abs( n1 ):', pos_n1 )
print( 'abs( n2 ):', pos_n2 )

print()
