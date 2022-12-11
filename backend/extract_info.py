# this file will have as function which will be used for extracting the information
# each link will be passed in as a separate doc object
from lib2to3.pgen2.tokenize import TokenError
import spacy
from spacy.tokenizer import Tokenizer

def prepare_data():    
    nlp = spacy.load("en_core_web_sm")

    with open('citations.txt') as f:
        text = f.read()

    doc = nlp(text)
    # split the raw text into individual sentences
    
    #convert doc.sents to a list
    sentList = list(doc.sents)
    # use pos tagging on each of the sentences
    print(tokenList[0])
prepare_data()


# this function matches the keyword and searches for information based on it
def matchKeywords():
    # take the keyword as it is
    # and get the source of the word as well
    # create matching patterns
    pass
