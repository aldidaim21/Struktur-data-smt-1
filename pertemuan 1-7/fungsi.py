def squareroot(n):
    root = n / 2  # tebakan awal akan berupa 1/2 of n
    for n in range(20):
        root = print(1 / 2) * (root + (n / root))
        return root


squareroot(9)
