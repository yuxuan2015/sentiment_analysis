#-*- coding:utf-8 _*-
"""
@author:lyy
@file: sentiment_model.py
@time: 2019/06/11
@Software: PyCharm
"""

##参考：https://kexue.fm/archives/3360


import os
import jieba
import logging

main_path = os.path.dirname(os.path.abspath(__file__))

##添加jieba中没有的词
jieba.setLogLevel(logging.INFO)
userdict_path = main_path +'/dict/userdict_add.txt'
jieba.load_userdict(userdict_path)

negdict = set([value.strip().replace("\n", "") for value in open(main_path +'/dict/neg.txt', encoding="utf8").readlines()])
posdict = set([value.strip().replace("\n", "") for value in open(main_path +'/dict/pos.txt', encoding="utf8").readlines()])
nodict = set([value.strip().replace("\n", "") for value in open(main_path +'/dict/no.txt', encoding="utf8").readlines()])
plusdict = set([value.strip().replace("\n", "") for value in open(main_path +'/dict/plus.txt', encoding="utf8").readlines()])


#预测函数
def predict(s):
	p = 0
	# sd = [str(term) for term in  HanLP.segment(s)]
	sd = jieba.lcut(s)
	for i in range(len(sd)):
		if sd[i] in negdict:
			if i>0 and sd[i-1] in nodict:
				p = p + 1
			elif i>0 and sd[i-1] in plusdict:
				p = p-2
			else: p = p-1
		elif sd[i] in posdict:
			if i>0 and sd[i-1] in nodict:
				p = p-1
			elif i>0 and sd[i-1] in plusdict:
				p = p+2
			elif i>0 and sd[i-1] in negdict:
				p = p-1
			elif i<len(sd)-1 and sd[i+1] in negdict:
				p = p-1
			else: p = p+1
		elif sd[i] in nodict:
			p = p-0.5
	return p


##计算极性
def text_polarity(s):
	score = predict(s)
	if score > 0:
		polarity = "positive"
	elif score < 0:
		polarity = "negative"
	else:
		polarity = "neutral"
	return polarity


##测试例子
if __name__ == "__main__":
	text = "这个黑心老板太恶心了"
	print(text_polarity(text))
