import pickle
import george
import scipy
import sncosmo

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import astropy.units as u
import astropy.constants as c

from pyentrp import entropy as ent
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern
from astropy.io import ascii
from matplotlib.ticker import LinearLocator
from matplotlib import cm

wavelengths = {
    'U': 3663,
    'B': 4361,
    'V': 5448,
    'R': 6407,
    'I': 7980,
    'J': 12200,
    'H': 16300,
    'K': 21900,
    'UVM2': 2310,
    'UVW1': 2910,
    'UVW2': 2120,
    
}


sed_mag = pd.read_csv('2011fe.csv')


# Make data.
all_times= np.unique(sed_mag['Time'])
all_wavelengths = np.unique(sed_mag['Effective Wavelength'])

flux_grid =np.zeros([len(all_times), len(all_wavelengths)])

for i, t in enumerate(all_times):
    
    flux_grid[i, :] = sed_mag[sed_mag['Time']==t]['flux']
    
flux_grid.shape, all_times.shape, all_wavelengths.shape

plt.plot(all_wavelengths, flux_grid[100, :])
plt.show()

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = all_wavelengths
Y = all_times
X, Y = np.meshgrid(X, Y)
Z = flux_grid


ax.zaxis._set_scale('log')

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)


# Customize the z axis.
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')



# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()