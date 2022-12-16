# Import Python Libraries
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import ticker
from matplotlib.ticker import AutoMinorLocator
from streamlit_option_menu import option_menu
from scipy.stats import norm
#Desarrollo de la interfaz
with st.sidebar:
    options = option_menu(menu_title="main menu",options=["Home", "Reservoir data"],icons=[])
#Distribución normal Bo
BO_norm = norm.rvs(loc=1.5, scale=0.5, size=100)
BO_norm = np.where(BO_norm < 1, 1, BO_norm)
BO_norm = np.where(BO_norm > 2, 2, BO_norm)
