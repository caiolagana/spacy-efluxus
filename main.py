from flask import Flask, request, jsonify
import spacy
import pytesseract

#nlp = spacy.load("pt_core_news_sm")
#doc = nlp(sentences[0])
#print(doc.text)
#for token in doc:
#    print(token.text, token.pos_, token.dep_)

app = Flask(__name__)

@app.get("/")
def hello_world():
    return "Hello, World!!"

@app.post("/compute")
def res():
    input_json = request.get_json(force=True)
    print('data from client: ',input_json)
    dictToReturn = {'answer':42}
    return jsonify(dictToReturn)

#file = open("input-test.txt", "r")
#f = nlp(file.read())
#for token in f:
#    print(token.text, token.pos_, token.dep_)