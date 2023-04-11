from get_coordinates import vertical, horizontal
from convert_to_str import convert

def bishop(coordinates):
    ver = vertical(coordinates)
    hor = horizontal(coordinates)

    b_hor = hor
    b_ver = ver

    while b_hor > 0 and b_ver < 7:
        b_hor = b_hor - 1
        b_ver = b_ver + 1
        print(convert(b_ver, b_hor))

    b_hor = hor
    b_ver = ver

    while b_hor < 7 and b_ver < 7:
        b_hor = b_hor + 1
        b_ver = b_ver + 1
        print(convert(b_ver, b_hor))

    b_hor = hor
    b_ver = ver

    while b_hor < 7 and b_ver > 0:
        b_hor = b_hor + 1
        b_ver = b_ver - 1
        print(convert(b_ver, b_hor))

    print(coordinates)
