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
df_confirmed = pd.read_csv("./data/time_series_covid19_confirmed_global.csv")
df_deaths = pd.read_csv("./data/time_series_covid19_deaths_global.csv")
df_recovered = pd.read_csv("./data/time_series_covid19_recovered_global.csv")

# Data Preparation - Cumulative data
# Confirmed cases
df_confirmed_cumul = df_confirmed.melt(id_vars=["Province/State", "Country/Region",'Lat', "Long"], var_name='Date', value_name='Count')
# Death cases
df_deaths_cumul = df_deaths.melt(id_vars=["Province/State", "Country/Region",'Lat', "Long"], var_name='Date', value_name='Count')
# Recovered cases
df_recovered_cumul = df_recovered.melt(id_vars=["Province/State", "Country/Region",'Lat', "Long"], var_name='Date', value_name='Count')

# Content in sidebar
st.sidebar.write("""
# Deaths number
""")
option = st.sidebar.selectbox(
    'Which country do you want to dislay?',
     df_deaths_cumul["Country/Region"].unique())

# Content in main interface
if option:
  'You selected:', option
else:
  'You have not selected an option'