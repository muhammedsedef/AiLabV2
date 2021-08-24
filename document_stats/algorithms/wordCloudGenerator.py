from wordcloud import WordCloud
import matplotlib.pyplot as plt
from document_stats.algorithms import preprocessingHelper



doc_1 = 'Convolutional Neural Networks are very similar to ordinary Neural Networks from the previous chapter'
doc_2 = 'Convolutional Neural Networks take advantage of the fact that the input consists of images and they constrain the architecture in a more sensible way.'
doc_3 = 'In particular, unlike a regular Neural Network, the layers of a ConvNet have neurons arranged in 3 dimensions: width, height, depth.'
doc_4 = "saf saofjıosafıjsa fkjdsjfdjlf gıosdılgkdslgkd saf saf elli elli elli elli elli altmış altmış altmış altmış ben ben ben ben ben ben ConvNet ConvNet ConvNet ConvNet ConvNet ConvNet ConvNet ConvNet ConvNet ConvNet ConvNet ConvNet ConvNet ConvNet ConvNet ConvNet ConvNet ConvNet ConvNet ConvNet ConvNet ConvNet ConvNet ConvNet ConvNet "
docs = [doc_1, doc_2, doc_3, doc_4]


def wordCloudAll(corpus, useStopwords):
    str = ""
    for i in corpus:
        str += i
        str += " "
    print(str)
    if useStopwords == True:
        str = preprocessingHelper.preprocessing_(str)
    else:
        str = preprocessingHelper.preprocessing_(str, False)


    wc = WordCloud(background_color='white').generate(str)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    return plt.show()


#wordCloudAll(docs, False)



def wordCloud(corpus, useStopwords):
    wordCloudList = []

    if useStopwords == True:
        corpus = preprocessingHelper.alldocclean_(corpus)
    else:
        corpus = preprocessingHelper.alldocclean_(corpus, False)

    for sample in corpus:
        plt.figure()
        wc = WordCloud(background_color='white').generate(sample)
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        wordCloudList.append(plt.show())

    return wordCloudList


#wordCloud(docs, False)
