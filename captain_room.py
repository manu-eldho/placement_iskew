# Question: In a hotel, there are k members in each family except the captain's family which has only 1 member. Given a list of room numbers, find the captain's room number.

from collections import Counter

def find_captain_room(k, room_list):
    freq = Counter(room_list)
    for room, count in freq.items():
        if count != k:
            print(room)
            return

k = 5
room_list = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]

find_captain_room(k, room_list)
