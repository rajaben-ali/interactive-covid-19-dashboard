import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px

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
@st.cache
def load_data():
  columns_to_be_removed = ['Lat', 'Long']
  confirmed = pd.read_csv("./data/time_series_covid19_confirmed_global.csv").drop(columns_to_be_removed, axis = 'columns')
  deaths = pd.read_csv("./data/time_series_covid19_deaths_global.csv").drop(columns_to_be_removed, axis = 'columns')
  recovered = pd.read_csv("./data/time_series_covid19_recovered_global.csv").drop(columns_to_be_removed, axis = 'columns')
  return confirmed, deaths, recovered

df_confirmed, df_deaths, df_recovered = load_data()

# Formatting of data
@st.cache
def format_data():
  df_confirmed.rename({'Province/State': 'province', 'Country/Region': 'country', 'Date': 'date'}, axis=1, inplace=True)
  df_deaths.rename({'Province/State': 'province', 'Country/Region': 'country', 'Date': 'date'}, axis=1, inplace=True)
  df_recovered.rename({'Province/State': 'province', 'Country/Region': 'country', 'Date': 'date'}, axis=1, inplace=True)

format_data()

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

if st.sidebar.checkbox('Reported cases'):
  # Content in sidebar
  st.sidebar.write("""
  ### Reported number of covid cases for one specific country
  """)
  option_confirmed = st.sidebar.selectbox(
      'Cases - Which country do you want to dislay?',
      get_confirmed_melted(df_confirmed)["country"].unique())
  # Content in main interface
  df_confirmed_melted = get_confirmed_melted(df_confirmed)

  # plot
  st.write('### Reported number of covid cases in '+option_confirmed)
  fig = px.line(df_confirmed_melted[df_confirmed_melted["country"] == option_confirmed], x="date", y="confirmed-count", hover_name="confirmed-count",
          line_shape="spline", render_mode="svg")
  st.plotly_chart(fig)

if st.sidebar.checkbox('Death cases'):
  # Content in sidebar
  st.sidebar.write("""
  ### Death number from covid cases for one specific country
  """)
  option_death = st.sidebar.selectbox(
      'Death - Which country do you want to dislay?',
      get_deaths_melted(df_deaths)["country"].unique())
  # Content in main interface
  df_death_melted = get_deaths_melted(df_deaths)

  # plot
  st.write('### Death number of people from covid in '+option_death)
  fig_death = px.line(df_death_melted[df_death_melted["country"] == option_death], x="date", y="death-count", hover_name="death-count",
          line_shape="spline", render_mode="svg")#, animation_frame="date")
  st.plotly_chart(fig_death)


if st.sidebar.checkbox('Recovered cases'):
  # Content in sidebar
  st.sidebar.write("""
  ### Recovered number from covid cases for one specific country
  """)
  option_recov = st.sidebar.selectbox(
      'Recovered - Which country do you want to dislay?',
      get_recovered_melted(df_recovered)["country"].unique())
  # Content in main interface
  df_recovered_melted = get_recovered_melted(df_recovered)

  # plot
  st.write('### Recovered number of people from covid in '+option_recov)
  fig_conf = px.line(df_recovered_melted[df_recovered_melted["country"] == option_recov], x="date", y="recovered-count", hover_name="recovered-count",
          line_shape="spline", render_mode="svg")#, animation_frame="date")
  st.plotly_chart(fig_conf)