import BoardFunctions.Display as Display
import BoardFunctions.Board as Board
import BoardFunctions.Transformer as Transformer

import MessageFunctions.transformations as transformations
import MessageFunctions.groups as groups

import DataFunctions.collection as collection


def main():
    board = Board.Board(32*8)
    disp = Display.Display(board, 8, 32, size=25)

    frame = []
    space = [False]*8
    """
    for c in groups.lowercase:
        frame += transformations.letter_form_to_onoff_form(c)
        frame.append(space)
        frame.append(space)
    """
    
    tickers = collection.tickers()
    # initialize the first 3 tickers
    for i in range(len(tickers)):
        ticker = collection.get_ticker_data(tickers[i])
        # translate to frame
        frame += ticker_data_to_letter_form(ticker)
        for i in range(4):
            frame.append(space)


    arr = transformations.onoff_form_to_array_form(frame)
    #color = transformations.tf_array_to_color(arr, color=(54, 208, 255))
    board.data = arr

    ctr = 0

    while not disp.shouldExit:
        ctr += 1
        if ctr > 200:
            
            frame = Transformer.scroll(frame, wrap=True)
            arr = transformations.onoff_form_to_array_form(frame)
            #color = transformations.tf_array_to_color(arr, color=(54, 208, 255))
            board.data = arr

                   
            ctr = 0
        disp.loop()

def ticker_data_to_letter_form(tick):
    space = [False]*8
    data = []

    color =  (0,255,0) if tick["up?"] else (255,0,0)

    data += transformations.string_to_letter_form(tick["symbol"], (54, 208, 255))
    data.append(space)
    data.append(space)
    data += transformations.string_to_letter_form("$" + str(tick["dollarDelta"]),color)
    data.append(space)
    data.append(space)
    data += transformations.string_to_letter_form(str(tick["percentDelta"]) + "%", color)

    return data
    

main()
