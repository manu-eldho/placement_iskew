# Question: Given a simulation string with events (C/U for people coming, R/L for people leaving), find the minimum number of chairs needed.

def min_chair(simulation):
    chairs = 0
    total_chairs = 0

    for event in simulation:
        if event in ['C', 'U']:
            if chairs > 0:
                chairs -= 1  
            else:
                total_chairs += 1  
        elif event in ['R', 'L']: 
            chairs += 1  

    return total_chairs
sim = input()
print(min_chair(sim))
