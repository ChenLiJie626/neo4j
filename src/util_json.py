

def transform(data):
    nodes = []
    edges = []
    print(data)

    Id = 1
    node = {
        "label": data['name'],
        "value": 10,
        "image": data['img'],
        "id": data['_id'],
        "categories": [
            'role'
        ],
        "info": get_summary(data)
    }
    nodes.append(node)




    movies = data['role']
    for movie in movies:
        edge = {
            "id": Id,
            "label": "位于",
            "from": data['_id'],
            "to": movie['_id']
        }
        Id = Id + 1
        edges.append(edge)
        node = {
            "label": movie['name'],
            "value": 10,
            "image": None,
            "id": movie['_id'],
            "categories": [
                'movie'
            ],
            "info": movie['summary']
        }
        nodes.append(node)

        try:
            authors = movie['author']
            for author in authors:
                edge = {
                    "id": Id,
                    "label": "编写",
                    "from": author['_id'],
                    "to": movie['_id']
                }
                Id = Id + 1
                edges.append(edge)
                node = {
                    "label": author['name'],
                    "value": 10,
                    "image": author['img'],
                    "id": author['_id'],
                    "categories": [
                        'author'
                    ],
                    "info": get_summary(author)
                }
                nodes.append(node)
        except Exception as err:
            pass

        try:
            directors = movie['director']
            for director in directors:
                edge = {
                    "id": Id,
                    "label": "导演",
                    "from": director['_id'],
                    "to": movie['_id']
                }
                Id = Id + 1
                edges.append(edge)
                node = {
                    "label": director['name'],
                    "value": 10,
                    "image": director['img'],
                    "id": director['_id'],
                    "categories": [
                        'director'
                    ],
                    "info": get_summary(director)
                }
                nodes.append(node)
        except Exception as err:
            pass

        try:
            genre_rs = movie['genre_r']
            for genre_r in genre_rs:
                edge = {
                    "id": Id,
                    "label": "类型",
                    "from": genre_r['_id'],
                    "to": movie['_id']
                }
                Id = Id + 1
                edges.append(edge)
                node = {
                    "label": genre_r['id'],
                    "value": 10,
                    "image": None,
                    "id": genre_r['_id'],
                    "categories": [
                        'genre_r'
                    ],
                    "info": None
                }
                nodes.append(node)
        except Exception as err:
            pass

        try:
            haves = movie['have']
            for have in haves:
                edge = {
                    "id": Id,
                    "label": "标签",
                    "from": have['_id'],
                    "to": movie['_id']
                }
                Id = Id + 1
                edges.append(edge)
                node = {
                    "label": have['tag'],
                    "value": 10,
                    "image": None,
                    "id": have['_id'],
                    "categories": [
                        'have'
                    ],
                    "info": None
                }
                nodes.append(node)
        except Exception as err:
            pass

        try:
            roles = movie['role']
            for role in roles:
                edge = {
                    "id": Id,
                    "label": "出演",
                    "from": role['_id'],
                    "to": movie['_id']
                }
                Id = Id + 1
                edges.append(edge)

                node = {
                    "label": role['name'],
                    "value": 10,
                    "image": role['img'],
                    "id": role['_id'],
                    "categories": [
                        'role'
                    ],
                    "info": get_summary(role)
                }
                print(role['_id'])
                nodes.append(node)
        except Exception as err:
            pass

    result = {
        "categories": {
            "genre_r": "喜剧",
            "author": "编剧",
            "director": "导演",
            "role": "演员",
            "have": "标签",
            "movie": "电影",
        },
        "data": {
            "nodes": nodes,
            "edges": edges
        }
    }

    return result


def get_summary(data):
    summary = None
    try:
        summary = data['summary']
    except Exception as err:
        pass
    return summary


c = 0



def dfs(data, cnt):
    global c
    img = None
    try:
        img = data['img']
        categorie = 'role'
    except Exception as err:
        categorie = 'movie'
        pass

    node = {
        "label": data['name'],
        "value": 10,
        "image": img,
        "id": data['_id'],
        "categories": [
            categorie
        ],
        "info": get_summary(data)
    }

    nodes_path.append(node)
    try:
        for data1 in data['role']:
            dfs(data1, cnt + 1)
            c = c + 1
            edge = {
                "id": c,
                "label": "出演",
                "from": data['_id'],
                "to": data1['_id']
            }

            edges_path.append(edge)

    except Exception as err:
        print(err,666)
        pass


def find_path(data):
    global nodes_path
    global edges_path
    nodes_path = []
    edges_path = []
    dfs(data, 0)
    result = {
        "categories": {
            "role": "演员",
            "movie": "电影",
        },
        "data": {
            "nodes": nodes_path,
            "edges": edges_path
        }
    }
    print(result)
    return result