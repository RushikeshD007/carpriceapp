import streamlit as st
import home
import data
import predict
import plots
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
# S5.1: Configure the home as directed above.
def app():
	st.header("Car Price Prediction App")
	st.text("""
            This web app allows a user to predict the prices of a car based on their 
            engine size, horse power, dimensions and the drive wheel type parameters.
        	""")