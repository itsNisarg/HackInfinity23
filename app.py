from sklearn.preprocessing import MinMaxScaler

import datetime
import streamlit as st
import psycopg2
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import tensorflow as tf

st.image("https://upload.wikimedia.org/wikipedia/commons/4/46/Bitcoin.svg")
st.title("Real time BTC/USDT future price predictor ")
st.empty()
st.empty()
st.empty()

fig = None
col1, col2, col3 = st.columns(3)

with col1:
   if st.button("Predict (Nxt 5-mins)"):
       conn = psycopg2.connect(
           host="localhost",
           database="postgres",
           user="postgres",
           password="Envy2002"
       )

       cur = conn.cursor()
       cur.execute(""" SELECT * from "curren" """)
       rows = cur.fetchall()

       # Convert the results into a Pandas dataframe
       df = pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])
       df = df.reindex(index=df.index[::-1])

       close_price = df[["close"]]
       scaler = MinMaxScaler(feature_range=(0, 1))
       close_price = scaler.fit_transform(close_price)
       new_model = tf.keras.models.load_model('5pred.h5')
       x = np.array([close_price[9::-1]])
       # array = np.array([close_price[0:50]])
       prediction = new_model.predict(x)
       prediction = scaler.inverse_transform(prediction)
       prices = prediction[0]
       df = df.iloc[:150]
       df = df.loc[::-1].reset_index(drop=True)
       close_price = df["close"]




       timer_add = []
       tempo = df['close'][len(df["close"]) - 1]
       time_stamp = df["time"][len(df["time"]) - 1]
       fig = px.line(df, x="time", y="close", color_discrete_sequence=['#f9a03f'],
                     range_x=[df["time"][0], df["time"][len(df["time"]) - 1]])

       for i in range(0, 5):
           # Add a timedelta to get the next time stamp
           next_dt = time_stamp + datetime.timedelta(seconds=60)
           timer_add.append(next_dt)
           time_stamp = next_dt
       prices = prices + (tempo - prices[0])
       # sss
    #    predictDf = pd.DataFrame({'time': timer_add, 'close': prices})
    #    st.write(predictDf)
    #    fig = px.line(predictDf, x="time", y="close", color_discrete_sequence=['#f9a03f'],
    #                  range_x=[df["time"][0], df["time"][len(df["time"]) - 1]])
    #    fig.add_trace(go.Scatter(x=timer_add, y=close_price, mode='lines', line=dict(color="crimson")))
    # #  sss

       # st.write(fig)
       fig.add_trace(go.Scatter(name="future_pred",x=timer_add, y=prices, mode='lines', line=dict(color="crimson")))
       fig['layout']['xaxis'].update(autorange=True)
       # st.write(fig)

with col2:
   if st.button("Predict (Nxt 10-mins)"):
       conn = psycopg2.connect(
           host="localhost",
           database="postgres",
           user="postgres",
           password="Envy2002"
       )

       cur = conn.cursor()
       cur.execute(""" SELECT * from "curren" """)
       rows = cur.fetchall()

       # Convert the results into a Pandas dataframe
       df = pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])
       df = df.reindex(index=df.index[::-1])

       close_price = df[["close"]]
       scaler = MinMaxScaler(feature_range=(0, 1))
       close_price = scaler.fit_transform(close_price)
       new_model = tf.keras.models.load_model('10pred.h5')
       x = np.array([close_price[29::-1]])
       # array = np.array([close_price[0:50]])
       prediction = new_model.predict(x)
       prediction = scaler.inverse_transform(prediction)
       prices = prediction[0]
       df = df.iloc[:150]
       df = df.loc[::-1].reset_index(drop=True)
       close_price = df["close"]

       fig = px.line(df, x="time", y="close", color_discrete_sequence=['#f9a03f'],
                     range_x=[df["time"][0], df["time"][len(df["time"]) - 1]])
       timer_add = []
       tempo = df['close'][len(df["close"]) - 1]
       time_stamp = df["time"][len(df["time"]) - 1]

       for i in range(0, 150):
           # Add a timedelta to get the next time stamp
           next_dt = time_stamp + datetime.timedelta(seconds=60)
           timer_add.append(next_dt)
           time_stamp = next_dt
       prices = prices + (tempo - prices[0])

       # predictDf = pd.DataFrame({'time': timer_add, 'close': prices})
       # st.write(predictDf)
       # fig = px.line(predictDf, x="time", y="close", color_discrete_sequence=['#f9a03f'],
       #               range_x=[df["time"][0], df["time"][len(df["time"]) - 1]])
       # fig.add_trace(go.Scatter(x=timer_add, y=close_price, mode='lines', line=dict(color="crimson")))
       #  fig.add_trace(go.Scatter(x=timer_add, y=prices, mode='lines', line=dict(color="crimson")))
       # st.write(fig)
       fig.add_trace(go.Scatter(name="future_pred",x=timer_add, y=prices, mode='lines', line=dict(color="crimson")))
       fig['layout']['xaxis'].update(autorange=True)
       # st.write(fig)

with col3:
   if st.button("Predict (Nxt 20-mins)"):
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Envy2002"
    )

    cur = conn.cursor()
    cur.execute(""" SELECT * from "curren" """)
    rows = cur.fetchall()

    # Convert the results into a Pandas dataframe
    df = pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])
    df = df.reindex(index=df.index[::-1])

    close_price = df[["close"]]
    scaler = MinMaxScaler(feature_range=(0, 1))
    close_price = scaler.fit_transform(close_price)
    new_model = tf.keras.models.load_model('20pred.h5')
    x = np.array([close_price[59::-1]])
    # array = np.array([close_price[0:50]])
    prediction = new_model.predict(x)
    prediction = scaler.inverse_transform(prediction)
    prices = prediction[0]
    df = df.iloc[:150]
    df = df.loc[::-1].reset_index(drop=True)
    close_price = df["close"].to_numpy()
    ts_df = df["time"].to_numpy()

    fig = px.line(df, x="time", y="close", color_discrete_sequence=['#f9a03f'],range_x=[df["time"][0],df["time"][len(df["time"]) - 1]])
    timer_add = []
    tempo = df['close'][len(df["close"]) - 1]
    time_stamp = df["time"][len(df["time"]) - 1]
    for i in range(0,20):
        # Add a timedelta to get the next time stamp
        next_dt = time_stamp + datetime.timedelta(seconds=60)
        timer_add.append(next_dt)
        time_stamp = next_dt
    prices = prices+(tempo-prices[0])
    fig.add_trace(go.Scatter(name="future_pred",x=timer_add,y=prices, mode='lines', line=dict(color="crimson")))
    fig['layout']['xaxis'].update(autorange=True)
st.write(fig)
ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>

<a style='display: inline; text-align: left;' href="https://github.com/itsNisarg/HackInfinity23" target="_blank">&#169; by Deepminds</a></p>

</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)