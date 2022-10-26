To setup the python environment:

python -m venv .env
source .env/bin/activate
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download pt_core_news_sm

To run the program:

turn on the server:
python webwait.py

run the client:
python client.py