import streamlit as st
import pandas as pd
st.title('Diesel Generator Size Calculator')
#name = st.text_input('whats your name', '')
appliances=st.multiselect("Choose appliances",['Air Conditioner','CF Bulb','Halogen light','Motor'],['CF Bulb'])
st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write('\
        The chart above shows some numbers I picked for you. \
        I rolled actual dice for these, so they\'re *guaranteed* to \
        be random. \
    ')
    st.image("https://static.streamlit.io/examples/dice.jpg")

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