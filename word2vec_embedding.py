# coding:utf8
import jieba.posseg as postag
import numpy as np
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity

embedding_path = "2000000-small.txt"
embedding_path2 = "./500000-small.txt"
embedding_path3 = "./tencent_45000.txt"


try:
    model200 = KeyedVectors.load_word2vec_format(embedding_path, binary=False, unicode_errors='ignore')
    print("use txt")
except:
    model200 = KeyedVectors.load_word2vec_format(embedding_path, binary=True)
    print("use bin")



try:
    model50 = KeyedVectors.load_word2vec_format(embedding_path2, binary=False, unicode_errors='ignore')
    print("use txt")
except:
    model50 = KeyedVectors.load_word2vec_format(embedding_path2, binary=True)
    print("use bin")


try:
    model45000 = KeyedVectors.load_word2vec_format(embedding_path3, binary=False, unicode_errors='ignore')
    print("use txt")
except:
    model45000 = KeyedVectors.load_word2vec_format(embedding_path3, binary=True)
    print("use bin")


# model = KeyedVectors.load_word2vec_format(embedding_path, binary=True)
# 词性加权一下
pos_weight = {
    "n": 10,  # 名词
    "N": 10,  # 名词
    "t": 5,  # 时间词
    "s": 5,  # 处所词
    "f": 3,  # 方位词
    "v": 10,  # 动词
    "a": 10,  # 形容词
    "A": 10,  # 形容词
    "b": 5,  # 区别词
    "z": 5,  # 状态词
    "r": 5,  # 代词
    "m": 5,  # 数词
    "q": 5,  # 量词
    "d": 8,  # 副词
    "p": 5,  # 介词
    "c": 1,  # 连词
    "u": 1,  # 助词
    "e": 1,  # 叹词
    "y": 1,  # 语气词
    "o": 1,  # 拟声词
    "h": 1,  # 前缀
    "k": 1,  # 后缀
    "x": 1,  # 字符串
    "w": 1,  # 标点符号
    "j": 10,  # 简称略语
    "i": 10,  # 成语
    "l": 10,  # 习用语
}


def get_word_embedding(word, model):
    try:
        return model[word]
    except Exception as e:
        # print(repr(e))
        emb = []
        for char in word:
            try:
                emb.append(model[char])
            except Exception as e:
                # print(repr(e))
                pass
        if len(emb):
            _ = np.average(emb, axis=0)
            # print(_)
            return _
        else:
            return np.zeros(200)


def get_sentence_embedding(sentence_, model):
    total_w = 0
    sum_array = np.zeros(200)
    for w, t in postag.cut(sentence_):
        # print(w, t)
        weight = pos_weight.get(t[0], 1)
        total_w += weight
        arr = weight * get_word_embedding(w, model)
        # sum_array = np.add(sum_array, arr)
        sum_array += arr
    sum_array /= total_w
    return sum_array


def cosine_similarity_1(x, y):
    """需要处理异常情况，如0，这里就不用它了，使用 sklearn接口即可"""
    num = x.dot(y.T)
    de_nom = np.linalg.norm(x) * np.linalg.norm(y)
    return num / de_nom


def predict(text_a, text_b, model):
    embedding_a = get_sentence_embedding(text_a, model)
    # print(embedding_a)
    embedding_b = get_sentence_embedding(text_b, model)
    res = cosine_similarity([embedding_a, embedding_b])[0][1]
    # res = cosine_similarity_1(embedding_a, embedding_b)
    # print("cos:{}".format(cosine_similarity_1(embedding_a, embedding_b)))
    return res


if __name__ == "__main__":
    a = model["你好"]
    print("embedding:{}".format(a))
    print("most similar words:{}".format(model.most_similar("你好")))
    sentence = "今天天气不错啊"
    sentence_e = get_sentence_embedding(sentence)
    #
    # e = cosine_similarity(X=[d], Y=[d, d])
    # print("e::::", e)

    e = cosine_similarity(X=[[0, 1]], Y=[[0, 1], [0, 2], [1, 2], [2, 3]])
    # ok
    print("e::::", e)

    # print(predict("我很爱你呢", "我非常爱你"))
    #
    print(predict("鲁班七号", "你是谁"))
    print(predict("你是那个", "你是谁"))
    print(predict("对的啊", "不错啊啊啊"))
    print(predict("对的啊", "不对啊"))
    print(predict("不错啊", "不对啊"))
    print(predict("你知道那个事情吗", "我不是很了解"))
    """
    从结果看，rank还行，相似度得分好像 ...起没有语序
    """


def sentence2word(sentence,model):
    res = dict()
    sum_array = np.zeros(200)
    for w, t in postag.cut(sentence):
        # print(w, t)
        weight = pos_weight.get(t[0], 1)
        print(w, weight)
        words = dict(model.most_similar(w, topn = 20))
        for word in words.keys():
            if res.get(word):
                res[word] += weight * words[word]
            else:
                res[word] = weight * words[word]
        print(res)

    res = sorted(res.items(), key=lambda x: x[1], reverse=True)
    return res[:10]


