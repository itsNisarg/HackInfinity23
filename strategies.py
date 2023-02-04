# from exchange.binance import Binanceclient
# import pandas as pd
# from IPython.display import display
# import numpy as np
# import plotly.express as px
# class strategies:
#     def __init__(self,candles):
#         self.candles = candles
#
#     def RSI(self,rsi_period):
#         #rsi_period = 14
#         df = pd.DataFrame(self.candles)[['time', 'open', 'high', 'low', 'close']]
#
#         # to calculate RSI, we first need to calculate the exponential weighted aveage gain and loss during the period
#         df['gain'] = (df['close'] - df['open']).apply(lambda x: x if x > 0 else 0)
#         df['loss'] = (df['close'] - df['open']).apply(lambda x: -x if x < 0 else 0)
#
#         # here we use the same formula to calculate Exponential Moving Average
#         df['ema_gain'] = df['gain'].ewm(span=rsi_period, min_periods=rsi_period).mean()
#         df['ema_loss'] = df['loss'].ewm(span=rsi_period, min_periods=rsi_period).mean()
#
#         # the Relative Strength is the ratio between the exponential avg gain divided by the exponential avg loss
#         df['rs'] = df['ema_gain'] / df['ema_loss']
#
#         # the RSI is calculated based on the Relative Strength using the following formula
#         df['rsi_14'] = 100 - (100 / (df['rs'] + 1))
#
#         # displaying the results
#         display(df[['time', 'rsi_14', 'rs', 'ema_gain', 'ema_loss']])
#
# #         # plotting the RSI
# #         fig_rsi = px.line(df, x='time', y='rsi_14', title='RSI Indicator')
# #
# #         # RSI commonly uses oversold and overbought levels, usually at 70 and 30
# #         overbought_level = 70
# #         orversold_level = 30
# #
# # # adding oversold and overbought levels to the plot
# # fig_rsi.add_hline(y=overbought_level, opacity=0.5)
# # fig_rsi.add_hline(y=orversold_level, opacity=0.5)
# #
# # # showing the RSI Figure
# # display(fig_rsi)


import psycopg2
import pandas as pd

# Connect to the database

if __name__=="__main__":
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Envy2002"
    )

    # Query the database and retrieve the results
    cur = conn.cursor()
    cur.execute(""" SELECT * from "RVNUSDT" """)
    rows = cur.fetchall()

    # Convert the results into a Pandas dataframe
    df = pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])
    print(df)



