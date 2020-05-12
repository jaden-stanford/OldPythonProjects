
''' Purpose: provide overlay of pillow support
'''

from PIL import Image
from PIL import ImageTk

import tkinter
from tkinter import *

def get_blank_image( dim, bg="#000000" ) :
    ''' Returns a new image with dimensions w by h
    '''

    from PIL import Image

    img = Image.new( "RGB", dim, bg )

    return img

def show( img ) :
    ''' Display img to screen
    '''

    img.show()

def get_selfie( person ) :
    ''' Returns a new copy of the cs 1112 of selfied uploaded by person 
    '''
    PEOPLE_FOLDER = "http://www.cs.virginia.edu/~cs1112/people/"

    link = PEOPLE_FOLDER + person + "/selfie.jpg"

    img = get_image( link  )

    return img

def get_image( link ) :
    ''' Returns a new copy of the image at link
    '''

    import urllib.request, io
    from PIL import Image
    
    stream = urllib.request.urlopen( link )
    data = stream.read()
    pixels = io.BytesIO( data )
    img    = Image.open( pixels )
    img    = img.convert('RGB')

    #load_canvas( img )

    return img

def get_size(  img ) :
    ''' Returns the dimensions of img
    '''

    return img.size

def set_pixel( img, xy, c ) :
    ''' Sets the spot xy in img to color c
    '''

    img.putpixel( xy, c )

    # update_canvas( img )


def get_pixel( img, xy ) :
    ''' Gets the color at spot xy in img
    '''

    img.getpixel( xy )

def resize( img, max_w, max_h ) :
    ''' Scales img to ensure that it fits within a max_w x max_h box
    '''

    w, h = img.size

    scale_w = w / max_w
    scale_h = h / max_h

    scale = max( scale_w, scale_h )

    if ( scale > 1 ) :
        w = int( w / scale )
        h = int( h / scale )
        img = img.resize( ( w, h ) ).convert( 'RGB' )
        
    return img

### ----

# define globals and initialize
global canvas, image, board, tk_img, root, container

canvas    = None
image     = None
tk_img    = None
root      = None
container = None

def load_canvas( img, update=None ) :
    global root, container, tk_img, canvas

    w, h = img.size

    cw, ch = w + 125, h + 75

    root = Tk()
    root.title( "" )

    container = Frame( root, width=cw, height=ch, bg="#000000" )
    container.pack_propagate( 0 )
    container.pack()

    tk_img = ImageTk.PhotoImage(img)

    canvas = tkinter.Label( container, image=tk_img )
    canvas.image = tk_img
    canvas.source = img

    canvas.config()
    canvas.pack()

    if ( update != None ) :
        refresh( img, f )

    root.mainloop()

    return canvas

def update_canvas( img ) :

    from PIL import Image
    from PIL import ImageTk

    global canvas

    tk_img = ImageTk.PhotoImage( img )
    canvas.image = tk_img
    canvas.source = img

#initialize()

#img = get_blank_image( (600,800), "Navy" )
#img = get_image( "http://www.cs.virginia.edu/~cs1112/images/ycdi.png" ); 
