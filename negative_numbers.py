# Question: Given a sorted matrix (rows and columns in non-increasing order), count the number of negative numbers efficiently.

def countNegatives(grid, n: int, m: int) -> int:
    count = 0
    row, col = n - 1, 0  		

    while row >= 0 and col < m:
        if grid[row][col] < 0:
            count += (m - col)  	
            row -= 1  		
        else:
            col += 1 	 	

    return count

n = int(input())  
m = int(input())  
row_list = [list(map(int, input().split())) for _ in range(n)]

print(countNegatives(row_list, n, m))
