
''' Purpose: web data acquisition -- print line-by-line the list of lines making up
        the contents of web file most-misspelled from
        http://www.cs.virginia.edu/~cs1112/datasets/words/
'''

# need help to get web data - so import the capability
from urllib.request import urlopen

# specify the link of interest
CS1112_WORDS_WEB_FOLDER = "http://www.cs.virginia.edu/~cs1112/datasets/words/"
FILE_NAME = "most-misspelled"

# get a link to file of interest
link = CS1112_WORDS_WEB_FOLDER + FILE_NAME

link = "http://www.cs.virginia.edu/~cs1112/datasets/words/most-misspelled"

# get a connection to stream the web resource of interest
stream = urlopen( link )

# read stream to get the contents of the page
content = stream.read()

# decode contents into plain text form
text = content.decode( "UTF-8" )
text = text.strip()
# get the lines that make up the text
lines = text.split('\n') # will split on \n

# print the lines one by one
for line in lines:
    print(line)
