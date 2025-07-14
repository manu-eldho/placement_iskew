# Question: You are given a natural number N. Your task is to count how many times the digit 0 appears in all the numbers from 1 to N (inclusive).

def count_zeros(n):
    count = 0
    factor = 1
    while factor <= n:
        lower = n % factor
        curr = (n // factor) % 10
        higher = n // (factor * 10)
        if curr == 0:
            count += higher * factor
        else:
            count += higher * factor

        if curr == 0:
            count += lower + 1

        factor *= 10
    return count

print(count_zeros(105))
