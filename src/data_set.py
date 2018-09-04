
#!/usr/bin/python2
#-*- coding: UTF-8 -*-
import json
import os
import re
from nltk.corpus import stopwords
import nltk

# pip install nltk
# nltk.download('stopwords')
# nltk.download('punkt')

'''
define news struct
'''
class NewsInfo(object):

    def __init__(self,id,title,content):
        self.id = id
        self.title = title
        self.content = content
'''
parse news content title id
object
    content
    title
    id
'''
def parse_data(line):
    news =  json.loads(line)
    newsInfo = NewsInfo(news['id'],news['title'],news['content'])
    return newsInfo

'''
parse data from file
'''
def read_file(path):
    files = []
    if os.path.isdir(path):
        files = os.listdir(path)
    else:
        files.append(path)
    results = []
    for filepath in files:
        with open(filepath) as file:
            line = file.readline()
            while line is not None and len(line) > 0:
                try:
                    results.append(parse_data(line))
                    line = file.readline()
                except Exception as e:
                    print(e)
    return results
'''
word split
'''
def participle(line):
    words = nltk.word_tokenize(line)
    result = [w for w in words if(w not in stopwords.words('english'))]
    return result


'''
build word2vector train set

'''
def build_word2vec_trainset(input_path,output_path):
    writer = open(output_path, "w")
    news = read_file(input_path)
    for newsinfo in news:
        writer.write(' '.join(participle(newsinfo.title)).encode("utf-8")+'\n')
        writer.write(' '.join(participle(newsinfo.content)).encode("utf-8")+'\n')
    writer.close()


path = '/Users/huangzhongnan/Downloads/bytecup2018/test'
news = read_file(path)

for newsinfo in news:
    title = newsinfo.title
    print(title)
    print(participle(title))

build_word2vec_trainset(path,"word2vectrain")