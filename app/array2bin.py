import struct

def convert(l):
    '''
    Converts a list of lists of 8x8 into
    8 bytes
    '''
    r = bytes(0)

    for row in l:
        byte = 0
        offset = 7

        for col in row:
            thing = 1 << offset
            offset -= 1
            if col:
                byte |= thing
        r += struct.pack('B', byte)
    return r
