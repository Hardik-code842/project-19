# Code for 'diabetes_main.py' file.

# Importing the necessary Python modules.
import streamlit as st
import numpy as np 
import pandas as pd
import diabetes_plots
import diabetes_predict

import diabetes_home


# Configure your home page by setting its title and icon that will be displayed in a browser tab.
st.set_page_config(page_title = 'Early Diabetes Prediction Web App',
                    page_icon = 'random',
                    layout = 'wide',
                    initial_sidebar_state = 'auto'
                    )

# Loading the dataset.
@st.cache()
def load_data():
    # Load the Diabetes dataset into DataFrame.

    df = pd.read_csv('diabete_df.csv')
    df.head()

    # Rename the column names in the DataFrame.
    df.rename(columns = {"BloodPressure": "Blood_Pressure",}, inplace = True)
    df.rename(columns = {"SkinThickness": "Skin_Thickness",}, inplace = True)
    df.rename(columns = {"DiabetesPedigreeFunction": "Pedigree_Function",}, inplace = True)

    df.head() 

    return df

diabetes_df = load_data()

# Adding a navigation in the sidebar using radio buttons
# Create the 'pages_dict' dictionary to navigate.
pages_dict = {"Home": diabetes_home, 
           "Predict Diabetes": diabetes_predict, 
           "Visualise Decision Tree": diabetes_plots}
# Add radio buttons in the sidebar for navigation and call the respective pages based on user selection.
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Go to ",tuple(pages_dict.keys()))
if choice == "Home":
    diabetes_home.app()
else:
  selected_page = pages_dict[choice]
  selected_page.app(diabetes_df)
