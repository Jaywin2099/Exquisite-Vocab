import requests

# Set the API endpoint
endpoint = "https://random-word-api.herokuapp.com/word?number=1"

# Make the API request
response = requests.get(endpoint)

# Parse the response as JSON
response_json = response.json()

# Extract the word from the response
word = response_json[0]

# Set the API endpoint
endpoint = "http://api.wordnik.com/v4/word.json/{word}/definitions"

# Make the API request
response = requests.get(endpoint.format(word=word))

# Parse the response as JSON
response_json = response.json()

# Extract the first definition from the response
definition = response_json

# Print the definition
print(definition)