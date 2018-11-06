import VectorialModel
import basicMethods as bm
from BooleanModel import getDocScores


def getFreq(freqs,w,d):
    if (w,d) in freqs:
        return freqs[w,d]
    return 0

def getIndex(index,key):
    if key in index:
        return index[key]
    return 0

def formatDocWeightsOutput(weights,freqs,word,N):
    output = []
    ws = bm.indexmot(weights,word)
    fs = bm.indexmot(freqs,word)
    print(bm.fd(weights, word, 3))
    print(fs)
    print(ws)
    for d in range(1,N+1):
        output.append([d,getIndex(fs,d),getIndex(ws,d)])
    return output

def formatWeightsPerDocOutput(weights,freqs,d,N):
    output = []
    ws = bm.indexdoc(weights,d)
    fs = bm.indexdoc(freqs,d)
    for w in fs.keys():
        output.append([w,getIndex(fs,w),getIndex(ws,w)])
    return output

def formatWeightsBoolean(freqs,query,N):
    output = []
    docs = getDocScores(freqs,query,N)
    for i,doc in enumerate(docs):
        if doc:
            output.append([doc])
    return output

def formatWeightsVec(freqs,query,N,method):
    output = []
    docs = VectorialModel.getDocScores(freqs,query,N)
    for i,doc in enumerate(docs):
        output.append([i,doc])
    return output

