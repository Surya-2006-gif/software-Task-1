import numpy as np


with open('log.txt','r') as fobj:

    sensor_readings = [int(reading) for line in fobj for reading in line.strip().split()]



 #converting the list to a numpy array
sensor_readings = np.array(sensor_readings)


