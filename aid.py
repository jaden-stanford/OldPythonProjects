

''' Purpose: function exploration with list manipulations

    Email id: jgs8wh@virginia.edu
    Email id: aez5uzy@virginia.edu

    Pledge: All effort for this assignment has been done as team and when both
            the driver and navigator are present and working together
'''


def rotate( x ) :
    ''' Returns ...

        Driver: Jaden
        Navigator: Anthony
    '''
    length = len(x)
    if (length != 0):
        letter = x.pop()
        x.insert(0, letter)
        return x
    else:
        pass



def rotate_k_times( x, k ) :
    ''' Returns ...

        Driver: Jaden
        Navigator: Anthony
    '''

    for i in range (0, k):
        rotate(x)
    return x


def common( x, y ) :
    ''' Returns ...

        Driver: Jaden
        Navigator: Anthony
    '''

    a = x.copy()
    b = y.copy()

    list = []

    for element in a:
        if element in b:
            list.append(element)
    return list

if ( __name__ == '__main__' ) :
    import abet

    abet.test_rotate()
    abet.test_rotate_k_times()
    abet.test_common()
