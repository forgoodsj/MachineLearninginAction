#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/3/5
# __author__ = 'jun'
from numpy import *


def loadDataSet():  # 创建实验样本，将词条切分后的文档集合，将标点符号去掉了
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1表示含有侮辱性文字，0表示正常言论
    return postingList, classVec


def createVocabList(dataSet):  # 创建一个包含在所有文档中出现的不重复词的列表
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)  # 创建两个集合的并集
    return list(vocabSet)


def setOfWords2Vec(vocabList, inputSet):
    # 输入参数为词汇列表和某个文档，输出的是文档向量，每个元素为1或0，分别表示词汇列表中的单词在输入文档中是否出现，如果出现则该位置返回1，如果没出现则为0。如果inputSet中出现了词汇列表中没有的单词，则返回报错
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word: %s is not my Vocabulary!" % word)
    return returnVec


# listOfPosts,listClasses = loadDataSet()
# myVocabList = createVocabList(listOfPosts)
# print(myVocabList)
# print(listOfPosts[0])
# print(setOfWords2Vec(myVocabList,listOfPosts[0]))

def trainNB0(trainMarix, trainCategory):
    # 输入文档矩阵trainMarix,由多个词条在词汇列表中是否出现的向量组成的矩阵
    # 输入参数2：每篇文档类别标签构成的向量，这里假设标签只有0和1，如果有多个，这里需要额外变更
    numTrainDocs = len(trainMarix)  # 输入文档中词条的数量
    numWords = len(trainMarix[0])  # 单词列表总长度
    pABusive = sum(trainCategory) / float(numTrainDocs)  # 侮辱性词条占比
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0Denom = 2.0  # 初始化概率1/2
    p1Denom = 2.0  # 初始化概率为1/2
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMarix[i]  # 向量相加
            p1Denom += sum(trainMarix[i])
        else:
            p0Num += trainMarix[i]
            p0Denom += sum(trainMarix[i])
    p1Vect = log(p1Num / p1Denom)  # 向量除以总数。向量是每个单词出现在含有侮辱性单词的句子中的次数，总数是含有侮辱性单词句子的总的单词数量
    # 得到的结果就是每个单词是侮辱性单词的概率
    # 取对数是为了以后在求句子概率的时候，避免过多小数相乘得到0，所以要用对数,然后对数相加
    p0Vect = log(p0Num / p0Denom)
    return p0Vect, p1Vect, pABusive


# trainMat = []
# for postinDoc in listOfPosts:
#     trainMat.append(setOfWords2Vec(myVocabList,postinDoc))

# p0v,p1v,pAn = trainNB0(trainMat,listClasses)
#
# print(p0v)

def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    # vec2Classify 要分类的向量（词条在词汇列表中是否出现的向量），以及3个概率
    p1 = sum(vec2Classify * p1Vec) + log(
        pClass1)  # 理论上应该是概率相乘，因为怕小数相乘后得到0，所以取对数后相加。pclass1为词条本身为侮辱性词条的占比（侮辱词条/总词条）。原公式为p(ci|w)=p(w|ci)p(ci)/p(w) ，对这个公式取对数。
    # ci为侮辱性词条的概率。
    # p(w|ci)为 单词在侮辱性词条中出现的概率。
    # w为所有单词，概率相乘
    # 最后是比较p1和p0的大小，所以可以不用除以都有的p(w）。
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)  # 因为只有0和1，所以1-p1 就是p0
    if p1 > p0:
        return 1
    else:
        return 0


def testingNB():
    listOfPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOfPosts)
    trainMat = []
    for postinDoc in listOfPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0v, p1v, pAn = trainNB0(array(trainMat), array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0v, p1v, pAn))
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0v, p1v, pAn))


testingNB()
