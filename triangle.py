def triangle(nb):
    if not nb or nb % 2 == 0:
        return
    for i in range(nb):
        stars = (i * 2 + 1) * "*"
        center = stars.center(nb * 2, " ")
        print(f"{center}")


triangle(5)
