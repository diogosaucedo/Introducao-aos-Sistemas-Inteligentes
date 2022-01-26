"""
3) Faça uma função que receba uma string como parâmetro e retorne quantas palavras há na string.
"""

sample_sentence = "Noivinha do Aristides."


def count_words(sentence):
    return len(sentence.split(" "))


print("Amount of words: ", str(count_words(sample_sentence)))
