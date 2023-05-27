import time
from neopolitan.demos import display as neop
from data.collection import get_tickers, get_ticker_data
from data.transformation import ticker_obj_to_string

all_ticker_data = [ticker_obj_to_string(get_ticker_data(sym)) for sym in get_tickers()]
display_str = '    '.join(all_ticker_data)

neop(display_str)