# -*- coding:utf-8 -*-

import sys
sys.path.append('utils/')
from preprocess import *
from sentianalysis import *

#
stopword_path = 'dict/stop_words.txt'
degreeword_path = 'dict/degreewords.txt'
sentimentword_path = 'dict/sentiment_word_score.txt'
deny_path = 'dict/denial_dict.txt'

# 停用词列表
stopwords = load_data(stopword_path)
#否定词表
notword = load_data(deny_path)
#程度词表
degree_dict = file2dict(degreeword_path)
#情感词表
sentiment_dict = file2dict(sentimentword_path)


text = '还可以，比预计时间晚了一小时到，不过还好'
#text = '不太好吃，相当难吃，要是米饭再多点儿就好了'
# text = "剁椒鸡蛋好咸,土豆丝很好吃"
print('%s的情感值为：%.4f' % (text, sents_score(text, sentiment_dict, degree_dict, notword)))
print(f'{text}\n情感值：{sents_score(text, sentiment_dict, degree_dict, notword)}')