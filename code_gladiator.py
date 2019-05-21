from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import json

chatbot = ChatBot(
    "code_gladiator",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
	},
	{
            'import_path': 'chatterbot.logic.TimeLogicAdapter'
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation'
        }
    ],
    filters=["filters.get_recent_repeated_responses",
    ],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter'
)

trainer1 = ChatterBotCorpusTrainer(chatbot)
trainer1.train("chatterbot.corpus.english")
data = json.loads(open('./faq.json').read())
for i in data:
    trainer2 = ListTrainer(chatbot)
    trainer2.train(i)
print('Chatbot Started:')

while True:
    try:
        bot_input = chatbot.get_response(input("human:"))
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break

