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

# Formatting of data
df_confirmed.rename({'Province/State': 'province', 'Country/Region': 'country', 'Date': 'date'}, axis=1, inplace=True)
df_deaths.rename({'Province/State': 'province', 'Country/Region': 'country', 'Date': 'date'}, axis=1, inplace=True)
df_recovered.rename({'Province/State': 'province', 'Country/Region': 'country', 'Date': 'date'}, axis=1, inplace=True)

# Raw data - with streamlit cache
@st.cache
def get_confirmed_melted(df):
  return df.melt(id_vars=["province", "country"], var_name='date', value_name='confirmed-count')
  #return data.sort_values(by='confirmed-count', axis=0, ascending=False)

@st.cache
def get_deaths_melted(df):
  return df.melt(id_vars=["province", "country"], var_name='date', value_name='death-count')
  #return data.sort_values(by='death-count', axis=0, ascending=False)

@st.cache
def get_recovered_melted(df):
  return df.melt(id_vars=["province", "country"], var_name='date', value_name='recovered-count')
  #return data.sort_values(by='recovered-count', axis=0, ascending=False)

# Cumulative data - with streamlit cache


# Add normalized columns to the three csv files
# Confirmed csv - add column named "norm-confirmed"

# Deaths csv - add column named "norm-deaths"

# Recovered csv - add column named "norm-recovered"


# Sidebar Title and description
st.sidebar.write("""
# Control data to display here
""")

if st.sidebar.checkbox('Show data for reported cases'):
  # Content in sidebar
  st.sidebar.write("""
  ### Reported number of covid cases for one specific country
  """)
  option = st.sidebar.selectbox(
      'Which country do you want to dislay?',
      get_confirmed_melted(df_confirmed)["country"].unique())
  # Content in main interface
  df_confirmed_melted = get_confirmed_melted(df_confirmed)
  chart_death = alt.Chart(df_confirmed_melted[df_confirmed_melted["country"] == option]).mark_line().encode(
    x=alt.X('date:T'),
    y=alt.Y('confirmed-count:Q'),
    color=alt.Color("country:N")
  ).properties(title="Confirmed number of cases for "+option)
  st.altair_chart(chart_death, use_container_width=True)
