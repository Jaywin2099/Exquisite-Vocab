import requests

minWordLength = 7

def getWord(): 
    w = requests.get('https://random-word-api.herokuapp.com/word').json()[0]
    return w

# makes sure the word is greater than {minWordLength} characters
contents = getWord()
while (len(contents) < minWordLength):
    contents = getWord()

req = 'https://dictionaryapi.com/api/v3/references/collegiate/json/{}?key=ac74c3d7-59de-45da-b65b-a5d552901721'.format(contents)

merriamJSON = requests.get(req).json()

shortDefs = merriamJSON[0]['shortdef']

for i in shortDefs:
    contents += '\n' + i 

# writes word and other info to file
wordFile = open('word.txt', 'w')
wordFile.write(contents)
wordFile.close()

if __name__ == '__main__':
    print(contents)