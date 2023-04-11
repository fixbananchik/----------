def horizontal(coordinata):
    bufer = coordinata[0]
    my_letters = 'abcdefgh'
    return my_letters.index(bufer)

def vertical(coordinata):
    bufer = coordinata[1]
    return int(bufer) - 1
