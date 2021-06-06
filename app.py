import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px

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
  df_confirmed.rename({'Province/State': 'province', 'Country/Region': 'country'}, axis=1, inplace=True)
  df_deaths.rename({'Province/State': 'province', 'Country/Region': 'country'}, axis=1, inplace=True)
  df_recovered.rename({'Province/State': 'province', 'Country/Region': 'country'}, axis=1, inplace=True)

format_data()

# Raw data - with streamlit cache
@st.cache
def get_confirmed_melted(df):
  df = df.melt(id_vars=["province", "country"], var_name='date', value_name='confirmed-count')
  df['date'] = pd.to_datetime(df['date'])
  return df
  #return data.sort_values(by='confirmed-count', axis=0, ascending=False)

@st.cache
def get_deaths_melted(df):
  df = df.melt(id_vars=["province", "country"], var_name='date', value_name='death-count')
  df['date'] = pd.to_datetime(df['date'])
  return df
  #return data.sort_values(by='death-count', axis=0, ascending=False)

@st.cache
def get_recovered_melted(df):
  df = df.melt(id_vars=["province", "country"], var_name='date', value_name='recovered-count')
  df['date'] = pd.to_datetime(df['date'])
  return df
  #return data.sort_values(by='recovered-count', axis=0, ascending=False)

# Cumulative data - with streamlit cache
# TODO:

# TODO: Add normalized columns to the three csv files

# Useful functions
def get_daterange_str(date_col, custom=False):
  if custom:
    date_range = str(global_month) +"-"+ str(global_year)
    return " in " + date_range
  start_d = date_col.dt.date.min()
  end_d = date_col.dt.date.max()
  return " from " + str(start_d.day) +"-"+ str(start_d.month) +"-"+ str(start_d.year) \
    + " to " + str(end_d.day) +"-"+ str(end_d.month) +"-"+ str(end_d.year)

@st.cache
def get_available_years():
  return list(np.unique(np.concatenate([get_confirmed_melted(df_confirmed)['date'].dt.year.unique(), \
      get_deaths_melted(df_deaths)['date'].dt.year.unique(), \
      get_recovered_melted(df_recovered)['date'].dt.year.unique()]), axis=0))

# End of useful functions

# Sidebar Title and description
st.sidebar.write("""
# Control data to display here
""")

with st.sidebar.beta_expander('Selection of datetime'):
  special_timeline = st.checkbox('Choose a specific timeline')
  if special_timeline:
    option_years = get_available_years()
    global_year = st.radio('Select year', option_years)
    global_month = st.slider('Select month', min_value=1, max_value=12)
  else:
    st.write("No specific timeline is used, the dashboard will display the overall timeline.")
    global_year = None
    global_month = None

with st.sidebar.beta_expander('Selection of counting method'):
  global_method = st.radio('Select method', ["number","cumulated number", "7-day rolling average"])

# TODO: Cache the variable 'all_possible_countries'
all_possible_countries = np.unique(np.concatenate((get_confirmed_melted(df_confirmed)["country"].unique(),
  get_deaths_melted(df_deaths)["country"].unique(),
  get_recovered_melted(df_recovered)["country"].unique()), 0))

global_country = st.sidebar.selectbox(
      'Which country do you want to dislay?',
      all_possible_countries)

global_case_type = st.sidebar.radio('Select case types', ["confirmed","deaths", "recovered"]) # Dynamically get possible years from datasets

# End of sidebar code

