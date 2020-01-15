x = [
    [2,3,5],
    [4,7,1],
    [9,5,7]
    ]


y = [
    [3,3,8],
    [1,4,1],
    [3,4,2]
    ]

result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
        result[i][j] = x[i][j]+ y[i][j]


print(result)
