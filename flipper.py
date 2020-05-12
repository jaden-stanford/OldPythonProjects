
''' Purpose: implements the flipper.py problem on test 1
'''

import random

# get inputs
reply1 = input( "Enter seed: " )

random.seed(reply1)

reply2 = input( "Enter choices: " )
string = reply2.split()

reply3 = input( "Enter flips: " )
flips = int(reply3)

for r in range (0, flips):
    r = random.choice(string)
    print(r)
