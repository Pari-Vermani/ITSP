# %load signal_processing.py

"""
signal_processing.py
~~~~~~~~~~

A module to implement the signal preprocessing of which consists of: Calibration( to remove drift errors and offsets from the raw signals )
A moving average filter( to remove high frequency noise from raw data ), a high-pass filter( to remove gravitational acceleration from raw data ) and normalization*. It is not optimized, and omits many desirable features.
"""

#### Libraries
# Third-party libraries
import numpy as np

filename = 'input.csv'

sensor_input = np.genfromtxt(filename, delimiter=',')
# Assuming input is a N x 3 matrix where N is the number of readings
N = np.size(sensor_input, 0)
# Calculating the magnitude of readings(indirectly gravity) when the accelerometer is held idle for a few ms
g_mag = ((sensor_input[0, 0] + sensor_input[1, 0] + sensor_input[2, 0])/3)**2 + ((sensor_input[0, 1] + sensor_input[1, 1] + sensor_input[2, 1])/3)**2 +((sensor_input[0, 2] + sensor_input[1, 2] + sensor_input[2, 2])/3)**2
g_mag = np.sqrt(g_mag)

# Calling transformation matrix, output will be shrunk to N x 2 matrix
sensor_input = rot(sensor_input, g_mag)

# Calling moving average filter
sensor_input = ma_filter(sensor_input, N)

# Calling high pass filter
sensor_input = high_pass(sensor_input, g_mag, N)

# Calling normalisation function
sensor_input = norm(sensor_input)

# Define transformation matrix
def rot(sensor_input, g_mag):
    

# Define moving average filter
def ma_filter(sensor_input, N):

    # Assuming a variable n which is the number of recent readings we take an average over
    n = 4
    filtered_output = np.zeros((N - n + 1, 3))
    
    for i in range(0, N - n + 1):
        mean = np.zeros((1, 2))
        for j in range(i, i + n):
            filtered_output[i, 1] = filtered_output[i, 1] + sensor_input[j, 1]
            filtered_output[i, 0] = filtered_output[i, 0] + sensor_input[j, 0]

        filtered_output[i, 1] = filtered_output[i, 1] / n
        filtered_output[i, 0] = filtered_output[i, 0] / n

    return filtered_output

# Define high pass filter
def high_pass(sensor_input, g_mag, N):
    
    # Subtracting g from y-coordinates
    for i in range(0, N):
        sensor_input[i, 1] = sensor_input[i, 1] - g_mag;
    return sensor_input
    
# Define normalisation function
def norm(sensor_input):
    
