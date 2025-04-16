from difflib import get_close_matches

import json5

data = json5.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return  data[word]
    elif word.title() in data:
        return  data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) >0:
        print("Did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("Press y for yes or n for no")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return("Pugger your own steps on wrong keys.")
        else:
            return("You have entered wrong input. Please enter just y or n")
    else:
        print("Pugger your own steps on wrong keys.")

word = input("Enter the word you want to search: \n")
output = translate(word)
print(output)

