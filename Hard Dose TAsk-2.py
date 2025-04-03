import numpy as np
from math import sqrt
def find_distance(perceived_width):
     
     real_width=17
    #alpha here represents FOV
     alpha =55
     frame_height=720
     frame_width=1280
     diagonal_length= sqrt((frame_height)**2+(frame_width)**2)

     f=diagonal_length/2*(np.tan(alpha/2))

     """  percieved_width/focus=real_width/distance"""

     return (real_width*f)/perceived_width

