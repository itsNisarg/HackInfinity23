from datetime import datetime

import requests
import pandas as pd
import time
# import datetime
symbol = "BTCUSDT"
interval = "1m"
limit = 1000 # number of candles to retrieve in each request
end_time = int(time.time() * 1000) - 60000


# Define the end time
# end_time = int(time.mktime(datetime.now().timetuple())) * 1000

from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:Envy2002@localhost/postgres")




def createframe(msg):
  df = pd.DataFrame(msg)
  df = df.loc[:,['t','o','h','l','c']]
  df.columns = ['time','open','high','low','close']
  df.open = df.open.astype(float)
  df.high = df.high.astype(float)
  df.close = df.close.astype(float)
  df.low = df.low.astype(float)
  df.time = pd.to_datetime(df.time,unit='ms')
  return df


if __name__ == "__main__":
        url = f"https://api.binance.com/api/v1/klines?symbol={symbol}&interval={interval}&limit={limit}&endTime={end_time}"
        response = requests.get(url)
        data = response.json()
        tim = []
        ope = []
        hig = []
        lo = []
        clo = []
        for candle in data:
            tim.append(candle[6])
            ope.append(candle[1])
            hig.append(candle[2])
            lo.append(candle[3])
            clo.append(candle[4])
            #filter_cand = {"t" : candle[6],"o" : candle[1], "h" : candle[2], "l" : candle[3], "c" : candle[4]}
            #frame.to_sql('BTCUSDT', engine, if_exists='append', index=False)
            #print(frame)
        filter_cand = {"t" : tim,"o" : ope, "h" : hig, "l" : lo, "c" : clo}
        frame = createframe(filter_cand)
        # framte = frame.reindex(index=frame.index[::-1])
        print(frame)
        frame.to_sql('curren', engine, if_exists='append', index=False)


