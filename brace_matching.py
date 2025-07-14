# Question: Given a string containing only '{' and '}' braces, check if the braces are properly matched.

n = input()

count_left_braces = n.count('{')
count_right_braces = n.count('}')

if count_left_braces == count_right_braces and not n.endswith('{'):
    print("Matching")
else:
    print("Not Matching")
