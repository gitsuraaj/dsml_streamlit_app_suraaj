import pandas as pd
import streamlit as stl
import yfinance as yf
import datetime

stl.write(
    """
    # Stock Price Analyser
    Shown are the stock prices of Apple
    """
)
#refer https://pypi.org/project/yfinance/ for functions available in yfinance package

#https://aroussi.com/post/python-yahoo-finance  - for function understanding

dicter={'AAPL': "Apple", "GOOG": "Google"}
ticker_symbol = stl.text_input('Stock Symbol', 'AAPL')

stl.write('The current ticker symbol is of:', dicter[ticker_symbol])

#ticker_symbol="AAPL"
ticker_data=yf.Ticker(ticker_symbol)

col1, col2 = stl.columns(2)

# Enter Start Date of the Analysis
with col1:
    start_date= stl.date_input ("Starting Date", datetime.date (2019,1,1))  #default value

# Enter End Date of the Analysis
with col1:
    end_date= stl.date_input ("Ending Date", datetime.date (2022,12,31))  #default value

# get historical market data
hist = ticker_data.history(period='1d', start=f'{start_date}', end=f'{end_date}')
# to show this in streamlit
df=stl.dataframe(hist)

#since stock prices are shown using a line chart, we'll go to https://docs.streamlit.io/
# documentation and using search functionality, we'll search for line chart

stl.write(f"""
## Closing price of {ticker_symbol} each day
""")
stl.line_chart(hist['Close'])


##### -------------------------------#########
col1, col2, col3 = stl.columns(3)

with col1:
   stl.header("A cat")
   stl.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   stl.header("A dog")
   stl.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   stl.header("An owl")
   stl.image("https://static.streamlit.io/examples/owl.jpg")
##### -------------------------------#########