import telebot
from telebot import types
# import config
bot = telebot.TeleBot('7082220435:AAEc6t-bmqin14NClkLChaNpVdAA2Us6T-4')
@bot.message_handler(commands=['start'])  
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('Чего я умею ?!')
    btn1 = types.KeyboardButton('Связь с разработчиками')
    # btn1 = types.KeyboardButton('')
    # btn1 = types.KeyboardButton('')
    bot.send_message(message.chat.id, '<b>Привет,я ждал твоего сообщения</b>', parse_mode='html')
@bot.message_handler(content_types = ['text'])
def func(message):
    if(message.text == 'Чего я умею ?!'):
        bot.send_message(message.chat.id, text = 'И так,сейчас я тебе расскажу о том чего умею. /n Для начала сообщение мне стоит писать с маленькой буквы,за исключением особенных фраз...')
    elif(message.text == 'Связь с разработчиками'):
         bot.send_message(message.chat.id, text = 'аккаунт разработчика бота @s_milv')
bot.polling()