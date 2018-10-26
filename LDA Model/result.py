import os
import nltk
import codecs
import numpy as np
import matplotlib.pyplot as plt

from time import time
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.externals import joblib

lda_ModelPath = os.path.join('model', 'ldaModels.model')  # 保存训练的lda模型
n_top_words = 40
n_features = 2500
index = 1;  #由训练模型时获得

# 文本预处理
def textPrecessing(text):
    #拿出代码停用词 可继续补充
    f2 = codecs.open('codestopwords.txt', "r", encoding='utf-8')
    codewd = f2.read()
    codewd = codewd.splitlines()
    for desc in codewd:
        codewdLst = nltk.word_tokenize(desc)
    # 分词
    wordLst = nltk.word_tokenize(text)
    # 去除停用词
    filtered = [w for w in wordLst if (w not in codewdLst or w not in stopwords.words('english'))]
    #filtered = [w for w in wordLst if w not in stopwords.words('english')]
    # 仅保留名词和动词
    refiltered = nltk.pos_tag(filtered)
    filtered = [w for w, pos in refiltered if (pos.startswith('NN') or pos.startswith('VB'))]

    # 词干化
    #ps = PorterStemmer()
    #filtered = [ps.stem(w) for w in filtered]
    return " ".join(filtered)


# 打印topic_top_word
def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("fn:")
        print(feature_names)
        print("lens of fn")
        print(len(feature_names))
        print("topic:")
        print(topic)
        #print("type of topic")
        #print(type(topic))
        print("Topic #%d:" % topic_idx)
        j=0
        temp_name = ''
        for i in topic.argsort():
            j=j+1
            if(j>=7):
                break
            temp = int(len(topic)//len(feature_names))
            i = i//temp
            #print("i:%d"%i)
            if(feature_names[i] != temp_name):
                temp_name = feature_names[i]
                print(feature_names[i],end=" ")
            #print("".join(feature_names[i]))
                  #for i in topic.argsort()[:-n_top_words - 1:-1]]))
    #print
    '''
    with open(os.path.join('lda_result', 'res_topic_word.csv'), 'w') as f:
        f.write("Topic, Top Word\n")
        for topic_idx, topic in enumerate(model.components_):
            f.write(str(topic_idx) + ',')
            topic_word_dist = [(feature_names[i], topic[i])
                              r i in topic.argsort()[:-n_top_words - 1:-1]]
            for word, score in topic_word_dist:
                f.write(word + '#' + str(score) + ';')
            f.write('\n')
    '''


f = codecs.open('testdata.txt','r',encoding = 'utf-8')
content = f.read()
content = content.splitlines()
print(content)

docLst = []
for desc in content:
    docLst.append(textPrecessing(desc))
print('代码预处理完毕！\n')
print("docLst:\n")
print(docLst)
print('\n')

print("开始统计词频\n")
tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2,
                                max_features=n_features,
                                stop_words='english')
tf = tf_vectorizer.fit_transform(docLst)


print("LDA模型进行测试！\n")
lda_models = joblib.load(lda_ModelPath)
tf_vectorizer._validate_vocabulary()
tf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(lda_models[1], tf_feature_names, n_top_words)

