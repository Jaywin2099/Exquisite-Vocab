#a chat bot made the code that took me a day to make in 5 minutes with a little pushing
import requests
import json

# Set the API endpoint URL
url = "https://random-word-api.herokuapp.com/word?number=1"

# Send a GET request to the API
response = requests.get(url)

# Extract the word from the response
random_word = response.json()[0]

# Set the API endpoint URL
url = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/" + random_word

# Set your API key
api_key = "ac74c3d7-59de-45da-b65b-a5d552901721"

# Make the API request
response = requests.get(url, params={"key": api_key})

# Parse the JSON response
try:
    data = json.loads(response.text)[0]["shortdef"]
except:
    data = json.loads(response.text)

print(f"The definition of '{random_word}' is", end=' ')

for i in data:
    print(i, end=', ')