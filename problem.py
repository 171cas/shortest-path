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
    matrix = {}
    unvDic = {}
    unvisited = set(key for key in map.keys())

    for key in unvisited:
        matrix[key] = [INF, None]
        unvDic[key] = INF

    # current_city = start
    # unvisited.remove(start)
    matrix[start] = [0, None]
    unvDic[start] = 0
    # test = {'a':1,'b':123, 'asdf':45, 'asdfff':-50}

    # unvisited.remove(current_city)
    # current_city = min(test, key=test.get)
    i = 0
    while unvisited:  # i < 3:
        current_city = min(unvDic, key=unvDic.get)
        current_distance = unvDic[current_city]
        # print('current_city', current_city)
        # print('unvDic', unvDic)
        # print('matrix', matrix)
        # print('current_distance', current_distance)
        # print('--------------------------------------------------------')
        # neighbors = [city[0] for city in list(map[current_city])]
        # print('current_city',current_city)
        # print('map[current_city]',map[current_city])
        # print('list(map[current_city])',list(map[current_city]))

        for city in list(map[current_city]):
            # print('city',city)
            # print('matrix[city[0]]',matrix[city[0]])
            # print('2--------------------------------------------------------')
            if city[1]+current_distance < matrix[city[0]][0] and city[0] in unvisited:
                matrix[city[0]][0] = city[1]+current_distance
                matrix[city[0]][1] = current_city
                unvDic[city[0]] = city[1]+current_distance

        # print('matrix',matrix)
        unvisited.remove(current_city)
        del unvDic[current_city]
        # i = i+1

    return matrix


print(find(map_dij, 'Seattle', 'Miami'))

# print(min(d, key=d.get))
# for city in map[current_city]:
#             print(city[0])
#         current_city = unvisited.pop()

# for pair in map[current_city]:
#      neighbors[pair[0]] = pair[1]

# print(unvDic)
# print(unvisited)
# print(matrix)

# visited = set()
# neighbors = {}
