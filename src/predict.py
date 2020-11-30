import pickle

import tensorflow as tf

import numpy as np
title_count, title_set, genres2int, features, targets_values, ratings, users, movies, data, movies_orig, users_orig \
    = pickle.load(open('preprocess.p', mode='rb'))
movie_matrics = pickle.load(open('movie_matrics.p', mode='rb'))
movieid2idx = {val[0]:i for i, val in enumerate(movies.values)}
def recommend_same_type_movie(movie_id_val, top_k=20):
    norm_movie_matrics = tf.sqrt(tf.reduce_sum(tf.square(movie_matrics), 1, keepdims=True))
    normalized_movie_matrics = movie_matrics / norm_movie_matrics
    print(movie_id_val)
    # 推荐同类型的电影
    probs_embeddings = (movie_matrics[movieid2idx[movie_id_val]]).reshape([1, 200])
    probs_similarity = tf.matmul(probs_embeddings, tf.transpose(normalized_movie_matrics))
    sim = (probs_similarity.numpy())
    #     results = (-sim[0]).argsort()[0:top_k]
    #     print(results)
    print("您看的电影是：{}".format(movies_orig[movieid2idx[movie_id_val]]))
    print("以下是给您的推荐：")
    p = np.squeeze(sim)
    p[np.argsort(p)[:-top_k]] = 0
    p = p / np.sum(p)
    # print(len(p))
    results = set()
    while len(results) != top_k:
        c = np.random.choice(28601, 1, p=p)[0]
        results.add(c)
    res = []
    for val in (results):
        res.append(movies_orig[val][1])

    return res

if __name__ == '__main__':
    print(recommend_same_type_movie(1, 20))