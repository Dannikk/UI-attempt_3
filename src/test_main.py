from .main import *
import os

def test_snoop_says():
    file_name = "test_resources.txt"
    print(os.path)
    for n in range(10, 30):
        assert len(snoop_says(file_name, n).replace("\n", "").split()) == n

def test_markov_chain():
    file_name = "test_resources.txt"
    for n in range(10, 30):
        with io.open(file_name, "r", encoding='utf-8') as file:
            language = words(file)
        matrix = transition_matrix(language)
        sentence = markov_chain(language, matrix, n)
        assert type(sentence) == str and len(snoop_says(file_name, n).replace("\n", "").split()) == n