# Question: Given an array of integers and a value k, find the number of unique pairs (i,j) where|arr[i] - arr[j]| = k 

from collections import Counter

def find(n, arr, k):
    abs_count = Counter(abs(x) for x in arr)
    result = set()
    for num in abs_count:
        if k == 0:
            if abs_count[num] > 1:
                result.add((num, num))
        else:
            if num + k in abs_count:
                result.add(tuple(sorted((num, num + k))))
    return len(result)
n = 4
arr = [1, 2, 1, 2]
k = 0
print(find(n, arr, k))  
