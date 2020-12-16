import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif get_close_matches(word, data.keys())[0]:
        w = get_close_matches(word, data.keys())[0]
        print("Did you mean {} instead of  {}?".format(w, word))
        ch = input("Please choose yes or no Y/N:").lower()
        try:
            if ch == "y":
                return data[w]
            else:
                return "Sorry the word you are finding is not in dictionary."
        except IndexError:
            return "The word doesn't exist.Please double check!"


word = input("Enter a word:")

output = translate(word)

for x in output:
    print(x)
