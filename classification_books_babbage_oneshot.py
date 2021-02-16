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



primerString1 = "Q: "
primerString = " - Who is the author and what is the genre? \nA:"

#prmpt = "Children of Dune"

#prmpt = "The Old Man and the Sea"

prmpt = "1984"



inputString = primerString1 + prmpt + primerString

print("Testing - Classification: \n")
print("""Description - One-shot Question and Answer Provide the system with book title with the 
    expectation that the system will return the correct author and genre. \n""")

print('Engine: Ada \n')

print("Input String: \n" + inputString)

print("\n Output: \n")

response = openai.Completion.create(engine="babbage", prompt=inputString, max_tokens=30, temperature=0, best_of=5)


#print (response)

responseString = prmpt + ": " + response['choices'][0]['text']

print(responseString + "\n")
