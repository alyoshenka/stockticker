import yfinance as yf
import pprint as pp

import json

tickers = json.load(open('./assets/data/tickers.json', 'r'))['tickers']

for tick in tickers:


    data = yf.Ticker(str(tick))
    info = data.info

    #pp.pprint(tsla.info)

    hist = data.history(period='5d')
    #pp.pprint(hist)
    

    close = info['previousClose']
    openP = info['open']
    high = info['dayHigh']
    low = info['dayLow']
    cur = info['currentPrice']

    delta = cur - close

    #print('current:', cur, 'open:', openP, 'high:', high, 'low:', low, 'close:', close)

    print(tick, ':', '${0:0.2f} {1:0.2f}%'.format(delta, delta/close*100))