# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 18:28:51 2024

@author: vinic
"""
import pandas as pd
import numpy as np
import glob
import os
import matplotlib.pyplot as plt

########## START OF DATA IMPORT ##########

# Define the path to the folder containing data files
data_folder = "E:\\Git\\import spectra hr4000\\multespec" 

# Number of wavelengths
n_wavelength_effective = 1063  

# Row index of the first considered wavelength
skiprows = 1054  

# Number of samples
num_amost = 8  

# Calculate the number of columns based on the number of samples
ultcol = (num_amost * 2 + 1)

# Import the file (single file with all samples), read spectral data, filter wavelengths of interest.
nome_arquivo = "multespec.txt"
spect_Data = pd.read_csv(os.path.join(data_folder, nome_arquivo), delimiter='\t', header=None, skiprows=skiprows, nrows=n_wavelength_effective, usecols=range(1, ultcol, 2))
wavelengths = pd.read_csv(os.path.join(data_folder, nome_arquivo), delimiter='\t', header=None, skiprows=skiprows, nrows=n_wavelength_effective, usecols=[0])
spect_Data = np.transpose(np.array(spect_Data))
spect_Data = spect_Data[1:, :]
spect_Data_ml = np.transpose(spect_Data) # Samples separated by columns.

########## END OF DATA IMPORT ##########

# Plot spectral data 
# Create the figure and axes
fig, ax = plt.subplots(figsize=(10, 5))

# Spectral data of training and validation
ax.plot(wavelengths, np.transpose(spect_Data), linewidth=1.0)
ax.tick_params(direction='in')
ax.set_title("Spectral curves")
ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Relative Transmitted Intensity(%)") # Your optical parameter (reflectance, transmittance, scope, absorvance)
ax.set_xlim(475, 750)
ax.set_ylim(-10, 110)

plt.show()
