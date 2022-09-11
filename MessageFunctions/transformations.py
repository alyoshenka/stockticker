def letter_form_to_onoff_form(arr):
    """
    transform letters made as indexed lines into full-height lines
    using True/False

    [ [1,2], [3,7], ... ]
        ->
    [ [F, T, T, F, F, F, F], [F, F, F, T, F, F, T, T], ... ]
    """
    height = 8
    col_idx = 0
    on_indexes = []
    for col in arr:
        line = [False]*8
        for item in col:
            line[item] = True
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


test_letter_form = [[0], [7]]
test_onoff_form = [[True, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, True]]
test_array_form = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True]
test_color = [(255, 255, 255), None, None, None, None, None, None, None, None, None, None, None, None, None, None, (255, 255, 255)]

assert test_onoff_form == letter_form_to_onoff_form(test_letter_form), "to_onoff_form"
assert test_array_form == onoff_form_to_array_form(test_onoff_form), "to_array_form"
assert test_color == tf_array_to_color(test_array_form), "array_to_color"