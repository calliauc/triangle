
def triangle(nb):
    if not nb or nb%2 == 0:
        return()
    for i in range(nb):
        num="*"
        print(num.rjust(nb-i, ' ') + i*2*"*")

triangle(5)