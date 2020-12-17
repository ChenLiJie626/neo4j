


def get_summary(data):
    summary = None
    try:
        summary = data['summary']
    except Exception as err:
        pass
    return summary


def get_img(data):
    img = None
    try:
        img = data['img']
    except Exception as err:
        pass
    return img


def get_name_tag(data):
    name = None
    try:
        name = data['name']
    except Exception as err:
        name = data['tag']
        pass
    return name


c = 0

categorie_all = ["genre_r", 'author', "director", "role", "have", "movie"]


def get_id(data):
    id = None
    try:
        id = data['id']
    except Exception as err:
        pass
    return id

def dfs(data, categorie):
    global c


    node = {
        "label": get_name_tag(data),
        "value": 10,
        "image": get_img(data),
        "id": data['_id'],
        "db_id":get_id(data),
        "categories": [
            data['_type']
        ],
        "info": get_summary(data)
    }

    nodes_path.append(node)


    for item in categorie_all:
        try:
            for data1 in data[item]:
                dfs(data1, categorie)
                c = c + 1
                edge = {
                    "id": c,
                    "label": item,
                    "from": data['_id'],
                    "to": data1['_id']
                }
                edges_path.append(edge)
            break
        except Exception as err:
            # print(err ,666)
            pass


def find_path(data):
    global nodes_path
    global edges_path
    nodes_path = []
    edges_path = []

    dfs(data, None)
    result = {
        "categories": {
            "Person": "人",
            "role": "演员",
            "t": "标签",
            "genres": "类型",
        },
        "data": {
            "nodes": nodes_path,
            "edges": edges_path
        }
    }
    print(result)
    return result
