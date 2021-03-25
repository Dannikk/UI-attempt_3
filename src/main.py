import io
import random


def words(file) -> list:
    lang = []
    try:
        for line in file:
            lang.extend(line.split())
    except Exception as e:
        print(e)
    return lang


def transition_matrix(tokens: list) -> dict:
    matrix = {}
    for i in range(len(tokens) - 2):
        if (tokens[i], tokens[i + 1]) in matrix:
            # print((tokens[i], tokens[i + 1]))
            matrix[tokens[i], tokens[i + 1]].add(tokens[i + 2])
        else:
            matrix[tokens[i], tokens[i + 1]] = {tokens[i + 2]}
    return matrix


def markov_chain(tokens: list, tr_matrix: dict, length: int) -> str:
    sentence = []
    a = random.choice(tokens)
    b = random.choice(tokens)
    sentence.append(a)
    sentence.append(b)
    for i in range(length - 2):
        if (a, b) in tr_matrix:
            # print(tr_matrix[a, b])
            a, b = b, random.choice(list(tr_matrix[a, b]))
            sentence.append(b)
        else:
            a, b = b, random.choice(tokens)
            sentence.append(b)

    return " ".join(sentence)


def snoop_says(file_name: str, sent_len: int) -> str:
    with io.open(file_name, "r", encoding='utf-8') as file:
        language = words(file)

    matrix = transition_matrix(language)
    sentence = markov_chain(language, matrix, sent_len)
    # print(len(sentence.split(" ")))
    return sentence


# m = transition_matrix(["a", "b", "c", "dfdrfsa", "srvs"])
# print(m)
if __name__ == '__main__':
    file_name = "../snoop279.txt"
    for n in range(10, 25):
        print(len(snoop_says(file_name, n).replace("\n", "").split()) == n)
