# Inputs:
INPUT1 = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
# Output:
OUTPUT2 =["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]
#
# Inputs:
INPUT = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
# Output:
OUTPUT =["0.1", "1.1.1", "1.2", "1.2.1", "1.11", "2", "2.0", "2.0.0"]


def custom_cmp(a,b):
    if a[0] == b[0]:
        return 0
    else:
        a = a.split('.')
        b = b.split('.')
        if len(a) == 1 or len(b) == 1:
            return 0
        if a[1] > b[1]:
            return -1
        elif a[1] == b[1]:
            return 0
        else:
            return -1

def answer(l):
    l = sorted(l)
    return sorted(l, cmp=custom_cmp)


answer(INPUT)
print OUTPUT
