def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for map_ in items:
            if map_[args[0]] != None:
                print(map_[args[0]])
    elif len(args) > 1:
        for map_ in items:
            new_map = dict()
            for key in args:
                if key in map_:
                    new_map[key] = map_[key]
            if new_map != None:
                print(new_map)



if __name__ == "__main__":
    goods = [
       {'title': 'Ковер', 'price': 2000, 'color': 'green'},
       {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    field(goods, 'title', 'price')