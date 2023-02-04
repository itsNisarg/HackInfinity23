import streamlit as st
import psycopg2
import pandas as pd
import tensorflow as tf
import numpy as np
st.title("Crypto Ticker Predictor")

tickers = ['BTC']

if st.button("Predict"):
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Envy2002"
    )

    cur = conn.cursor()
    cur.execute(""" SELECT * from "RVNUSDT" """)
    rows = cur.fetchall()

    # Convert the results into a Pandas dataframe
    df = pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])
    df = df.loc[::-1].reset_index(drop=True).head()
    close_price = df[["close"]]
    new_model = tf.keras.models.load_model('fin.h5')
    x = np.array([close_price[-5:]])
    prediction = new_model.predict(x)
    prices = prediction[0]
    for ticker, price in zip(tickers, prices):
        st.write(f"{ticker}: {price}")



