from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3


chatbot = ChatBot('Tiago')
conversation = [
                'Olá',
                 'Oi',
                'Boa noite',
                'Com licença',
                'Prazer em conhecê-lo',
                'Qual é o seu nome?',
                'Meu nome é Tiago',
                'Como você está?',
                'Eu estou bem',
                'Tudo ótimo',
                'Bom dia',
                'Boa tarde',
                'Muito bem, obrigado',
                'Até breve',
                'Adeus',
                'O que você gosta de fazer?',
                'Eu gosto de programar'
                ]
trainer = ListTrainer(chatbot)
trainer.train(conversation)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 125)


def setup():
    for voice in voices:
        if voice.name == 'brazil':
            engine.setProperty('voice', voice.id)


def speak(test):
    setup()
    engine.say(test)
    engine.runAndWait()


while True:
    question = input("Usuário: ")
    response = chatbot.get_response(question)
    if float(response.confidence) > 0.2:
        speak(response)
        print('bot', response)
    else:
        speak('Ainda não sei responder esta pergunta')
        print('Ainda não sei responder esta pergunta')


#while True:
 #   text = str(input("Digite o seu texto: "))

  #  if text not in ('sair', 'Sair'):
   #     speak(text)
    #else:
     #   speak('Adeus')
      #  break