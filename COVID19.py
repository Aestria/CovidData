import numpy as np
import scipy as sy
from scipy import special

import matplotlib as mp
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.cm as cm
import matplotlib.colors as colors
from matplotlib.colors import LogNorm
heatmapcolour = cm.coolwarm
heatmapcolour.set_bad('w',1.)
plt.rcParams.update({'font.size': 20})
mp.rc('xtick', labelsize=20)
mp.rc('ytick', labelsize=20)

import uncertainties
from uncertainties import ufloat
from uncertainties import umath
from uncertainties.umath import *  # sin(), etc.
from uncertainties import unumpy  # Array manipulation
from uncertainties import ufloat_fromstr

import sympy as sm
from sympy.solvers.ode import dsolve
sm.init_printing()

import pandas as pd
