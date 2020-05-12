
''' Purpose: Experience the thrill of random generation and list examination

    Task: Prompt and get three integers s, n, and d from its user (in that
          order). Use integer s as a seed to the Python random number
          generator. Then print n octal digits (base 8 digits) line by
          line by line. Then print the number of generated occurrences of d.
          There should be no other output

    Checker:

'''

# needed module
import random

#####  Get the input 

reply = input( 'Enter three numbers: ' )

#####  Convert the input into the integers s, d, n   
s, n, d = reply.split()

s, n, d = int( s ), int( n ), int( d )

#####  Set the seed for generating random values 

#####  Generate and print n random octal numbers and along the way store them in a list

#####  Determine number of generated octal values equal to d and print that number out


