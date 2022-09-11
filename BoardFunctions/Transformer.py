def scroll(data, dist=1, wrap=False):
    if wrap:
        data.append(data[0])
    return data[1:None]