import numpy as np


# Global variable to track the minimum path count
minimum = float('inf')  # Set to a very large number
path=[]

def shortest_path(area_map, map_size, dest_x, dest_y, i, j, path_count):
    global minimum  # Access the global variable
    global path
    # Out of bounds check
    if i < 0 or j < 0 or i >= map_size or j >= map_size:
        return
    
    # Destination reached, update minimum path
    if i == dest_x and j == dest_y:
        minimum = min(minimum, path_count)
        return  

    # Obstacle or already visited cell
    if area_map[i, j] == 0:
        return

    # Mark current position as visited (temporarily)
    area_map[i, j] = 0 
    path.append((i,j))

    # Explore all possible moves (N, S, E, W)
    shortest_path(area_map, map_size, dest_x, dest_y, i-1, j, path_count+1)  # Up
    shortest_path(area_map, map_size, dest_x, dest_y, i+1, j, path_count+1)  # Down
    shortest_path(area_map, map_size, dest_x, dest_y, i, j-1, path_count+1)  # Left
    shortest_path(area_map, map_size, dest_x, dest_y, i, j+1, path_count+1)  # Right

    # Backtrack: Unmark the position so other paths can use it
    area_map[i, j] = 1 
    path.pop() 


# reading the obstacles using file_object
file_path = r"c:\Users\surya\Downloads\obstacles.txt"
with open(file_path, 'r') as f_obj:
    obstacles = [list(map(int, line.split())) for line in f_obj]


#creating a array for storing obstacles
obstacles_array = np.array(obstacles)

# Find maximum distance to determine map size
maximum = np.max(obstacles_array)
map_size = 2 * maximum + 1
area_map = np.ones((map_size, map_size), dtype=int)

# Origin at center
centre_x = centre_y = map_size // 2

# N,E,S,W represents the absolute value of the corners of the obstacle from the origin


for (N, E, S, W) in obstacles_array:
   

   # converting those absolute distance into coordinates w.r.t to the central box(considered as initial point) of matrix
    x_start = centre_x - W  # West boundary 
    x_end = centre_x + E    # East boundary 
    y_start = centre_y - N  # North boundary   
    y_end = centre_y + S    # South boundary 

 
    area_map[y_start:y_end+1, x_start:x_end+1] = 0  

print("The map of the environment ")
print(area_map)

dest_y=centre_y-10

dest_x=centre_x-10

map_copy=area_map.copy()
shortest_path(map_copy,map_size,dest_x,dest_y,centre_x,centre_y,0)
print(minimum)