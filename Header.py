# Import Libraries
import datetime

import numpy as np
import seaborn as sns

from matplotlib import colors
import matplotlib.pyplot as plt

import bokeh.io
from bokeh.resources import INLINE
from bokeh.layouts import row, gridplot
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show, output_file

import pandas as pd

import scipy as sp
import scipy.io as sio

from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler


# Allow plotting inline
%matplotlib inline
plt.rcParams['figure.figsize'] = (12,8)

bokeh.io.output_notebook(INLINE)   # The INLINE is necessary in jupyter, not in scripts
