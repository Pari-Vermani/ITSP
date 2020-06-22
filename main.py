#This is the main file for calling all the functions in order.
#Import Libraries
import numpy as np
import pandas as pd
from matplotlib.image as mpimg
import os

#Import Functions
from Trajectory Recognition.signal_processing import *
from filename.innerfile import*

def main():
  #Import csv file with the data values
  acc_inputs=pd.read_csv("ITSP/____.csv")
  
  print('csv file read')
  
  #Calling the functions
  signal_mat= *signal_processing_func*(acc_inputs)
  print('Signal processing funstion called successfully')
  
