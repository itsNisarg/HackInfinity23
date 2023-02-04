import streamlit as st
import psycopg2
import pandas as pd
import tensorflow as tf
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
st.title("Crypto Ticker Predictor")

tickers = ['BTC']

if st.button("Predict"):
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="admin"
    )

    cur = conn.cursor()
    cur.execute(""" SELECT * from "BTCUSDT" """)
    rows = cur.fetchall()

    # Convert the results into a Pandas dataframe
    df = pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])
    df = df.loc[::-1].reset_index(drop=True)
    close_price = df[["close"]]
    new_model = tf.keras.models.load_model('fin.h5')
    x = np.array([close_price[0:5]])
    array = np.array([close_price[0:50]])
    prediction = new_model.predict(x)
    prices = prediction[0]
    for ticker, price in zip(tickers, prices):
        st.write(f"{ticker}: {price}")
    
    # st.write(array)
    # fig = go.Figure(data=go.Scatter(x=np.arange(0,50, 1), y=array, mode='lines', line=dict(color="white")), layout_yaxis_range=[25000,26000])
    # st.line_chart(array.reshape(-1, 1))

    # fig = go.Figure(data=[go.Scatter(y=[1, 3, 2], line=dict(color="crimson"))],layout=dict(title=dict(text="Estimated Price")))


    fig = px.line(df,x="time", y="close", color_discrete_sequence=['f9a03f'], range_x=[df["time"][0], df["time"][len(df["time"])-1]], range_y=[20000, 25000])
    fig.add_trace(go.Scatter(y=np.append(close_price, price), mode='lines', line=dict(color="crimson")))
    st.write(fig)

    st.write(prices)



