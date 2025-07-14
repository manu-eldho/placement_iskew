# Question: Given a list of strings, group all anagrams together and print each group on a new line.

from collections import defaultdict

def group_anagrams(strs):
    anagram_groups = defaultdict(list)
    for word in strs:
        key = ''.join(sorted(word)) 
        anagram_groups[key].append(word)
    for group in anagram_groups.values():
        print(' '.join(group))

N = int(input())
strs = input().split()
group_anagrams(strs)
