def n_topla(i):

    if i == 0:
        return 0

    else:
        return i + n_topla(i-1)

print(n_topla(i))
