# Question: Given a string, find the maximum number of times you can form the word "balloon" using the characters in the string.

from collections import Counter
def max_number_of_balloons(text):
    count = Counter(text)
    return min(
        count['b'],
        count['a'],
        count['l'] // 2,
        count['o'] // 2,
        count['n']
    )
    
text="loonbalxballpoon"
i=max_number_of_balloons(text)
print(i)
