# Spectral Data Importer for Machine Learning and Spectral Data Processing

This repository contains two Python scripts designed to facilitate the import of spectral data for machine learning implementations or other types of spectral data processing in Python.

## Scripts
import_spectra_sf.py: Use this script when spectral data is stored in a single .txt file.

import_spectra_mf.py: Use this script when samples are divided into multiple .txt files.

## Usage
1. Adjust the **skiprows** parameter to the line number of the first wavelength evaluated, varying according to the interrogated optical system.
2. Set **n_wavelength_effective** to the number of wavelengths to be used, defining the spectral band and width evaluated.
3. Define the number of samples (**n_amost** parameter) and **update the directory** of the data accordingly.

## Plotting
The code generates a simple plot with spectral curves. By default, the y-axis represents "transmittance," but this can be modified according to the optical data saved in the spectrometer (e.g., transmission, absorption, scope, etc.).

