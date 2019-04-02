from subprocess import check_output
import telebot
from telebot import types #Добавляем импорт кнопок
import time

bot = telebot.TeleBot("XXXXXXXXX:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")#Bot's token
user_id = 0 #your accaunt's id
@bot.message_handler(content_types=["text"])
def main(message):
   if (user_id == message.chat.id): #проверяем, что пишет именно владелец
      comand = message.text  #текст сообщения
      markup = types.InlineKeyboardMarkup() #создаем клавиатуру
      button = types.InlineKeyboardButton(text="Повторить", callback_data=comand) #создаем кнопку
      markup.add(button) #добавляем кнопку в клавиатуру
      try: #если команда невыполняемая - check_output выдаст exception
         bot.send_message(user_id, check_output(comand, shell = True,  reply_markup = markup)) #вызываем команду и отправляем сообщение с результатом
      except:
         bot.send_message(user_id, "Invalid input") #если команда некорректна

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
  comand = call.data #считываем команду из поля кнопки data
  try:#если команда не выполняемая - check_output выдаст exception
     markup = types.InlineKeyboardMarkup() #создаем клавиатуру
     button = types.InlineKeyboardButton(text="Повторить", callback_data=comand) #создаем кнопку и в data передаём команду
     markup.add(button) #добавляем кнопку в клавиатуру
     bot.send_message(user_id, check_output(comand, shell = True), reply_markup = markup) #вызываем команду и отправляем сообщение с результатом
  except:
     bot.send_message(user_id, "Invalid input") #если команда некорректна

if __name__ == '__main__':
    while True:
        try:#добавляем try для бесперебойной работы
            bot.polling(none_stop=True)#запуск бота
        except:
            time.sleep(10)#в случае падения
