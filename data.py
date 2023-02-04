import requests
import pandas as pd
symbol = "BTCUSDT"
interval = "1m"
limit = 1000 # number of candles to retrieve in each request
total_candles = 5000 # total number of candles to retrieve
start_time = 0

from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:Envy2002@localhost/postgres")

url = f"https://api.binance.com/api/v1/klines?symbol={symbol}&interval={interval}&limit={limit}"



def createframe(msg):
  df = pd.DataFrame([msg])
  df = df.loc[:,['t','o','h','l','c']]
  df.columns = ['time','open','high','low','close']
  df.open = df.open.astype(float)
  df.high = df.high.astype(float)
  df.close = df.close.astype(float)
  df.low = df.low.astype(float)
  df.time = pd.to_datetime(df.time,unit='ms')
  return df


if __name__ == "__main__":
    while total_candles > 0:
        url = f"https://api.binance.com/api/v1/klines?symbol={symbol}&interval={interval}&limit={limit}&startTime={start_time}"
        response = requests.get(url)
        data = response.json()
        for candle in data:
            filter_cand = {"t" : candle[6],"o" : candle[1], "h" : candle[2], "l" : candle[3], "c" : candle[4]}
            frame = createframe(filter_cand)
            print(frame)
            frame.to_sql('BTCUSDT', engine, if_exists='append', index=False)
            print(frame)
        total_candles -= limit
        start_time = data[-1][0]