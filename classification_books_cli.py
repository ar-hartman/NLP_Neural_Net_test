import openai
import config
import json
import sys
import time





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


def callGPT(engine, inputString, max_tokens):
    if engine == '--davinci':
        gptEngine = 'davinci'
    elif engine == '--curie':
        gptEngine = 'curie'
    elif engine == '--babbage':
        gptEngine = 'babbage'
    elif engine == '--ada':
        gptEngine = 'ada'

    response = openai.Completion.create(engine=gptEngine, prompt=inputString, max_tokens=max_tokens, temperature=0)
    responseString = response['choices'][0]['text']
    print(responseString + "\n")

def main():
    script = sys.argv[0]
    engine = sys.argv[1]
    max_tokens = int(sys.argv[2])
    assert engine in ['--davinci', '--curie', '--babbage', '--ada'], \
        'Engine is not one of --davinci, --curie, --babbage, --ada: ' + engine
    #exits the program
    print("User provided the following engine: " + engine + "\n\n")


    prompt = input("What would you like to ask GPT-3? Enter 'quit' to exit program.\n")

    while prompt != 'quit':
        callGPT(engine, prompt, max_tokens)
        prompt = input("Ask a question. OR Enter 'quit' to exit program.\n")




    print('exiting the program.')
    sys.exit()



    



if __name__ == "__main__":
    main()