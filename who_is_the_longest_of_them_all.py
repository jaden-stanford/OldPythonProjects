
''' Purpose: find the word of the longest length amongst the input
'''

# get the words
reply = input( 'Enter a series of words: ' )
words = reply.split()

# need to keep track of the longest word seen so far. It's initialization
# should never prevent the word of longest length being missed

longest_word_seen = ''
# consider the words one by one

for word in words :

    # check the word out - compare its length to longest so far
    # if current word is longer than the longest word so far, need to update
    #first ge the lengths of the two words we want to compare

    n_1 = len(longest_word_seen)
    n_2 = len(word)

    if (n_2 > n_1):
        longest_word_seen = word
    else:
        pass


# longest word so far must be longest as considered every word as a possibility

# print longest word

print(longest_word_seen)

# all done

#What if we wanted to find all of the words that are the longest?

for word in words:
    n_1 = len(longest_word_seen)
    n_2 = len(word)

    if (n_1 == n_2):
        print(word)
