#!-*- coding:utf-8 -*-

__author__ = 'houlisha'


from __future__ import division
from collections import Counter

import IDFLoader

D_filename = ""


def BM25(Q, D, word_idf):
    # score(Q,D) = sum(IDF(qi) * (TF(qi) * (k + 1)) / (TF(qi) + k * (1- b + b * (|D|/avgdl))))
    # return: the bm25 score of Q with all Documents
    #         bm_scores = [score(Q, D1), score(Q, D2), ...]

    bm_scores = []

    # param
    k = 1.2  # [1.2, 2.0]
    b = 0.75
    avgdl = sum([len(doc) for doc in D]) / len(D)
    for doc in D:
        D_words = Counter(doc)
        scores = 0.0
        for q in Q:
            tf = D_words.get(q, 0)
            tmp = k * (1 - b + b * (len(doc) / avgdl))
            score = word_idf.get(q, 0) * (tf * (k + 1)) / (tf + tmp)
            scores += score
        bm_scores.append(scores)

    return bm_scores


def main():
    D_texts = [line.strip().split(" ") for line in open(D_filename).readlines()]
    word_idf = IDFLoader.idfWithSmooth(D_texts)

    query = ["word1", "word2", "word3"]

    bm25_score = BM25(query, D_texts, word_idf)
    return bm25_score

if __init__ == "__main__":
    main()