import pandas as pd
import yfinance as yf
import streamlit as st
from datetime import datetime

st.markdown('# Analisando empresas')

st.text_input('Ticker Code:', key = 'tickercode', value = 'GOOG')
ticker = st.session_state.tickercode
data = yf.Ticker(ticker)

st.markdown(f'## Últimas notícias da {ticker}:')

data_news = pd.DataFrame(data.news)

data_news2 = data_news[['title', 'publisher', 'link', 'relatedTickers']]
st.dataframe(data_news2)

end_date = datetime.now().strftime('%Y-%m-%d')
data_hist = data.history(period = 'max', start = '2019-10-15', end = end_date, interval = '5d')
data_hist = data_hist.reset_index()

st.markdown('## Construa seu gráfico')

ey = st.selectbox('Eixo y:', data_hist.columns)
ex = st.selectbox('Eixo x:', data_hist.columns)

st.markdown(f'### Gráfico {ey} X {ex}')
st.line_chart(data_hist, x = ex, y = ey)


