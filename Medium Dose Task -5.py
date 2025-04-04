# conversion of Eulers representation to quaternion
import numpy as np


def euler_to_quaternion(roll, pitch, yaw):
    
    cy = np.cos(yaw * 0.5) #cosine of half of the yaw angle
    sy = np.sin(yaw * 0.5) #sine of half of the yaw angle
    cp = np.cos(pitch * 0.5) #cosine of half of the pitch angle
    sp = np.sin(pitch * 0.5)    #sine of half of the pitch angle
    cr = np.cos(roll * 0.5) #cosine of half of the roll angle
    sr = np.sin(roll * 0.5) #sine of half of the roll angle

    w = cr * cp * cy + sr * sp * sy
    x = sr * cp * cy - cr * sp * sy
    y = cr * sp * cy + sr * cp * sy
    z = cr * cp * sy - sr * sp * cy

    return w, x, y, z






#getting the euler angles in radians
pitch=int(input("Enter the orientation w.r.t y-axis in radians: "))
roll=int(input("Enter the orientation w.r.t x-axis in radians: "))
yaw=int(input("Enter the orientation w.r.t z-axis in radians: "))



print("The quaternion representation of the given euler angles is: ",euler_to_quaternion(roll,pitch,yaw))
