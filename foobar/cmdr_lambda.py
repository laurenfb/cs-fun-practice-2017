import math

def answer(n):
    # your code here
    id_string = ""
    number = 1
    while len(id_string) < 10006:
        if is_prime(number):
            id_string += str(number)
        number += 1
    minion_id = id_string[n:n+5]
    return minion_id



def is_prime(number):
    number = abs(number)
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for divisor in range(2, int(math.sqrt(number)+1)):
            if number % divisor == 0:
                return False
    return True


print answer(0)
print answer(3)
print answer(10000)
