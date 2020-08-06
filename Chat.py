from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')

chatbot.set_trainer(ListTrainer)


chatbot.train([
   'oi',
    'ola',
    'tudo bem com vc?',
    'estou bem, e vc?'
])

while True:

    # Get a response to the input text 'I would like to book a flight.'
    response = chatbot.get_response(input('Você: '))

    print('Chat:',response)