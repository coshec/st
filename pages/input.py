import streamlit as st

qty=[0,0,0,0]
phase=[None,None,None,None]
watt=[0.5,0.5,0.5,0.5]
key_id=0
button_click=st.button('Done',key='btn_select')
if button_click:
    if len(appliances)> 1:
        tabs=st.tabs(appliances)
        for i,tab in enumerate(tabs):
            with tab:
                key_id+=1
                qty[i-1] = st.slider('Select quantity', 0, 10, 1,key=key_id)
                key_id+=1
                phase[i-1]=st.radio('Phase',['Single','3-phase'],key=key_id)
                key_id+=1
                watt[i-1]=st.number_input(label='Enter Wattage',key=key_id)
#st.write(f'Hello {name}!')
# Using object notation
if st.button('Done',key='btn_data'):
    df=pd.DataFrame({'Appliance':appliances,'Qty':qty,'Phase':phase,'Wattage':watt})
    st.write(df)
    # st.write(phase)
    # st.write(watt)
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
# x = st.slider('Select an integer x', 0, 10, 1)
# y = st.slider('Select an integer y', 0, 10, 1)
# df = pd.DataFrame({'x': [x], 'y': [y] , 'x + y': [x + y]}, index = ['addition row'])
# st.write(df)