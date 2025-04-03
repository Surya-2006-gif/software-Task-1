import numpy as np
from math import sqrt

#Getting input for the markers coordinates 
X = int(input("Enter the x coordinate of the destination: "))
Y = int(input("Enter the y coordinate of the destination: "))

# Global position of the marker,w.r.t to the origin
marker_global = np.array([X, Y, -60])

#THe arrived coordinate or the coordinates with error
rover_stopped = np.array([X, Y - 0.55, -60])

def change_frame_of_reference(marker_global, rover_stopped):
    #Returns marker's position relative to the rover_stopped coordinatees
    return marker_global - rover_stopped  # The result will be [0, 0.55, 0]

def compute_distances(marker_global, rover_stopped):
    
    # Distance in origin frame (origin to marker)
    dist_global = sqrt(marker_global[0]**2 + marker_global[1]**2 + marker_global[2]**2)
    
    # Distance in rover's frame (rover_stopped to marker)
    relative_pos = change_frame_of_reference(marker_global, rover_stopped)
    dist_rover_frame = sqrt(relative_pos[0]**2 + relative_pos[1]**2 + relative_pos[2]**2)
    
    return dist_global, dist_rover_frame


relative_pos = change_frame_of_reference(marker_global, rover_stopped)
dist_global, dist_rover = compute_distances(marker_global, rover_stopped)

print(f"Marker's position in rover's frame: {relative_pos}")
print(f"Distance in global frame: {dist_global:.2f} meters")
print(f"Distance in rover's frame: {dist_rover:.2f} meters")