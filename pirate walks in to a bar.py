def answer(numbers):
    i = 0
    pirate = []
    pirate.append(0)
    while True:
        new = numbers[i]
        if new not in pirate:
            pirate.append(new)
            i = new
        else:
            solution = len(pirate) - pirate.index(new)
            return solution

print answer([1,3,0,1])  
print answer([1,0])
print answer([1,2,1])
