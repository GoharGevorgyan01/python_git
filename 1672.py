# Input: accounts = [[1,5],[7,3],[3,5]]
# Output: 10
# Explanation: 
# 1st customer has wealth = 6
# 2nd customer has wealth = 10 
# 3rd customer has wealth = 8
# The 2nd customer is the richest with a wealth of 10.
#-------------------------------------------------------------------
a = [[1,5],
        [7,3],
        [3,5]
        ]
a1 = []
for i in range(len(a)):
    c = 0
    for j in range(len(a[i])):
        c += a[i][j]
    a1.append(c)
print(a1)
print(max(a1))