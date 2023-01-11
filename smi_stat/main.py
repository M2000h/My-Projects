from asyncio import set_event_loop, get_event_loop
from telethon import TelegramClient
from wordcloud import WordCloud
from string import digits
import numpy as np
import pymorphy3
import telebot
import re

stop_list = {
    'мочь', 'делать', 'хорошо', 'пос', 'никак', 'ведь', 'у', 'для', 'ну', 'мы', 'три', 'н', 'к', 'тогда', 'сделать',
    'нет', 'сразу', 'ничего', 'опять', 'wall', 'значит', 'этот', 'весь', 'кстати', 'бы', 'так', 'под', 'особенно',
    'очень', 'да', 'при', 'менее', 'какой', 'кроме', 'любой', 'вообще', 'до', 'что', 'хороший', 'п', 'нужно',
    'второй', 'вполне', 'прямо', 'через', 'далее', 'много', 'или', 'поскольку', 'про', 'хоть', 'даже', 'там',
    'вдруг', 'оно', 'также', 'никакой', 'есть', 'раз', 'нибыть', 'нельзя', 'вместе', 'м', 'между', 'не', 'давно',
    'надо', 'сколько', 'наверное', 'за', 'такой', 'после', 'ранний', 'именно', 'несколько', 'то', 'никогда',
    'здесь', 'общий', 'они', 'сейчас', 'ни', 'примерно', 'если', 'скоро', 'мой', 'лишь', 'либо', 'куда', 'в',
    'новый', 'можно', 'вы', 'который', 'впрочем', 'таки', 'наш', 'являться', 'её', 'казаться', 'почему', 'о',
    'пример', 'пока', 'никто', 'равно', 'поэтому', 'без', 'на', 'она', 'быстро', 'тоже', 'точно', 'немного', 'он',
    'всё', 'я', 'быть', 'пусть', 'ли', 'ради', 'вот', 'снова', 'кто', 'конечно', 'свой', 'один', 'лично', 'теперь',
    'ещё', 'разве', 'уж', 'мало', 'некоторый', 'иначе', 'совсем', 'когда', 'по', 'это', 'хотя', 'почти', 'потом',
    'широта', 'ты', 'два', 'от', 'однако', 'тип', 'из', 'далёкий', 'й', 'прийтись', 'большой', 'просто', 'а', 'тут',
    'знать', 'совершенно', 'но', 'чем', 'уже', 'потому', 'и', 'всегда', 'тот', 'ранее', 'себя', 'где', 'только',
    'более', 'другой', 'же', 'перед', 'чтобы', 'как', 'сам', 'с', 'тем', 'возможно', 'над', 'самый', 'хотеть',
    'человек', 'сегодня', 'стать', 'работа', 'каждый', 'ваш', 'видео', 'первый', 'год', 'твой', 'чтоб'}

HELP_TEXT = """
Привет! Я строю облако слов, для телеграмм каналов.
Чтобы я построил облако, канал должен быть:
▫️ на русском языке
▫️ публичным
▫️ иметь в себе текстовые посты содержащие больше 100 символов

Просто отправь мне ссылку на канал в любом формате из трех:
▫️ https://t.me/durov_russia
▫️ @durov_russia
▫️ durov_russia
"""

bot = telebot.TeleBot("0000000:XXXXXXXXXXXXXXXXXXXX")
api_id = 123456
api_hash = 'xxxxxxxx'
client = TelegramClient('new_session', api_id, api_hash)
client.start()
morph = pymorphy3.MorphAnalyzer()

loop = get_event_loop()
set_event_loop(loop)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, HELP_TEXT, disable_web_page_preview=True)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(message.text, message.from_user)
    bot.reply_to(message, "Принял, секундочку...")
    try:
        messages = loop.run_until_complete(client.get_messages(message.text, limit=1000))
    except ValueError:
        bot.reply_to(message, "Кажется, такого канала не существует:(\n"
                              "Убедитесь, что ссылка соответствует условиям\n"
                              "/help")
        return
    sum_text = " "
    for m in messages:
        if m.fwd_from is None and m.message is not None:
            if len(m.message) > 100:
                sum_text += m.message + " "
    sum_text = sum_text.lower()
    sum_text = sum_text.translate(str.maketrans('', '', digits))
    sum_text = re.sub(r'[a-z]+', '', sum_text)
    sum_text = re.sub(r'[A-Z]+', '', sum_text)
    sum_text = sum_text.replace(",", " ")
    sum_text = sum_text.replace(".", " ")
    sum_text = sum_text.replace(";", " ")
    sum_text = sum_text.replace("\n", " ")
    sum_text = sum_text.replace(":", " ")
    sum_text = sum_text.replace("?", " ")
    sum_text = sum_text.replace('"', " ")
    sum_text = sum_text.replace("(", " ")
    sum_text = sum_text.replace(")", " ")
    sum_text = sum_text.replace("/", " ")
    sum_text = sum_text.replace("!", " ")
    sum_text = sum_text.replace("_", " ")
    sum_text = sum_text.replace("-", " ")
    res_text = ""
    for word in sum_text.split():
        w = morph.parse(word)[0].normal_form
        if w not in stop_list:
            res_text += w + " "
    x, y = np.ogrid[:900, :900]

    mask = (x - 450) ** 2 + (y - 450) ** 2 > 390 ** 2
    mask = 255 * mask.astype(int)
    wc = WordCloud(background_color="white", repeat=True, mask=mask)
    try:
        wc.generate(res_text)
    except ValueError as e:
        bot.reply_to(message, "Упс, кажется что-то пошло не так:(\n"
                              "Убедитесь, что ссылка соответствует условиям\n"
                              "/help")
        return
    bot.send_photo(message.from_user.id, wc.to_image(), caption=message.text)


if __name__ == "__main__":
    bot.infinity_polling()
