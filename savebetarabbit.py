def answer(grid,food):
    n = len(grid)

    a = [[[]for i in range(n)]for i in range(n)]

    a[0][0] = [0]

    for i in range(1,n):
        a[0][i] = [j+grid[0][i] for j in a[0][i-1]]
        a[i][0] = [j+grid[i][0] for j in a[i-1][0]]

    for i in range(1,n):
        for j in range(1,n):
            a[i][j] = {}.fromkeys([k+grid[i][j] for k in a[i-1][j]]+[k+grid[i][j] for k in a[i][j-1]]).keys()
      
    for i in range(food,2*n-1,-1):
        if i in a[n-1][n-1]:
            return(food-i)
            break
    return(-1)
