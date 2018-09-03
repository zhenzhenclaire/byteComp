import os

POJ_ROOT = '/Users/claire/ByteDance/Bytecup2018/byteComp'

DATA_ROOT = os.path.join(POJ_ROOT, 'data')
TRAIN_DATA_DIR = os.path.join(DATA_ROOT, 'train')
TEST_DATA_DIR = os.path.join(DATA_ROOT, 'test')
MODEL_DIR = os.path.join(POJ_ROOT, 'model')

SPLIT_WORD = os.path.join(TRAIN_DATA_DIR, 'word2vectrain')
W2V_MODEL = os.path.join(MODEL_DIR, 'word2vec.model')
