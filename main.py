import time
from neopolitan.demos import display as neop
from neopolitan.board_functions.colors import GREEN, RED
from data.collection import get_tickers, get_ticker_data
from data.transformation import ticker_obj_to_string

all_ticker_data = [get_ticker_data(sym) for sym in get_tickers()]
msg = []
for tick in all_ticker_data:
    msg.append(('  ' + ticker_obj_to_string(tick), GREEN if tick['up?'] else RED))

neop(msg)
