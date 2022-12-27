import streamlit as st
import pandas as pd
st.title('Diesel Generator Size Calculator')
#name = st.text_input('whats your name', '')
appliances=st.multiselect("Choose appliances",['Air Conditioner','CF Bulb','Halogen light','Motor'],['CF Bulb'])
qty=[0,0,0,0]
phase=[None,None,None,None]
watt=[0.5,0.5,0.5,0.5]
if len(appliances)> 1:
    tabs=st.tabs(appliances)
    for i,tab in enumerate(tabs):
        with tab:
            qty[i-1] = st.slider('Select quantity', 0, 10, 1)
            phase[i-1]=st.radio('Phase',['Single','3-phase'])
            watt[i-1]=st.number_input('Enter Wattage',min_value=.5,max_value=120000)
#st.write(f'Hello {name}!')
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
x = st.slider('Select an integer x', 0, 10, 1)
y = st.slider('Select an integer y', 0, 10, 1)
df = pd.DataFrame({'x': [x], 'y': [y] , 'x + y': [x + y]}, index = ['addition row'])
st.write(df)