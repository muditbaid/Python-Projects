import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def dict(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        print("Did you mean %s" %get_close_matches(word,data.keys())[0])
        decide = input("Enter y for yes and n for no: ")
        if decide == 'y':
            return data[get_close_matches(word,data.keys())[0]]
        elif decide == 'n':
            return "Word not found"
        else:
            return "You have entered the wrong word, please try again with 'y' or 'n' "
    else:
        return "Word not found"
word = input("Enter the word you want to search: ")

output=dict(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
