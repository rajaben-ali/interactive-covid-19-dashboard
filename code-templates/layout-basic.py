import streamlit as st

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

# Space out the maps so the first one is 2x the size of the other three
c1, c2, c3, c4 = st.beta_columns((2, 1, 1, 1))

with c1:
  with st.beta_expander('C1'):
    st.write('Expanded contant C1')

with c2:
  with st.beta_expander('C2'):
    st.write('Expanded contant C2')

with c3:
  with st.beta_expander('C3'):
    st.write('Expanded contant C3')

with c4:
  with st.beta_expander('C4'):
    st.write('Expanded contant C4')


# Space out the maps so the second one is 2x the size of the other three
c5, c6, c7, c8 = st.beta_columns((1, 2, 1, 1))

with c5:
  with st.beta_expander('c5'):
    st.write('Expanded contant C5')

with c6:
  with st.beta_expander('c6'):
    st.write('Expanded contant C6')

with c7:
  with st.beta_expander('c7'):
    st.write('Expanded contant C7')

with c8:
  with st.beta_expander('c8'):
    st.write('Expanded contant C8')
