import MessageFunctions.groups as groups

def letter_form_to_onoff_form(arr, on=True, off=False):
    """
    transform letters made as indexed lines into full-height lines
    using on/off (set to True/False by default; change to set colors)

    [ [1,2], [3,7], ... ]
        ->
    [ [F, T, T, F, F, F, F], [F, F, F, T, F, F, T, T], ... ]
    """
    height = 8
    col_idx = 0
    on_indexes = []
    for col in arr:
        line = [off]*8
        for item in col:
            line[item] = on
        on_indexes.append(line)
    return on_indexes

def onoff_form_to_array_form(arr):
    """
    transform letters in full lines into one contiguous array

    [ [line], [line], ... ] -> [ True, False, True, ... ]
    """
    result = []
    for line in arr:
        result += line
    return result

def tf_array_to_color(arr, color=(255,255,255)):
    assert arr is not None

    return list(map(lambda on: color if on else None, arr))

def string_to_letter_form(string, color):

    space = [False]*8

    def get_formatted(char):
        ascii = ord(char)
        if ascii >= 97 and ascii < 123:
            return groups.lowercase[ascii-97]
        elif ascii >= 65 and ascii < 91:
            return groups.uppercase[ascii-65]
        elif ascii >= 48 and ascii < 58:
            return groups.numbers[ascii-48]
        elif char in groups.symbols:
            return groups.symbols[char]
        else:
            print("Cannot find char: " + char)
            return []

    data = []
    for char in string:
        formatted = get_formatted(char)
        data += letter_form_to_onoff_form(formatted, on=color)
        data.append(space)
    return data       



