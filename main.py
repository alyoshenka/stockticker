import BoardFunctions.Display as Display
import BoardFunctions.Board as Board
import BoardFunctions.Transformer as Transformer

import MessageFunctions.transformations as transformations
import MessageFunctions.groups as groups


def main():
    board = Board.Board(32*8)
    disp = Display.Display(board, 8, 32)

    frame = []
    space = [False]*8
    for c in groups.lowercase:
        frame += transformations.letter_form_to_onoff_form(c)
        frame.append(space)
        frame.append(space)


    arr = transformations.onoff_form_to_array_form(frame)
    color = transformations.tf_array_to_color(arr, color=(54, 208, 255))
    board.data = color

    ctr = 0

    while not disp.shouldExit:
        ctr += 1
        if ctr > 300:
            
            frame = Transformer.scroll(frame, wrap=True)
            arr = transformations.onoff_form_to_array_form(frame)
            color = transformations.tf_array_to_color(arr, color=(54, 208, 255))
            board.data = color

                   
            ctr = 0
        disp.loop()
    

main()
