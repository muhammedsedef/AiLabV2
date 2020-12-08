from collections import Counter
from document_stats.algorithms import preprocessingHelper

def frequency(corpus, n_most):
    list_of_frequency = []

    txt = ""
    for i in corpus:
        txt += i
        txt += " "
    txt = preprocessingHelper.preprocessing(txt)


    most_occur = Counter(txt).most_common(n_most)
    list_of_frequency.append(most_occur)

    return list_of_frequency

"""
doc_1 = 'Convolutional Neural Networks are very similar to ordinary Neural Networks from the previous chapter'
doc_2 = 'Convolutional Neural Networks take advantage of the fact that the input consists of images and they constrain the architecture in a more sensible way.'
doc_3 = 'In particular, unlike a regular Neural Network, the layers of a ConvNet have neurons arranged in 3 dimensions: width, height, depth.'
docs = [doc_1, doc_2, doc_3]


print(frequency(docs,5))

"""



def frequencySep(corpus, n_most):
    corpus = preprocessingHelper.alldocclean_(corpus)
    split_list = list(map(str.split, corpus))
    list_of_frequency = []


    for sample in split_list:
        most_occur = Counter(sample).most_common(n_most)
        list_of_frequency.append(most_occur)

    return list_of_frequency

#print(frequencySep(docs, 5))
