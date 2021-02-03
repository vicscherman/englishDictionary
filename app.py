import json
from difflib import get_close_matches


data = json.load(open("data.json"))



def search(word):
    #rendering input into lowercase
    word = word.lower()
    #if the input is found
    if word in data:
        return data[word]
    #if the word is in the dataset with a capital first letter eg "France"
    elif word.capitalize() in data:
        return data[word.capitalize()]
    #If the word is in the dataset in all caps like "NAFTA"
    elif word.upper() in data:
        return data[word.upper()]
    #If there are close matches to the word using the get_close_matches package, returns first close match. Accounts for incorrect user input (lowercase y, n, other strings)
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input(f"No match found for {word}. Did you mean {get_close_matches(word, data.keys())[0]} instead? Enter Y if yes, or N if no: " ).lower()
        if yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n":
            return f"Results for {word} not found."
        else:
            return "I didn't understand your entry."
    # if the word, and any similar words,  just doesn't exist in our dataset. Most typically for random strings
    else:
        return f" Results for {word} not found. Please double check your search input."
# Our search term prompt. Keeping it below to keep casing of input intact (function automatically turns input into lowercase)
word = input("Enter word: ")


output = (search(word))
# If the result is found in the list dataset
if type(output) == list:
    for item in output:
        #print index number +1 and the definition so it looks nice
        print(f"{output.index(item)+1}. ", item)
# If the result isn't found
else:
    print(output)