UP = '↑'
DOWN = '↓'

def ticker_obj_to_string(obj):
    # return f'{obj["symbol"]} ({obj["name"]}) {UP if obj["up?"] else DOWN} ${obj["dollarDelta"]} {obj["percentDelta"]}%'
    arrow = UP if obj["up?"] else DOWN
    dollar = '{0:.2f}'.format(obj["dollarDelta"])
    percent = '{0:.2f}'.format(obj["percentDelta"])
    return f'{obj["symbol"]} {arrow} ${dollar} {percent}%'