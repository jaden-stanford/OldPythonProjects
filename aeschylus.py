

''' Purpose: convert input into a list of words; print the list; remove
        all 's' from the words in the list; print the updated list

Author: Jaden Stanford
User id: jgs8wh@virginia.edu
'''

# get input and convert it into a list of words 

reply = input('Type a sentence: ')

words = reply.split()

# print what we have so far

print(  words )

#
new_list = []
for i in words:
    i =  i.replace('s','' )
    new_list.append(i)

print(new_list)

print(words)
