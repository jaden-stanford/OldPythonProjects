
''' Purpose: print a requested phrase a requested number of times
'''

# get phrase to be repeated
reply = input( "Enter phrase to be printed: " )

phrase = reply.strip()

# get number of times to repeat the phrase
reply = input( "Enter number of times to print the phrase: " )


nbr_of_times = int( reply )

# print the phrase the right number of times
for i in range( 0 , nbr_of_times):
    print(phrase)
