import sqlite3

from flask import Flask
from flask import jsonify
from neo4j import GraphDatabase
from src.sql import print_Movie, genres_Movie_H, genres_Movie_L, direct_Movie, direct_Person
from src.sql import print_Person
from src.sql import role_Movie
from src.sql import tag_Movie
from src.predict import recommend_same_type_movie

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
driver = GraphDatabase.driver("bolt://admin.idevlab.cn:7687", auth=("neo4j", "neo5j"))


@app.route('/')
def hello_world():
    return 'This is the movie backstage system'


@app.route('/print_Movie/<name>')
def Print_Movie(name):
    with driver.session() as session:
        res = session.read_transaction(print_Movie, name)
    res_json = []
    for item in res:
        json_temp = {
            'name': item['name'],
            'year': item['year'],
            'rate': item['rate'],
            'genre': item['genre'],
            'summary': item['summary']
        }
        res_json.append(json_temp)
    return jsonify(res_json)


@app.route('/print_Person/<name>')
def Print_Person(name):
    with driver.session() as session:
        res = session.read_transaction(print_Person, name)
    res_json = []
    for item in res:
        json_temp = {
            'name': item['name'],
            'sex': item['sex'],
            'birthday': item['birthday'],
            'img': item['img'],
            'summary': item['summary'],
            'birthplace': item['birthplace']
        }
        res_json.append(json_temp)
    return jsonify(res_json)


@app.route('/role_Movie/<name>')
def Role_Movie(name):
    with driver.session() as session:
        res = session.read_transaction(role_Movie, name)
    res_json = []
    for item in res:
        json_temp = {
            'name': item['name'],
            'year': item['year'],
            'rate': item['rate'],
            'genre': item['genre'],
            'summary': item['summary']
        }
        res_json.append(json_temp)
    return jsonify(res_json)


@app.route('/tag_Movie/<name>')
def Tag_Movie(name):
    with driver.session() as session:
        res = session.read_transaction(tag_Movie, name)
    res_json = []
    for item in res:
        json_temp = {
            'name': item['name'],
            'year': item['year'],
            'rate': item['rate'],
            'genre': item['genre'],
            'summary': item['summary']
        }
        res_json.append(json_temp)
    return jsonify(res_json)


@app.route('/genres_Movie_High/<name>')
def Genres_Movie_H(name):
    with driver.session() as session:
        res = session.read_transaction(genres_Movie_H, name)
    res_json = []
    for item in res:
        json_temp = {
            'name': item['name'],
            'year': item['year'],
            'rate': item['rate'],
            'genre': item['genre'],
            'summary': item['summary']
        }
        res_json.append(json_temp)
    return jsonify(res_json)


@app.route('/genres_Movie_Low/<name>')
def Genres_Movie_L(name):
    with driver.session() as session:
        res = session.read_transaction(genres_Movie_L, name)
    res_json = []
    for item in res:
        json_temp = {
            'name': item['name'],
            'year': item['year'],
            'rate': item['rate'],
            'genre': item['genre'],
            'summary': item['summary']
        }
        res_json.append(json_temp)
    return jsonify(res_json)


@app.route('/direct_Movie/<name>')
def Direct_Movie(name):
    with driver.session() as session:
        res = session.read_transaction(direct_Movie, name)
    res_json = []
    for item in res:
        json_temp = {
            'name': item['name'],
            'year': item['year'],
            'rate': item['rate'],
            'genre': item['genre'],
            'summary': item['summary']
        }
        res_json.append(json_temp)
    return jsonify(res_json)


@app.route('/direct_Person/<name>')
def Direct_Person(name):
    with driver.session() as session:
        res = session.read_transaction(direct_Person, name)
    res_json = []
    for item in res:
        json_temp = {
            'name': item['name'],
            'sex': item['sex'],
            'birthday': item['birthday'],
            'img': item['img'],
            'summary': item['summary'],
            'birthplace': item['birthplace']
        }
        res_json.append(json_temp)
    return jsonify(res_json)


@app.route('/recommend_Movie/<movieID>')
def Recommend_Movie(movieID):
    try:
        conn = sqlite3.connect('movID.db')
        c = conn.cursor()
        sql = "select id from MovID where name = ?"
        movieID = [movieID]
        cursor = c.execute(sql,movieID)
        for row in cursor:
            movieID = row[0]

        res = recommend_same_type_movie(int(movieID))

        res_json = []
        for item in res:
            with driver.session() as session:
                item = session.read_transaction(print_Movie, item)
            for i in iter(item):
                item = i
                break
            json_temp = {
                'name': item['name'],
                'year': item['year'],
                'rate': item['rate'],
                'genre': item['genre'],
                'summary': item['summary']
            }
            res_json.append(json_temp)
        return jsonify(res_json)
    except Exception as e:
        print(str(e))
        return 'not find'


# @app.route('/movie_Country/<country>')
# def Movie_Country(country):
#     try:
#         conn = sqlite3.connect('movie.db')
#         c = conn.cursor()
#         sql = "select name from movie where country like ? LIMIT 20"
#         country = ["%"+country+"%"]
#         cursor = c.execute(sql, country)
#         res = []
#         for row in cursor:
#             res.append(row[0])
#
#         print(res)
#         res_json = []
#         for item in res:
#             with driver.session() as session:
#                 item = session.read_transaction(print_Movie, item)
#             for i in iter(item):
#                 item = i
#                 break
#             json_temp = {
#                 'name': item['name'],
#                 'year': item['year'],
#                 'rate': item['rate'],
#                 'genre': item['genre'],
#                 'summary': item['summary']
#             }
#             res_json.append(json_temp)
#         return jsonify(res_json)
#     except Exception as e:
#         print(str(e))
#         return 'not find'


@app.route('/movie_Network/<name>')
def Movie_Country(name):
    conn = sqlite3.connect('movie.db')
    c = conn.cursor()
    sql = "select id from movie where name = ? "
    name = [name]
    cursor = c.execute(sql, name)
    res = None
    for row in cursor:
        res = row[0]
        break
    if res is None:
        return 'not find'

    actor = []
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
