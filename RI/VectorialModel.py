import RI.basicMethods as bm
import math

def f(freq,w,d):
    if (w,d) in freq:
        return freq[w,d]
    return 0

def scoreInnerProduct(freq,fquery,d):
    return sum([fquery[w]*f(freq,w,d) for w in fquery])

def scoreCoefDice(freq,fquery,d):
    up = 2*scoreInnerProduct(freq,fquery,d)
    down = sum([fquery[w]*fquery[w]+f(freq,w,d)*f(freq,w,d) for w in fquery])
    return up/down

def scoreCosin(freq,fquery,d):
    up = scoreInnerProduct(freq,fquery,d)
    down = math.sqrt(sum([fquery[w]*fquery[w]+f(freq,w,d)*f(freq,w,d) for w in fquery]))
    return up/down

def scoreJaccard(freq,fquery,d):
    up = scoreInnerProduct(freq,fquery,d)
    down = sum([fquery[w]*fquery[w]+f(freq,w,d)*f(freq,w,d) for w in fquery]) - up
    return up / down


def getDocScores(query="first and king or memories",
                 path="TPRI/D",N=4,computeFunction=scoreInnerProduct):
    freq = bm.generateReversedFile(path,N)

    fquery = bm.generateFreqOfQuery(query)

    docList = []
    for d in range(1, N+1):
        score = computeFunction(freq,fquery,d)
        docList.append(score)
    # print(docList)
    return docList

print(getDocScores())
print(getDocScores(computeFunction=scoreCoefDice))
print(getDocScores(computeFunction=scoreCosin))
print(getDocScores(computeFunction=scoreJaccard))