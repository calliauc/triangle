def triangle(nb):
    if not nb or nb % 2 == 0:
        return
    for i in range(nb):
        stars = (i * 2 + 1) * "*"
        stars = stars.center(nb * 2, " ")
        print(f"{stars}")


triangle(5)
