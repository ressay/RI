import string
from math import log10

N = 4
docList = [1,2,3,4]
listcar = {'.', ',', '!', '?', '’'}
stoplist = open('stopwords_fr.txt', 'r')
stoplist = stoplist.read()
stoplist = stoplist.lower()
stoplist = stoplist.split()
def generateReversedFile(path="TPRI/D",N=4):
    k = 1
    freq = {}  # dict vide


    while k <= N:
        # print("------------------------Indexe de fréquences du document", k, "-------------------")
        f = open(path + str(k) + '.txt', 'r')
        t = f.read()
        t = t.lower()
        i = 0
        while i < len(t):
            if t[i] in listcar:
                t = t.replace(t[i], " ")
            i += 1
        a = t.split()
        for w in a:
            if w not in stoplist and len(w) > 1:
                if (w, k) not in freq:
                    freq[w, k] = a.count(w)
                    # print(w, freq[w, k])
        k += 1
        f.close()
    # print("Le fichier inverse de la collection ")
    # for word in freq:
    #     print(word)
    return freq

def generateFreqOfQuery(query):
    query = query.lower()
    import re
    a = re.split('\s+',query)
    i = 0
    while i < len(query):
        if query[i] in listcar:
            query = query.replace(query[i], " ")
        i += 1

    f = {}
    for w in a:
        if w not in stoplist and len(w) > 1:
            if w not in f:
                f[w] = a.count(w)

    return f

#Exercice 02
def indexdoc(freq,d): #fonction pr 1 document
    # print("l'index du Document ",d," est")
    f = {}
    for(a,b) in freq:
        if b==d:
            f[a] = freq[a,b]
    return f

def indexmot(freq,w):  #fonction pr 1 mot
    # print("l'index du mot ",w," est")
    f = {}
    for(a,b) in freq:
        if a==w:
            f[b] = freq[a,b]
    return f

def getNi(freq):
    ni = {}
    for (w,d) in freq:
        if w not in ni:
            ni[w] = 0
        ni[w] += 1
    return ni

def maxFreq(freq):
    maxF = {}
    for doc in docList:
        maxF[doc] = max([freq[w,d] for (w,d) in freq if d==doc])
    return maxF

def getWeights(freq):
    ni = getNi(freq)
    maxes = maxFreq(freq)
    poids = {}
    for (w, d) in freq:
        poids[w, d] = (freq[w, d] / maxes[d]) * log10(N / ni[w]+1)
    return poids



freq = generateReversedFile()
#appel des fonctions
# d=int(input("Donner le numéro du document "))
# f = indexdoc(freq,d)
# print(f)
# w=input("Donner un mot ")
# w=w.lower()
# f = indexmot(freq,w)
# print(f)


