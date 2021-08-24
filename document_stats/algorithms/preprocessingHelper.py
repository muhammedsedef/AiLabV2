import nltk
from nltk.tokenize import word_tokenize
import string
import re


def stopwords(text):
    # for adding new stopwords in ntlk-stopwords
    #file = open(f"{os.path.dirname(__file__)}/turkce-stop-words.txt")
    file = open("document_similarity/algorithms/turkce-stop-words.txt")
    stop_words_extra = file.read()
    stopWords = nltk.corpus.stopwords.words('turkish')
    for i in stop_words_extra.split():
        stopWords.append(i)

    str = ""
    words = [word for word in text.split() if word not in stopWords]
    for i in words:
        str += i
        str += " "
    return str


# converts capital letters to lowercase in text
def text_lowercase(text):
    return text.lower()


# removing numbers from text
def remove_numbers(text):
    result = re.sub(r'\d+', '', text)
    return result


# removing punctuations in text
def remove_punctuations(text):
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator)


# removing whitespace in text
def remove_whitespace(text):
    return " ".join(text.split())


# tokenize text



def tokenizer(text):
    text = re.sub('^^\x20-\x7E', '', text) # ^^\x20-\x7E regex kodu. harf sayı noktalama haricindeki bütün karakterleri siliyor.
    return word_tokenize(text)


# preprocessing for texts
def preprocessing(cleaned, useStopwords=True):
    cleaned = remove_whitespace(cleaned)
    cleaned = remove_numbers(cleaned)
    cleaned = remove_punctuations(cleaned)
    valid_characters = 'abcçdefgğhıijklmnoöpqrsştuüvwxyzQWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ1234567890 '
    cleaned = ''.join([x for x in cleaned if x in valid_characters]) # yukarıdaki valid charlar içinde olmayan karakterleri silme.
    cleaned = text_lowercase(cleaned)
    if useStopwords == True:
        cleaned = stopwords(cleaned)

    cleaned = tokenizer(cleaned)
    return cleaned


# preprocessing for texts
def preprocessing_(doc, useStopwords = True): # harf, sayı, noktalama dışındaki karakterleri de tutuyor.
    cleaned = doc
    cleaned = remove_whitespace(cleaned)
    cleaned = remove_numbers(cleaned)
    cleaned = remove_punctuations(cleaned)
    cleaned = text_lowercase(cleaned)
    if useStopwords == True:
        cleaned = stopwords(cleaned)

    return cleaned


# preprocessing for all documents
def alldocclean(alldocuments, useStopwords = True):
    predocs = []
    for i in alldocuments:
        if useStopwords == True:
            predoc = preprocessing(i)
        else:
            predoc = preprocessing(i, False)
        predocs.append(predoc)
    return predocs  # predocs contains all cleared texts


# preprocessing for all documents
def alldocclean_(alldocuments, useStopwords = True):
    predocs = []
    for i in alldocuments:
        if useStopwords == True:
            predoc = preprocessing_(i)
        else:
            predoc = preprocessing_(i, False)

        predocs.append(predoc)
    return predocs  # predocs contains all cleared texts
# totalwords() -> get the cleaned document list
# return -> words in all documents
def totalwords(allpredocs):
    total = []
    for i in range(len(allpredocs)):
        if i <= len(allpredocs):
            total = set(total).union(set(allpredocs[i]))
    return total


# createDict -> get the cleaned documents list and totalwords list
# return -> a dictionary that contains words and the number of times words are repeated in the text for all texts
def createDict(allpredocs, totalwords):
    wordDicts = []
    for allpredoc in allpredocs:
        wordDictdoc = dict.fromkeys(totalwords, 0)
        for word in allpredoc:
            wordDictdoc[word] += 1
        wordDicts.append(wordDictdoc)
    return wordDicts # her kelime kaç kere var diye sözlük döndürür.