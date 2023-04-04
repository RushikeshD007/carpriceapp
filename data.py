 # Import necessary modules
import streamlit as st
import home
import data
import predict
import plots
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
    st.header("View Data")
    # Add an expander and display the dataset as a static table within the expander.
    with st.beta_expander("View Dataset"):
        st.table(car_df)
    
    # ADD NEW CODE HERE.
    st.subheader("Columns Description:")
    if st.checkbox("Show summary"):
        st.table(car_df.describe())
# ADD NEW CODE FROM HERE
    beta_col1, beta_col2, beta_col3 = st.beta_columns(3)

    # Add a checkbox in the first column. Display the column names of 'car_df' on the click of checkbox.
    with beta_col1:
        if st.checkbox("Show all column names"):
            st.table(list(car_df.columns))

    # Add a checkbox in the second column. Display the column data-types of 'car_df' on the click of checkbox.
    with beta_col2:
      if st.checkbox('View columns data-types'):
        st.table(car_df.dtypes)
    # Add a checkbox in the third column followed by a selectbox which accepts the column name whose data needs to be displayed.
    with beta_col3:
      if st.checkbox("View columns data"):
        column = st.selectbox("select column", tuple(car_df.columns))
        st.write(car_df[column])