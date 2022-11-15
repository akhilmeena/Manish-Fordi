import os
from flask import Flask,render_template,request,redirect
import telebot



TOKEN = '2109918986:AAErVJ9F_cne-cujIGG6VOZjw5GMNwr7UUA'
bot = telebot.TeleBot(TOKEN)
app=Flask(__name__)
#server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

#route() decorators
@app.route('/h')
def home():
    return "okay"

if __name__=='__main__':
  server.run(debug=True,host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
  #app.run(debug=True)
