def answer(x):
    car = len(x)
    total = sum(x)
    if total % car == 0:
        solution = total / car
        return solution
    else:
        solution = car - 1
        return solution
