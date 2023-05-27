import yfinance as yf
import json
from data.transformation import ticker_obj_to_string

def get_tickers():
    """Get all tickers listed in ./assets/data/tickers.json"""
    try:
        return json.load(open('../assets/data/tickers.json', 'r'))['tickers']
    except Exception as err:
        print("ERROR:", err)
        return None

def get_ticker_data(sym):
    """"Query and return formatted data from a ticker symbol"""
    try:
        data = yf.Ticker(str(sym))
    except Exception as err:
        print("ERROR", err)
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
    for sym in get_tickers():
        data = get_ticker_data(sym)
        disp = ticker_obj_to_string(data)
        print(disp)

