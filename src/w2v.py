from gensim.models import word2vec
import os
import path
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def model_train(sentences):
    print "Start train"
    model = word2vec.Word2Vec(sentences, sg = 1, size = 128, window = 5, min_count = 1, workers = 4 )
    print "Saving model"
    # Save model
    model.save(path.W2V_MODEL)
    return model

def get_most_similar(model, word, top_n):
    print "Get Most Similar Topn words of " + word + " is:" 
    similar_list = model.most_similar(word, topn = top_n)
    for items in similar_list:
        print items[0], items[1]

def cal_similarity(model, word1, word2):
    print "Calculate similarity between:" + word1 + " and " + word2 + "is"
    try:
        similarity = model.similarity(word1, word2)
    except KeyError:
        similarity = 0
    print similarity

def model_test(model):
    get_most_similar(model, 'door', 3)
    cal_similarity(model, 'death', 'food')

if __name__ == '__main__':
    sentence = word2vec.Text8Corpus(path.SPLIT_WORD)   
    if not os.path.exists(path.W2V_MODEL):
        model_train(sentence)
    else:
        trained_model = word2vec.Word2Vec.load(path.W2V_MODEL)
        model_test(trained_model)
        