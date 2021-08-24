from collections import Counter
from nltk.util import ngrams
from document_stats.algorithms import preprocessingHelper



doc_1 = 'Convolutional Neural Networks are very similar to ordinary Neural Networks from the previous chapter'
doc_2 = 'Convolutional Neural Networks take advantage of the fact that the input consists of images and they constrain the architecture in a more sensible way.'
doc_3 = 'In particular, unlike a regular Neural Network, the layers of a ConvNet have neurons arranged in 3 dimensions: width, height, depth.'
docs = [doc_1, doc_2, doc_3]


def bigramsAll(corpus, n_word, n_most, useStopwords):
    bigram_list = []


    txt = ""
    for i in corpus:
        txt += i
        txt += " "

    if useStopwords == True:
        txt = preprocessingHelper.preprocessing(txt)
    else:
        txt = preprocessingHelper.preprocessing(txt, False)

    bi_grams = list(ngrams(txt, n_word))
    most_occur = Counter(bi_grams).most_common(n_most)
    bigram_list.append(most_occur)

    return bigram_list


"""

#  All corpus was selected
def bigramsAll(corpus, n_word, n_most):
    print("bigramsAll fonsiyonundayım")
    bigram_list = []
    print("n_word ",n_word)
    print("n_most ",n_most)
    print("bigramsAll a gelen corpus = ",corpus)



    txt = ""
    for i in corpus:
        txt += i
        txt += " "
    txt = preprocessingHelper.preprocessing(txt)

    bi_grams = list(ngrams(txt, n_word))
    most_occur = Counter(bi_grams).most_common(n_most)
    bigram_list.append(most_occur)

    # print(bigram_list)
    return bigram_list
"""

#print(bigramsAll(docs,2,5, False))

#print(bigramsAll([doc_1],2,5, False))



def bigrams(corpus, n_word, n_most, useStopwords):
    bigram_list = []
    if useStopwords == True:
        corpus = preprocessingHelper.alldocclean_(corpus)
    else:
        corpus = preprocessingHelper.alldocclean_(corpus, False)
    split_list = list(map(str.split, corpus))

    for sample in split_list:
        bi_grams = list(ngrams(sample, n_word))
        most_occur = Counter(bi_grams).most_common(n_most)
        bigram_list.append(most_occur)

    return bigram_list


#print(bigrams(docs,2,2,False))

"""
# if 1by1 was selected
def bigrams(corpus, n_word, n_most):
    print("bigrams fonsiyonundayım")
    print("n_word: ",n_word)
    print("n_most: ",n_most)
    print("bigrams a gelen corpus: ",corpus)

    bigram_list = []
    corpus = preprocessingHelper.alldocclean_(corpus)
    split_list = list(map(str.split, corpus))

    for sample in split_list:
        bi_grams = list(ngrams(sample, n_word))
        most_occur = Counter(bi_grams).most_common(n_most)
        bigram_list.append(most_occur)

    return bigram_list


#print(bigrams(docs,2,2))

"""