# Start of plots
if (global_case_type == "confirmed"):
  # confirmed cases
  conf_data = get_confirmed_melted(df_confirmed)
  # plot
  st.write('### Reported number of covid cases in '+global_country)

  # Check if the user choose a specific timeline
  if special_timeline:
    special_df_conf = conf_data[conf_data["country"] == global_country]
    special_df_conf = special_df_conf[np.logical_and(special_df_conf["date"].dt.month == global_month, special_df_conf["date"].dt.year == global_year)]

    # Check if data is available for selected timeline
    if not special_df_conf.empty:
      conf_fig = px.line(special_df_conf, x="date", y="confirmed-count", hover_name="confirmed-count",
            title=global_country+ get_daterange_str(special_df_conf["date"], custom=True),
            labels={"confirmed-count":"number"},
            color="country",
            line_shape="spline", render_mode="svg")
      conf_fig.update_layout(hovermode="x")
      st.plotly_chart(conf_fig)
    else:
      # no dataframe available for selected datetime
      st.write("No data is available for the selected timeline, you can change the timeline parameter on the sidebar.")
  else:
    conf_fig = px.line(conf_data[conf_data["country"] == global_country], x="date", y="confirmed-count", hover_name="confirmed-count",
            title=global_country+ get_daterange_str(conf_data[conf_data["country"] == global_country]["date"]),
            labels={"confirmed-count":"number"},
            color="country",
            line_shape="spline", render_mode="svg")
    conf_fig.update_layout(hovermode="x")
    st.plotly_chart(conf_fig)
elif (global_case_type == 'deaths'):
  # death cases
  death_data = get_deaths_melted(df_deaths)
  # plot
  st.write('### Death number of covid cases in '+global_country)

  # Check if the user choose a specific timeline
  if special_timeline:
    special_df_death = death_data[death_data["country"] == global_country]
    special_df_death = special_df_death[np.logical_and(special_df_death["date"].dt.month == global_month, special_df_death["date"].dt.year == global_year)]

    if not special_df_death.empty:
      death_fig = px.line(special_df_death, x="date", y="death-count", hover_name="death-count",
              title=global_country+ get_daterange_str(special_df_death["date"], custom=True),
              labels={"death-count":"number"},
              color="country",
              line_shape="spline", render_mode="svg")
      death_fig.update_layout(hovermode="x")
      st.plotly_chart(death_fig)
    else:
      # no dataframe available for selected datetime
      st.write("No data is available for the selected timeline, you can change the timeline parameter on the sidebar.")
  else:
    # No specific timeline is selected, display all available timeline
    death_fig = px.line(death_data[death_data["country"] == global_country], x="date", y="death-count", hover_name="death-count",
            title=global_country+ get_daterange_str(death_data[death_data["country"] == global_country]["date"]),
            labels={"death-count":"number"},
            color="country",
            line_shape="spline", render_mode="svg")
    death_fig.update_layout(hovermode="x")
    st.plotly_chart(death_fig)
else:
  # Consider recovered
  recov_data = get_recovered_melted(df_recovered)
  # plot
  st.write('### Recovered case of covid in '+global_country)

  # Check if the user choose a specific timeline
  if special_timeline:
    special_df_recov = recov_data[recov_data["country"] == global_country]
    special_df_recov = special_df_recov[np.logical_and(special_df_recov["date"].dt.month == global_month, special_df_recov["date"].dt.year == global_year)]

    if not special_df_recov.empty:
      recov_fig = px.line(special_df_recov, x="date", y="recovered-count", hover_name="recovered-count",
                title=global_country+ get_daterange_str(special_df_recov["date"], custom=True),
                labels={"recovered-count":"number"},
                color="country",
                line_shape="spline", render_mode="svg")
      recov_fig.update_layout(hovermode="x")
      st.plotly_chart(recov_fig)
    else:
      # no dataframe available for selected datetime
      st.write("No data is available for the selected timeline, you can change the timeline parameter on the sidebar.")
  else:
    # No specific timeline is selected, display all available timeline
    recov_fig = px.line(recov_data[recov_data["country"] == global_country], x="date", y="recovered-count", hover_name="recovered-count",
            title=global_country+ get_daterange_str(recov_data[recov_data["country"] == global_country]["date"]),
            labels={"recovered-count":"number"},
            color="country",
            line_shape="spline", render_mode="svg")
    recov_fig.update_layout(hovermode="x")
    st.plotly_chart(recov_fig)
