import openai
import config
import json

openai.api_key = config.api_key

#response = openai.Completion.create(engine="davinci", prompt="This is a test", max_tokens=3)

#print(response)



##good at: complex intent, cause and effect, summarization for audience
#openai.Completion.create(engine="davinci")

##good at: language translation, complex classification, text sentiment, summarization
#openai.Completion.create(engine="curie")

##good at: moderate classification, semantic search classification
#openai.Completion.create(engine="babbage")

##good at: parsing text, simple classification, address correction, keywords
#openai.Completion.create(engine="ada")


primerString = """
    \"Animal Farm": {
        "Author": "George Orwell",
        "Genre": "Speculative fiction"
    },
    "A Clockwork Orange": {
        "Author": "Anthony Burgess",
        "Genre": "Science Fiction"
    },
    "The Plague": {
        "Author": "Albert Camus",
        "Genre": "Existentialism"
    },
    "A Fire Upon the Deep": {
        "Author": "Vernor Vinge",
        "Genre": "Science Fiction"
    },
    "A Wizard of Earthsea": {
        "Author": "Ursula K. Le Guin",
        "Genre": "Children's literature"
    },"""

#prmpt = """\"Children of Dune": {
#        "Author":"""

#prmpt = """\"The Old Man and the Sea": {
#        "Author":"""

prmpt = """\"1984": {
        "Author":"""

groundTruth = {
    "Author": "Frank Herbert",
    "Genre": "Science Fiction"
}


inputString = primerString + prmpt

print("Testing - Classification: \n")
print("""Description - Provide a list of books with accompanying authors and 
    genres to primer the system. Provide the system with the next title with the 
    expectation that the system will return the correct author and genre. \n""")

print('Engine: Davinci \n')

print("Input String: \n" + inputString)

print("\n Output: \n")

response = openai.Completion.create(engine="davinci", prompt=inputString, max_tokens=100, temperature=0, best_of=3)


#print (response)

responseString = prmpt + response['choices'][0]['text']

print(responseString + "\n")
