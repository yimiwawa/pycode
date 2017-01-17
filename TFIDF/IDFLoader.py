#!-*- coding:utf-8 -*-

__author__ = "houlisha"

from __future__ import division
import math


def idf(texts):
    # IDF(wi) = log{ N / DF(wi)}
    word_df = {}
    for line in texts:
        lineset = set(line)
        for word in lineset:
            word_df[word] = word_df.get(word, 0) + 1
    N = len(texts)
    word_idf = {word: math.log10(N / word_df.get(word)) for word in word_df.items()}
    return word_idf


def loadIdf(filename):
    word_idf = {}
    for line in open(filename):
        word, pred = line.strip().split(" ")
        word_idf[word] = float(pred)
    return word_idf


def idfWithSmooth(texts):
    # IDF(wi) = log{(N - DF(wi) + 0.5) / (DF(wi) + 0.5)}
    word_df = {}
    for line in texts:
        lineset = set(line)
        for word in lineset:
            word_df[word] = word_df.get(word, 0) + 1
    N = len(texts)
    word_idf = {word: math.log10((N - word_df.get(word) + 0.5) / (word_df.get(word) + 0.5)) for word in word_df.items()}
    return word_idf