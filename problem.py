import math
INF = math.inf

map_dij = {
    "Seattle": {("San Francisco", 679), ("Washington D.C.", 1000000)},
    "San Francisco": {("Seattle", 679), ("Los Angeles", 381), ("Denver", 474)},
    "Los Angeles": {("San Francisco", 381), ("Phoenix", 357)},
    "Phoenix": {("Los Angeles", 357), ("Denver", 586)},
    "Denver": {("Phoenix", 586), ("San Francisco", 474), ("Houston", 878), ("Kansas City", 557)},
    "Kansas City": {("Denver", 557), ("Houston", 815), ("Chicago", 412), ("Nashville", 554)},
    "Houston": {("Kansas City", 815), ("Denver", 878)},
    "Chicago": {("Kansas City", 412), ("New York", 712)},
    "Nashville": {("Kansas City", 554), ("Houston", 665), ("Miami", 817)},
    "New York": {("Chicago", 712), ("Washington D.C.", 203)},
    "Washington D.C.": {("Chicago", 701), ("Nashville", 566), ("Miami", 926), ("Seattle", 1000000)},
    "Miami": {("Washington D.C.", 926), ("Houston", 483), ("Nashville", 817)}
}


def find(map, start, end):
    mat = {}
    visited = set()
    unvisited = set(key for key in map.keys())
    for key in unvisited:
        mat[key] = [INF,None]

    current_city = start
    unvisited.remove(start)
    mat[start]=[0,None]

    # while unvisited:
    #     for city in map[current_city]:



    return mat

print(find(map_dij,'Seattle','Miami'))
