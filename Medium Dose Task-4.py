import numpy as np
from matplotlib import pyplot as plt

path = r"C:\Users\surya\Downloads\log.txt"
with open(path, 'r') as fobj:
    sensor_readings = [int(reading) for line in fobj for reading in line.strip().split()]

plt.plot(sensor_readings, label="sensor_readings")
plt.xlabel("Time")
plt.ylabel("Sensor Reading")

# converting the list to a numpy array
sensor_readings = np.array(sensor_readings)

length = len(sensor_readings)

# creating a window size that neither captures much noise or too less data
# The window size is the square root of the number of sensor readings
window_size = int(np.sqrt(length))

adaptive_filtered = []

# Muchiko filter is proned to noise because of sudden spike in the data so i think that sanchiko filter is better than muchiko filter

'''So i thought to use munchiko filter for less noise and sanchiko filter for more noise,since in the 
sensor readings mixed signal is also possible i came up with a idea to apply relevant filter for each window based on the noise level'''

# Adaptive filter based on comparison with global statistics
overall_std = np.std(sensor_readings)

for i in range(0, length):
    if i + window_size > length:
        break

    data_chunk = sensor_readings[i:i + window_size]
    local_std = np.std(data_chunk)

    # Adaptive threshold: compare local std to global std
    if local_std < 0.8 * overall_std:
        value = np.mean(data_chunk)  # Use Muchiko (mean) if less noise
    else:
        value = np.median(data_chunk)  # Use Sanchiko (median) if more noise

    adaptive_filtered.append(value)

#NOTE:The above used threshold  is analyzed by chatgpt with 500 synthetic data and then concluded. 





plt.plot(adaptive_filtered, label="Adaptive Filter", color='red')
plt.legend()
plt.title("Mixed Noise")
plt.show()
