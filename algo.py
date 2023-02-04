import pandas as pd
import cufflinks as cf
import numpy as np
import plotly.offline as plyo
from sqlalchemy import create_engine
from keras.models import Sequential
from keras.layers import SimpleRNN,Dense
import tensorflow as tf
# engine = create_engine("postgresql://postgres:Envy2002@localhost/postgres")
# myQuery = '''SELECT * FROM public."RVNUSDT"'''
# df = pd.read_sql_query(myQuery, engine)
# df.set_index('time',inplace=True)
# print(df)

# def RSI(temp):
#     data = temp
#     SMA1 = 3
#     SMA2 = 5
#     data['SMA1'] = data["close"].rolling(SMA1).mean()
#     data['SMA2'] = data["close"].rolling(SMA2).mean()
#     data.dropna(inplace=True)
#     data['Position'] = np.where(data['SMA1'] > data['SMA2'], 1, -1)
#     data.tail()
def RNN(df,lookback):
    test_size = 10
    tot = len(df)

    df = df[["time","close"]]
    trainer = df[:(tot-test_size),:]
    tester  = df[(tot-test_size):,:]
    rnn_data_x = []
    rnn_data_y = []
    for i in range(len(trainer)-lookback-1):
        rnn_data_x.append(trainer[i:i+lookback,1])
        rnn_data_y.append(trainer[i+lookback,1])
    rnn_data_y = np.array(rnn_data_y)
    rnn_data_x = np.array(rnn_data_x)
    tf.random.set_seed(4)
    model = Sequential()
    model.add(SimpleRNN(32,input_shape=(1,lookback)))
    model.add(Dense(1))
    model.compile(loss="mean_squared_error",
                  optimizer="adam",
                  metrics=["mse"])
    model.fit(rnn_data_x,rnn_data_y)



    


if __name__=="__main__":
    engine = create_engine("postgresql://postgres:Envy2002@localhost/postgres")
    myQuery = '''SELECT * FROM public."RVNUSDT"'''
    df = pd.read_sql_query(myQuery, engine)





