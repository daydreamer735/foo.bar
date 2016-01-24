def answer(x):
    car = len(x)
    total = sum(x)
    if total % car == 0:
        return car
    else:
        return car - 1
