import MessageFunctions.groups as groups
import MessageFunctions.letters as letters


import pprint as pp

def ten_zeroes():
    frame = []
    space = []
    for i in range(10):
        for line in letters.ZERO:
            frame.append(line)
        frame.append(space)
    return frame

def lowercase_with_space():
    frame = []
    space = []
    for char in groups.lowercase:
        for line in char:
            frame.append(line)
        frame.append(space)

    return frame

def cons_frame():
    frame = []
    space = []
    for char in groups.lowercase:
        for line in char:
            filled = [None]*8
            for idx in line:
                filled[idx] = (0, 0, 100)
            frame.append(filled)
        frame.append(space)

    return frame

def to_indices(frame):
    pairs = []
    for col in range(len(frame)):
        for row in range(len(frame[col])):
            if frame[col][row]:
                pairs.append([col, row])
                
    return pairs

def to_data_array(indices, width, height):
    data = [None]*width*height
    for pair in indices:
        idx = pair[1]*height+pair[0]
        data[idx] = (255, 255, 255)
    return data



def new_output():
    for i in range(len(groups.lowercase)):
        character = groups.lowercase[i]
        c = []
        for line in character:
            l = []
            for index in line:
                l.append(index % 8)
            c.append(l)
        print(chr(97+i), "=", c)
    print()
    for i in range(len(groups.uppercase)):
        character = groups.uppercase[i]
        c = []
        for line in character:
            l = []
            for index in line:
                l.append(index % 8)
            c.append(l)
        print(chr(65+i), "=", c)
    print()
    for i in range(len(groups.numbers)):
        character = groups.numbers[i]
        c = []
        for line in character:
            l = []
            for index in line:
                l.append(index % 8)
            c.append(l)
        print(chr(48+i), "=", c)
    print()
    for key in groups.symbols:
        character = groups.symbols[key]
        c = []
        for line in character:
            l = []
            for index in line:
                l.append(index % 8)
            c.append(l)
        print(key, "=", c)