import yfinance as yf
import pprint as pp

import json

def tickers():
    """Get all tickers listed in ./assets/data/tickers.json"""
    try:
        return json.load(open('./assets/data/tickers.json', 'r'))['tickers']
    except Exception as e:
        print("ERROR:", e)

def get_ticker_data(sym):
    """"Query and return formatted data from a ticker symbol"""
    try:
        data = yf.Ticker(str(sym))
    except Exception as e:
        print("ERROR", e)
        return None

    info = data.info
    #hist = data.history(period='5d')
    
    close = info['previousClose']
    #openP = info['open']
    #high = info['dayHigh']
    #low = info['dayLow']
    cur = info['currentPrice']
    name = info['shortName']
    symbol = info['symbol']

    delta = cur - close

    obj = {
        "symbol": symbol,
        "name": name,
        "dollarDelta": round(delta, 2),
        "percentDelta": round(delta/close*100, 2),
        "up?": delta > 0
    }
    return obj

def print_all_tickers():
    """Print data from all stock tickers in tickers.json"""
    for tick in tickers():
        obj = get_ticker_data(tick)

        print(obj['symbol'], ('(' + obj['name'] + ')'), ':', '${0:0.2f} {1:0.2f}%'.format(obj['dollarDelta'], obj['percentDelta']))