
def transform(data):
    nodes = []
    edges = []

    Id = 1
    node = {
        "label": data['name'],
        "value": 10,
        "image": get_img(data),
        "id": data['_id'],
        "categories": [
            data['_type']
        ],
        "info": get_summary(data)
    }
    nodes.append(node)

    try:
        authors = data['author']
        for author in authors:
            edge = {
                "id": Id,
                "label": "编写",
                "from": author['_id'],
                "to": data['_id']
            }
            Id = Id + 1
            edges.append(edge)
            node = {
                "label": author['name'],
                "value": 10,
                "image": author['img'],
                "id": author['_id'],
                "categories": [
                    author['_type']
                ],
                "info": get_summary(author)
            }
            nodes.append(node)
    except Exception as err:
        pass

    try:
        directors = data['director']
        for director in directors:
            edge = {
                "id": Id,
                "label": "导演",
                "from": director['_id'],
                "to": data['_id']
            }
            Id = Id + 1
            edges.append(edge)
            node = {
                "label": director['name'],
                "value": 10,
                "image": director['img'],
                "id": director['_id'],
                "categories": [
                    director['_type']
                ],
                "info": get_summary(director)
            }
            nodes.append(node)
    except Exception as err:
        pass

    try:
        genre_rs = data['genre_r']
        for genre_r in genre_rs:
            edge = {
                "id": Id,
                "label": "类型",
                "from": genre_r['_id'],
                "to": data['_id']
            }
            Id = Id + 1
            edges.append(edge)
            node = {
                "label": genre_r['id'],
                "value": 10,
                "image": None,
                "id": genre_r['_id'],
                "categories": [
                    genre_r['_type']
                ],
                "info": None
            }
            nodes.append(node)
    except Exception as err:
        pass

    try:
        haves = data['have']
        for have in haves:
            edge = {
                "id": Id,
                "label": "标签",
                "from": have['_id'],
                "to": data['_id']
            }
            Id = Id + 1
            edges.append(edge)
            node = {
                "label": have['tag'],
                "value": 10,
                "image": None,
                "id": have['_id'],
                "categories": [
                    have['_type']
                ],
                "info": None
            }
            nodes.append(node)
    except Exception as err:
        pass

    try:
        roles = data['role']
        for role in roles:
            edge = {
                "id": Id,
                "label": "出演",
                "from": role['_id'],
                "to": data['_id']
            }
            Id = Id + 1
            edges.append(edge)

            node = {
                "label": role['name'],
                "value": 10,
                "image": role['img'],
                "id": role['_id'],
                "categories": [
                    role['_type']
                ],
                "info": get_summary(role)
            }
            nodes.append(node)
    except Exception as err:
        pass

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
            "image": get_img(movie),
            "id": movie['_id'],
            "categories": [
                movie['_type']
            ],
            "info": get_summary(movie)
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
                        author['_type']
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
                        director['_type']
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
                        genre_r['_type']
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
                        have['_type']
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
                        role['_type']
                    ],
                    "info": get_summary(role)
                }
                nodes.append(node)
        except Exception as err:
            pass

    result = {
        "categories": {
            "Person": "人",
            "role": "演员",
            "t": "标签",
            "genres": "类型",
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

def dfs(data, categorie):
    global c


    node = {
        "label": get_name_tag(data),
        "value": 10,
        "image": get_img(data),
        "id": data['_id'],
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
