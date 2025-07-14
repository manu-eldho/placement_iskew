# Question: Read two matrices of the same dimensions and compute their element-wise sum.

r, c = input().split(' ')      
rows = int(r)
cols = int(c)

rowlist = []              
rowlist2 = []  

for i in range(rows):
    rowlist.append(input().split(' '))

for j in range(rows):
    rowlist2.append(input().split(' '))

print('First Matrix:')
for row in rowlist:
    for i in row:
        print(i, end=' ')
    print()

print('Second Matrix:')
for row in rowlist2:
    for i in row:
        print(i, end=' ')
    print()

print('Sum of the two matrices is:')
for i in range(rows):
    for j in range(cols):
        sum_val = int(rowlist[i][j]) + int(rowlist2[i][j])
        print(sum_val, end=' ')
    print()
