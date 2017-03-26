
# | 29
# | 22 30
# | 16 23 31
# | 11 17 24 32
# | 7  12 18 25 33
# | 4  8  13 19 26 34
# | 2  5  9  14 20 27 35
# | 1  3  6  10 15 21 28 36

# numbers along bottom increase with each row by the number of rows that have been added.
# recursion?

def answer(x,y):
    x_id = get_x_id_from_coord(x)
    for _ in range(1, y):
        x_id += x
        x += 1
    return str(x_id)

def get_x_id_from_coord(x):
    if x == 1:
        return 1
    else:
        return x + get_x_id_from_coord(x-1)




print get_x_id_from_coord(1)
print get_x_id_from_coord(5)
print get_x_id_from_coord(8)

# answer(3,2)
# answer(5,10)
answer(1,8)
