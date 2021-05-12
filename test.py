# coding:utf8
import jieba.posseg as postag
import numpy as np
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity

print('后羿、鲁班七号相似度' +' '+ str(model.similarity('后羿','鲁班七号')))#计算两词相关度

print('与后羿最相关的10个词')
model.most_similar('后羿', topn=10)#计算与词相关度最高的词

print('与鲁班最相关的10个词')
model.most_similar('鲁班', topn=10)

print('与ak47最相关的10个词')
model.most_similar('ak47', topn=10)

print('测试国王+女人-男人结果')
model.most_similar(positive=['女人', '国王'], negative=['男人'], topn=10)

model200.doesnt_match(['后羿','鲁班','艾希','程咬金','亚瑟']) #查找明显异于其他的词


#短句子相似度
print('45000词库',predict('适合新手的射手英雄','像鲁班七号的远程英雄',model45000))
print('500000词库',predict('适合新手的射手英雄','像鲁班七号的远程英雄',model50))


#测试两篇后羿内容的相似度
with open("houyi1.txt", "r",encoding = 'utf-8') as f:  # 打开文件
    text1 = f.read()  # 读取文件


with open("houyi2.txt", "r",encoding = 'utf-8_sig') as f:  # 打开文件
    text2 = f.read()  # 读取文件

print('45000词库', predict(text1, text2, model45000))
print('500000词库', predict(text1, text2, model50))

#测试后羿内容与典韦内容的相似度
with open("houyi1.txt", "r",encoding = 'utf-8') as f:  # 打开文件
    text1 = f.read()  # 读取文件


with open("dianwei.txt", "r",encoding = 'utf-8_sig') as f:  # 打开文件
    text2 = f.read()  # 读取文件


print('45000词库', predict(text1, text2, model45000))
print('500000词库', predict(text1, text2, model50))

# 测试典韦内容与凤凰新闻内容的相似度
with open("fhnews.txt", "r", encoding='utf-8') as f:  # 打开文件
    text1 = f.read()  # 读取文件

with open("dianwei.txt", "r", encoding='utf-8_sig') as f:  # 打开文件
    text2 = f.read()  # 读取文件

print('45000词库', predict(text1, text2, model45000))
print('500000词库', predict(text1, text2, model50))


# 测试王者荣耀内容与DNF内容的相似度
with open("dnf.txt", "r", encoding='utf-8') as f:  # 打开文件
    text1 = f.read()  # 读取文件

with open("dianwei.txt", "r", encoding='utf-8_sig') as f:  # 打开文件
    text2 = f.read()  # 读取文件

print('45000词库', predict(text1, text2, model45000))
print('500000词库', predict(text1, text2, model50))