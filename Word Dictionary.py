# have a python dictionary that has a key/value pair that represts a word and it's definition
# collect input from the user, input is a word 
# check if the word is in the dictionary 
# print the definition

# Using PyDictionary
from PyDictionary import PyDictionary

# Using PyDictionary & getMeanings or printMeanings 
dictionary = PyDictionary("eyes", "indentation", "head")

print(dictionary.getMeanings())


# dictionary = PyDictionary()

# while True:
#     word = input("Enter a word: ")
#     if word == "":
#         break
#     print(dictionary.meaning(word))


# Using local dictionary

# def main():
#     word_dictionary = {
#         'hi': 'a way of greeting',
#         'eye': 'an organ for seeing',
#         'earth': 'a planet in space',
#     }

#     while True:
#         word = input("Enter a word: ")
#         if word == "":
#             break
#         if word in word_dictionary:
#             print(word, ":", word_dictionary[word])

# main()


