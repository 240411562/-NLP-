import collections
import math
import random
import jieba
import numpy as np
import tensorflow as tf
import os

# 导入第三方库

# 1.从文件中提取停止词和训练文本

def red_data():
    # 读取停用词
    stop_words = []
    with open("data/stopwords.txt","r",encoding="UTF-8") as fStopWords:
        line = fStopWords.readline()
        while line:
            stop_words.append((line[:-1])) #去\n
            line = fStopWords.readline()
        stop_words = set(stop_words)
        print("停用词表读取完毕，共{n}个词".format(n=len(stop_words)))
red_data()