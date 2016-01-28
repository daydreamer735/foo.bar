def answer(n):
    import math
    pad = 0
    while n > 0:
        n = n - int(math.sqrt(n))**2
        pad = pad + 1
    return pad
