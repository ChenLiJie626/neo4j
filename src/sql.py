# coding:utf-8
import json

from neo4j import GraphDatabase
import pandas as pd

from src.util_json import transform

driver = GraphDatabase.driver("bolt://admin.idevlab.cn:7687", auth=("neo4j", "neo5j"))


def print_Movie(tx, name):
    # 根据电影返回电影信息
    result = set()
    for record in tx.run("Match  (a:Movie)  where  a.name =~$name" " return a", {"name": ".*" + name + ".*"}):
        result.add(record["a"])
    return result


def print_Person(tx, name):
    # 根据演员名称返回演员信息
    result = set()
    for record in tx.run("Match  (a:Person)  where  a.name=~$name  " " return a", {"name": ".*" + name + ".*"}):
        result.add(record["a"])
    return result


def role_Movie(tx, name):
    # 根据演员返回电影信息
    result = set()
    for record in tx.run(
            "Match  (a:Person)-[role]->(b:Movie) where  a.name =~$name"
            " return b  ORDER BY b.name", {"name": ".*" + name + ".*"}):
        result.add(record["b"])
    return result


def tag_Movie(tx, tag):
    # 根据标签返回电影信息
    result = set()
    for record in tx.run("Match  (a:Movie)-[have]->(b:t)"
                         "where  b.tag=~$tag"
                         " return  a", {"tag": ".*" + tag + ".*"}):
        result.add(record["a"])
    return result


def direct_Movie(tx, d_name):
    # 找导演相关电影
    result = set()
    for record in tx.run("Match  (a:Person)-[director]->(b:Movie) where  a.name=~$d_name"
                         " return b  ORDER BY b.name", {"d_name": ".*" + d_name + ".*"}):
        result.add(record["b"])
    return result


def genres_Movie_L(tx, genres):
    # 找寻类型相关电影
    result = set()
    for record in tx.run("Match  (a:genres)-[genre_r]->(b:Movie)"
                         "where  a.id=~$genres"
                         " return  b  ORDER BY b.rate limit 20", {"genres": ".*" + genres + ".*"}):
        result.add(record["b"])
    return result


def direct_Person(tx, d_name):
    # 找导演相关电影
    result = set()
    for record in tx.run("Match  (a:Person)-[director]->(b:Movie) where  a.name=~$d_name"
                         " with a,b,director match (c:Person)-[role]->(b:Movie) "
                         "return c ORDER BY b.name", {"d_name": ".*" + d_name + ".*"}):
        result.add(record["c"])
    return result


def genres_Movie_H(tx, genres):
    # 找寻类型相关电影
    result = set()
    for record in tx.run("Match  (a:genres)-[genre_r]->(b:Movie)"
                         "where  a.id=~$genres"
                         " return  b  ORDER BY b.rate DESC limit 20", {"genres": ".*" + genres + ".*"}):
        print(record["b"])
        result.add(record["b"])
    return result


def network_Person(tx, name):
    for record in tx.run("match path=(P1:Person)-[:role]-()-[]-() where P1.name=~'.*邓超.*'  return path, apoc.path.elements(path) limit 30"):
        res = record['apoc.path.elements(path)']
        return res




if __name__ == '__main__':

    with driver.session() as session:
        result = session.run("match p=(P1:Person)-[:role]-()-[]-() where P1.name=~'.*邓超.*' with collect(p) as ps call apoc.convert.toTree(ps)  yield value RETURN value").data()


    data = result[0]['value']
    transform(data)
    # res_json = []
    # for item in res:
    #     json_temp = {
    #         'name': item['name'],
    #         'sex': item['sex'],
    #         'birthday': item['birthday'],
    #         'img': item['img'],
    #         'summary': item['summary'],
    #         'birthplace': item['birthplace']
    #     }
    #     res_json.append(json_temp)
    # res_json = json.dumps(res_json, ensure_ascii=False)
    # print(res_json)
