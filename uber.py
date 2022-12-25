import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
import yfinance as yf
from functools import reduce

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

TICKERS=['AAPL','TSLA','AMD','META','MSFT']
@st.cache
def load_data():
    
    data_li=[]
    for ticker in TICKERS:
        df=yf.Ticker(ticker).history(period='5y',interval='1mo')['Close'].to_frame()
        df.rename({'Close':ticker},axis=1,inplace=True)
        data_li.append(df)
    data=reduce(lambda x,y: pd.merge(x,y,left_index=True,right_index=True,how='left'),data_li)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data()
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

tickers=st.multiselect("Choose tickers",TICKERS,["META","MSFT"])

st.line_chart(data[tickers])

st.subheader('Raw data')
st.write(data)