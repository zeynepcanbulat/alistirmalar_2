def n_faktoriyel(i):
    if i == 1 or i == 0:
        return 1

    else:
        return i * n_faktoriyel(i-1)

print(n_faktoriyel(i))
