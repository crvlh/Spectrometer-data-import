# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:54:23 2024

@author: vinic
"""
import pandas as pd
import numpy as np
import glob
import os
import matplotlib.pyplot as plt

########## START OF DATA IMPORT ##########

# Define the path to the folder containing data files
data_folder = "E:\\Git\\import spectra hr4000" 

# Filter
n_wavelength_effective = 1063 # Number of wavelengths
skip_rows = 1062  # Row index of the first considered wavelength 

# Import files (multiple files, each file a sample), read spectral data, filter wavelengths of interest.
file_list = glob.glob(os.path.join(data_folder, "*.txt"))
file_list = sorted(file_list, key=lambda x: int(os.path.basename(x).split(".")[0]))
num_samples = len(file_list)

# Read spectral data from each file and reshape into a 2D array
spect_data = [pd.read_csv(file, delimiter='\t', skiprows=skip_rows, nrows=n_wavelength_effective, usecols=range(1, 2))
                  for file in file_list]
spect_data = np.reshape(np.array(spect_data), (num_samples, n_wavelength_effective))

# Read wavelengths from the first file
wavelengths = pd.read_csv(file_list[0], sep='\t', header=None, usecols=[0], skiprows=(skip_rows + 1),
                          nrows=n_wavelength_effective, index_col=None)

# Transpose spectral data array (samples as columns)
spect_data_ml = np.transpose(spect_data)

########## END OF DATA IMPORT ##########

# Plot spectral data of training/validation and test sets

# Create the figure and axes
fig, ax = plt.subplots(figsize=(10, 5))

# Spectral data of training and validation
ax.plot(wavelengths, np.transpose(spect_data), linewidth=1.0)
ax.tick_params(direction='in')
ax.set_title("Spectral curves")
ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Relative Transmitted Intensity(%)") # Your optical parameter (reflectance, transmittance, scope, absorvance)
ax.set_xlim(475, 750)
ax.set_ylim(-10, 110)

plt.show()