
# name: Jaden Stanford
# email id: jgs8wh@virginia.edu

# any assistance: aez5uzy@virginia.edu

# purpose: use random, str, and list to generate a random sentence based on
#    user input.  the sentence is of form
#        Adjective noun verb adject noun

# needed modules
import random

# steps for random sentence generation
seed1 = input('Enter seed: ')
random.seed(seed1)

adj = input('Enter adjectives: ')
adjectives = adj.split()

n = input('Enter nouns: ')
nouns = n.split()


v = input('Enter verbs: ')
verbs = v.split()

w1 = random.choice(adjectives)
w2 = random.choice(nouns)
w3 = random.choice(verbs)
w4 = random.choice(adjectives)
w5 = random.choice(nouns)


print( )

print( w1, w2, w3, w4, w5)


