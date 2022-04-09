from flask import Flask, render_template, request
from chatterbot import ChatBot

from chatterbot.trainers import ListTrainer

app = Flask(__name__,template_folder='template')

chatbot = ChatBot('ChatBot')
trainer = ListTrainer(chatbot)
trainer.train([
'Hi',
'Hello',
'I need your assistance regarding my order',
'Please, Provide me with your order id',
'I have a complaint.',
'Please elaborate, your concern',
'How long it will take to receive an order ?',
'An order takes 3-5 Business days to get delivered.',
'Okay Thanks'])


@app.route("/")
def home():
    return render_template("T@S home.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    app.run()