c = 0
cate_all = ["genre_r", 'author', "director", "role", "have", "movie"]


def get_summary(data):
    if 'summary' in data:
        return data['summary']
    return None


def get_img(data):
    if 'img' in data:
        return data['img']
    return None


def get_name(data):
    if '_type' not in data:
        return None

    data_type = data['_type']
    try:
        if data_type == 'Movie' or data_type == 'Person':
            name = data['name']
        elif data_type == 't':
            name = data['tag']
        else:
            name = data['id']

    except Exception as err:
        name = data['id']
        pass
    return name


def get_id(data):
    if 'id' in data:
        return data['id']
    return None


def dfs(data):
    global c

    node = {
        "label": get_name(data),
        "value": 10,
        "image": get_img(data),
        "id": data['_id'],
        "db_id": get_id(data),
        "categories": [
            data['_type']
        ],
        "info": get_summary(data)
    }
    nodes_path.append(node)

    for item in cate_all:
        if item in data:
            for subnode in data[item]:
                c += 1
                edge = {
                    "id": c,
                    "label": item,
                    "from": data['_id'],
                    "to": subnode['_id']
                }
                edges_path.append(edge)
                dfs(subnode)


def find_path(data):
    global nodes_path
    global edges_path
    nodes_path = []
    edges_path = []

    dfs(data)

    result = {
        "data": {
            "nodes": nodes_path,
            "edges": edges_path
        }
    }
    return result
