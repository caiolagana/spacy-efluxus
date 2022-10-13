import spacy
from spacy.lang.pt.examples import sentences
nlp = spacy.load("pt_core_news_sm")
doc = nlp(sentences[0])
print(doc.text)
for token in doc:
    print(token.text, token.pos_, token.dep_)


file = open("input-test.txt", "r")
f = nlp(file.read())
for token in f:
    print(token.text, token.pos_, token.dep_)
