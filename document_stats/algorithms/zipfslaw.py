import matplotlib.pyplot as plt
import pandas as pd
from document_stats.algorithms import preprocessingHelper
from operator import itemgetter
#from importlib import reload

#reload(preprocessingHelper)


doc_1 = 'Convolutional Neural Networks are very similar to ordinary Neural Networks from the previous chapter'
doc_2 = 'Convolutional Neural Networks take advantage of the fact that the input consists of images and they constrain the architecture in a more sensible way.'
doc_3 = 'In particular, unlike a regular Neural Network, the layers of a ConvNet have neurons arranged in 3 dimensions: width, height, depth.'
doc_4 = "acaba altı altmış ama ancak benim adım saltuk ben bilgi ünide okuyorum elli elli elli elli elli elli elli elli elli elli elli elli elli elli elli elli elli elli elli elli elli"

arr = [doc_1, doc_2, doc_3, doc_4]



def zipfAll(arr, useStopwords):
    str = ""
    for i in arr:
        str += i
        str += " "



    frequency = {}
    if useStopwords == True:
        str = preprocessingHelper.preprocessing(str)
    else:
        str = preprocessingHelper.preprocessing(str, False)


    for word in str:

        count = frequency.get(word, 0)
        frequency[word] = count + 1

    rank = 1
    column_header = ['Rank', 'Frequency', 'Frequency * Rank']
    df = pd.DataFrame(columns=column_header)
    collection = sorted(frequency.items(), key=itemgetter(1), reverse=True)

    for word, freq in collection:
        df.loc[word] = [rank, freq, rank * freq]
        rank = rank + 1

    plt.figure(figsize=(5, 5))  # to increase the plot resolution
    plt.ylabel("Frequency")
    plt.xlabel("Words")
    plt.xticks(rotation=40)  # to rotate x-axis values

    for word, freq in collection[:30]:
        #plt.bar(word, freq)
        plt.scatter(word, freq)

    return df, plt.show()



#dfd, pltt = zipfAll(arr, True)


#print(dfd)


"""
zipf Kanunu:
corpusumuzda en çok kullanılan kelimeler ve kaç defa kullanıldıkları bilgisine sahip olalım.

eğer kelimenin rankı ile kaç defa geçtiği bilgisini çarparsak ve bunu bütün kelimeler için yaparsak. Birbirine çok yakın
sonuçlar buluruz.

Bunu grafiğe döktüğümüzde ise x-ekseni = ranking | y-ekseni = kaç defa geçtiği;
bize sol üstten sağ alta doğru linearish bir çizgi çizdirir.

Ve bu kanun BÜTÜN dillere uymaktadır.

"""

"""
Uygulaması ile ilgili bir örnek (https://www.youtube.com/watch?v=fCn8zs912OE&ab_channel=Vsauce)

İngilizce'de "the" kelimesi en çok kullanılan 1. Kelime(wordcount.org) ve 181 milyon defa büyük İngilizce corpusunda geçiyor.

İngilizce'de "sauce" kelimesi en çok kullanılan 5555. Kelime. Zipf's law sayesinde bu kelimenin corpusta kaç defa geçtiğini
tahminleyebiliriz.

"the"       1.      181Milyon
"sauce"     5555.       x

181Milyon x (1/5555) = 30000

Zipf's Law a göre sauce kelimesi 30bin kere corpusta geçer. Gidip gerçekten sauce kelimesinin frekansına bakarsak:
29594 kere geçtiğini görürüz neredeyse 30bin e eşit.

Zipf yasası sadece dilde değil hayattaki her şeye uyar. Türkiye gibi düzensiz nüfusa sahip olan bir ülkede bile
şehirlere göre yerleşim zipf yasasına uyuyor.

"""
