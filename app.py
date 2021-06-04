import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# This line needs to be the first one to be called in the script
# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

st.title('Dashboard for Covid19 data')
with st.beta_expander('Project description'):
  st.write("""
  The "interactive covid-19 dashboard" project is based on the dataset provided
  by [Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19).
  The dashboard allows users to visualize the number of Covid-19 cases or deaths per country as a function of time.
  """)

# Load the csv files
columns_to_be_removed = ['Lat', 'Long']
df_confirmed = pd.read_csv("./data/time_series_covid19_confirmed_global.csv").drop(columns_to_be_removed, axis = 'columns')
df_deaths = pd.read_csv("./data/time_series_covid19_deaths_global.csv").drop(columns_to_be_removed, axis = 'columns')
df_recovered = pd.read_csv("./data/time_series_covid19_recovered_global.csv").drop(columns_to_be_removed, axis = 'columns')

# Cumulative data - with streamlit cache
@st.cache
def get_confirmed_cumul(df):
  return df.melt(id_vars=["Province/State", "Country/Region"], var_name='Date', value_name='Confirmed-Count')

@st.cache
def get_deaths_cumul(df):
  return df.melt(id_vars=["Province/State", "Country/Region"], var_name='Date', value_name='Death-Count')

@st.cache
def get_recovered_cumul(df):
  return df.melt(id_vars=["Province/State", "Country/Region"], var_name='Date', value_name='Recovered-Count')

# Content in sidebar
st.sidebar.write("""
# Deaths number
""")
option = st.sidebar.selectbox(
    'Which country do you want to dislay?',
     get_confirmed_cumul(df_confirmed)["Country/Region"].unique())
