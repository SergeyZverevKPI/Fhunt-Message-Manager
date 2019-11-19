print('Hello, world')
import telebot
import config
bot = telebot.TeleBot(config.token)
admin_id = 397330072
@bot.message_handler(content_types = ['text'])
def echo(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, message.from_user.id)
    elif message.text == '/info':
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text = 'Ссылка на fhunt', url = 'https://freelancehunt.com/freelancer/Sergey_KPI.html')
        keyboard.add(url_button)
        bot.send_message(message.chat.id,'Нажмите кнопку',reply_markup = keyboard)
    else:
        bot.send_message(admin_id,message.json['text'])

bot.polling(none_stop = True)
