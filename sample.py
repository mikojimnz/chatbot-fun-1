from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Knightro')

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

while True:
    request = input("You: ")
    response = chatbot.get_response(request)
    print("Bot: {}".format(response))

print(response)
