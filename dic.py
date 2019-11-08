import json
import os
from difflib import get_close_matches

sourceFilePath = 'files/data.json'

def translate(sourceFilePath, keyword):

    if os.path.exists(sourceFilePath):
        data = json.load (open(sourceFilePath))
        #allow case insensitive search in dictionary
        keyword = keyword.lower()
        #first, we search for a perfect match of the word
        #second, we try to find closest match in dictionary - first element of the get_close_matches(word, list) using difflib library
        if keyword in data.keys():
            return data[keyword]
        elif len(get_close_matches(keyword, data.keys()))>0:
            #return 'Did you mean %s instead' %get_close_matches(keyword, data.keys())[0]   
            closest = get_close_matches(keyword, data.keys())[0]
            wantClosestMatch = input ('Did you mean \'{}\' instead ? Press Y for Yes and N for no: '.format(closest))
            if wantClosestMatch.upper() == 'Y':
                return data[closest]
            elif wantClosestMatch.upper() == 'N':
                return 'The word doesn\'t exist. Please double check it'
            else:
                return 'We didn\'t understand your entry'
        else:
            return "The word doesn't exist. Please double check it"
    else:
        return ('Dictionary File not found ')


word = input ('Enter word: ')     
print('Searching for \'{}\' in dictionary \'{}\' ...\n'.format(word, sourceFilePath))
result = translate(sourceFilePath, word)
if isinstance(result, list):
    for item in result:
        print(item)
else:
    print(result)
