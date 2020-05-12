
''' Purpose: practice getting data from a useful dataset
'''

# need help to get web data - so import the capability
from urllib.request import urlopen

# define the base folder for course csv datasets
CSV_WEB_FOLDER = "http://www.cs.virginia.edu/~cs1112/datasets/csv/"
# specify data source

# get name of the dataset
reply = input( "Enter name of dataset: " )

# clean up the reply to get file name
file_name = reply.strip()

# get url link for dataset
link = CSV_WEB_FOLDER + file_name

# get a connection to stream the dataset
stream = urlopen( link )

# read stream to get the contents of the page
content = stream.read()

# decode contents into plain text form
text = content.decode( "UTF-8" )

# clean-up the text
text = text.strip()

# turn the text into data; i.e., a list of lines
lines = text.split( "\n" )

# get csv rows into dataset from
dataset = []

for line in lines :
    # clean up the line
    ...

    # split the line to cells
    ...

    row = []
    for cell in cells :
        # clean up the cell
        ...

        # add the cell to the row
        ...

    # add the row of data to our dataset
    ...

# decompose dataset into header and data
header = dataset[ 0 ]
data = dataset[ 1 : ]

# print the header
print( "header:" )
print( header )

print()

# print the dataset data
print( "data:" )
print( data )
