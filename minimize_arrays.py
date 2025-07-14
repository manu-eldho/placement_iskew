# Question: Given two arrays of equal length, rearrange them to minimize the sum of products of corresponding elements.

n=int(input())
v1=list(map(int, input().split(" ")))
v2=list(map(int, input().split(" ")))

v1=sorted(v1)
v2.sort(reverse=True)

s=0
for i in range(n):
    s+=v1[i]*v2[i]
print(s
