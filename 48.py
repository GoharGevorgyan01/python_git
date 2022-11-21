# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
#-----------------------------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

m1 = []
for i in range(len(matrix)):
    m = [] 
    for j in range(len(matrix)-1,-1,-1):
        m.append(matrix[j][i])
    m1.append(m)
matrix.clear()
matrix = m1
print(matrix)