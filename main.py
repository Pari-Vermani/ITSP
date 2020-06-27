#This is the main file for calling all the functions in order.

#Import Libraries
import numpy as np
import pandas as pd
from matplotlib.image as mpimg
import os

#Import Functions
from Trajectory Recognition.signal_processing import *
# from filename.innerfile import* (for image generation file)

def main():
 #Variables used:
 #signal_mat: an Nx3 matrix
 
  #Calling the functions
  signal_mat= signal_processing()
  print('Signal processing function called successfully')
  image_gen(signal_mat)
  print('Image Generation function called successfully')
  
  
