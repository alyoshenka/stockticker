import BoardFunctions.Display as Display
import BoardFunctions.Board as Board

import MessageFunctions.main as Messages
import BoardFunctions.Transformer as Transformer

import MessageFunctions.transformations as transformations
import MessageFunctions.letters as letters


def main():
    board = Board.Board(32*8)
    disp = Display.Display(board, 8, 32)

    frame = []
    space = [False]*8
    char = letters.ZERO
    line1 = [[0,1,2,3,4,5,6,7]]
    for i in range(8):
        frame += transformations.letter_form_to_onoff_form(char)
        frame.append(space)
        frame.append(space)
        frame.append(space)


    arr = transformations.onoff_form_to_array_form(frame)
    color = transformations.tf_array_to_color(arr)
    board.data = color

    ctr = 0

    while not disp.shouldExit:
        ctr += 1
        if ctr > 300:
            
            frame = Transformer.scroll(frame, wrap=True)
            arr = transformations.onoff_form_to_array_form(frame)
            color = transformations.tf_array_to_color(arr)
            board.data = color

                
            
            ctr = 0
        disp.loop()
    

main()
