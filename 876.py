# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
#--------------------------------------------------
head = []
val = int(input('1 <= val <= 100: '))
for i in range(1,val+1):
    head.append(i)
print(head[len(head) // 2:])
#--------------------------------------------------
head = [1,2,3,4,5,6]
print(head[len(head) // 2:])
