import telebot
import os
from telebot import types

token = '5964464686:AAFFfIFzO4s5swOOA5eW9-rTJGI_XQlnGl0'

#cursor = connection.cursor()
#connection.commit()
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Monday_even")
    btn2 = types.KeyboardButton("Tuesday_even")
    btn3 = types.KeyboardButton("Wednesday_even")
    btn4 = types.KeyboardButton("Thursday_even")
    btn5 = types.KeyboardButton("Friday_even")
    btn6 = types.KeyboardButton("All_Week_even")
    btn7 = types.KeyboardButton("Switch_Week")
    btn8 = types.KeyboardButton("Help")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.chat.id,
                     text="Здравствуйте, {0.first_name}! Я умею выводить рассписание группы (BIN2201).".format(
                         message.from_user), reply_markup=markup)
    bot.send_message(message.chat.id,
                     text="Уважаемый {0.first_name}! Для более подробной информации о работе со мной пишите /help или же используйте плитки автоматических запросов!".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,
                     ' /Switch_Week_even - переключить неделю на четную \n /Switch_Week переключить неделю на нечетную \n /mtuci - Сайт университета \n Далее запросы выбираются спомощью плиток, что достаточно удобно. Если у вас пропали плитки просто свичните недели. Приятного пользования, также не забывайте проверять актуальность рассписания на сайте: https://mtuci.ru/')


@bot.message_handler(commands=['mtuci'])
def mtuci(message):
    bot.send_message(message.chat.id, 'Держите вашу ссылочку: https://mtuci.ru/')


@bot.message_handler(commands=['Switch_Week'])
def Switch_Week(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Monday")
    btn2 = types.KeyboardButton("Tuesday")
    btn3 = types.KeyboardButton("Wednesday")
    btn4 = types.KeyboardButton("Thursday")
    btn5 = types.KeyboardButton("Friday")
    btn6 = types.KeyboardButton("All_Week")
    btn7 = types.KeyboardButton("Switch_Week_even")
    btn8 = types.KeyboardButton("Help")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.chat.id, text="Уважаемый {0.first_name}! Вы переключили кнопки на нечетную неделю!".format(
        message.from_user), reply_markup=markup)


@bot.message_handler(commands=['Switch_Week_even'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Monday_even")
    btn2 = types.KeyboardButton("Tuesday_even")
    btn3 = types.KeyboardButton("Wednesday_even")
    btn4 = types.KeyboardButton("Thursday_even")
    btn5 = types.KeyboardButton("Friday_even")
    btn6 = types.KeyboardButton("All_Week_even")
    btn7 = types.KeyboardButton("Switch_Week")
    btn8 = types.KeyboardButton("Help")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.chat.id,
                     text="Уважаемый {0.first_name}! Вы переключили кнопки на четную неделю!".format(message.from_user),
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Switch_Week"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Monday")
        btn2 = types.KeyboardButton("Tuesday")
        btn3 = types.KeyboardButton("Wednesday")
        btn4 = types.KeyboardButton("Thursday")
        btn5 = types.KeyboardButton("Friday")
        btn6 = types.KeyboardButton("All_Week")
        btn7 = types.KeyboardButton("Switch_Week_even")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id,
                         text="Уважаемый {0.first_name}! Вы переключили кнопки на нечетную неделю!".format(
                             message.from_user), reply_markup=markup)

    elif (message.text == "Monday"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Monday")
        btn2 = types.KeyboardButton("Tuesday")
        btn3 = types.KeyboardButton("Wednesday")
        btn4 = types.KeyboardButton("Thursday")
        btn5 = types.KeyboardButton("Friday")
        btn6 = types.KeyboardButton("All_Week")
        btn7 = types.KeyboardButton("Switch_Week_even")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Нечетный Понидельник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Выш.математика(л) | Н-526 | 9:30 | Пискарев С.И \n ВВИТ(пр) | Н-324 | 11:20 | Колесников О.В. \n ВВИТ(пр) | Н-324 | 13:10 | Колесников О.В.),".format(
                             message.from_user), reply_markup=markup)

    elif (message.text == "Tuesday"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Monday")
        btn2 = types.KeyboardButton("Tuesday")
        btn3 = types.KeyboardButton("Wednesday")
        btn4 = types.KeyboardButton("Thursday")
        btn5 = types.KeyboardButton("Friday")
        btn6 = types.KeyboardButton("All_Week")
        btn7 = types.KeyboardButton("Switch_Week_even")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Нечетный Вторник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Выш.математика(пр) | Н-526 | 9:30 | Пискарев С.И \n Физкультура(пр) | Н-С/Зал-2 | 11:20 | Волохова С.В. \n Иностранный язык(пр) | Н-420 | 13:10 | Мальцева С.Н.".format(
                             message.from_user), reply_markup=markup)
    elif (message.text == "Wednesday"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Monday")
        btn2 = types.KeyboardButton("Tuesday")
        btn3 = types.KeyboardButton("Wednesday")
        btn4 = types.KeyboardButton("Thursday")
        btn5 = types.KeyboardButton("Friday")
        btn6 = types.KeyboardButton("All_Week")
        btn7 = types.KeyboardButton("Switch_Week_even")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Нечетная Среда".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Русский язык(пр) | Н-310 | 13:10 | Горшкова Д.И. \n Физика(л) | Н-347 | 15:25 | Карпов И.А.\n  ".format(
                             message.from_user), reply_markup=markup)

    elif (message.text == "Thursday"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Monday")
        btn2 = types.KeyboardButton("Tuesday")
        btn3 = types.KeyboardButton("Wednesday")
        btn4 = types.KeyboardButton("Thursday")
        btn5 = types.KeyboardButton("Friday")
        btn6 = types.KeyboardButton("All_Week")
        btn7 = types.KeyboardButton("Switch_Week_even")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Нечетная Четверг".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Русский язык(л) | Н-514 | 11:20 | Горшкова Д.И. \n История(пр) | Н-424 | 13:10 | Скляр Л.Н. \n  ".format(
                             message.from_user), reply_markup=markup)

    elif (message.text == "Friday"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Monday")
        btn2 = types.KeyboardButton("Tuesday")
        btn3 = types.KeyboardButton("Wednesday")
        btn4 = types.KeyboardButton("Thursday")
        btn5 = types.KeyboardButton("Friday")
        btn6 = types.KeyboardButton("All_Week")
        btn7 = types.KeyboardButton("Switch_Week_even")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Нечетная Пятница".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Физика(лаб) | Н-342 | 9:30 | Тимошина М.И.\n 'Физкультура(пр) | Н-С/Зал-2 | 11:20 | Волохова С.В. \n  ".format(
                             message.from_user), reply_markup=markup)

    elif (message.text == "All_Week"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Monday")
        btn2 = types.KeyboardButton("Tuesday")
        btn3 = types.KeyboardButton("Wednesday")
        btn4 = types.KeyboardButton("Thursday")
        btn5 = types.KeyboardButton("Friday")
        btn6 = types.KeyboardButton("All_Week")
        btn7 = types.KeyboardButton("Switch_Week_even")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Нечетный Понидельник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Выш.математика(л) | Н-526 | 9:30 | Пискарев С.И \n ВВИТ(пр) | Н-324 | 11:20 | Колесников О.В. \n ВВИТ(пр) | Н-324 | 13:10 | Колесников О.В.),".format(
                             message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Нечетный Вторник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Выш.математика(пр) | Н-526 | 9:30 | Пискарев С.И \n Физкультура(пр) | Н-С/Зал-2 | 11:20 \n Иностранный язык(пр) | Н-420 | 13:10 ".format(
                             message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Нечетная Среда".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Русский язык(пр) | Н-310 | 13:10 | Горшкова Д.И. \n Физика(л) | Н-347 | 15:25 | Карпов И.А.\n  ".format(
                             message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Нечетная Четверг".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Русский язык(л) | Н-514 | 11:20 | Горшкова Д.И. \n История(пр) | Н-424 | 13:10 | Скляр Л.Н. \n  ".format(
                             message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Нечетная Пятница".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Физика(лаб) | Н-342 | 9:30 | Тимошина М.И.\n 'Физкультура(пр) | Н-С/Зал-2 | 11:20 | Волохова С.В. \n  ".format(
                             message.from_user), reply_markup=markup)

    elif (message.text == "Help"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Monday")
        btn2 = types.KeyboardButton("Tuesday")
        btn3 = types.KeyboardButton("Wednesday")
        btn4 = types.KeyboardButton("Thursday")
        btn5 = types.KeyboardButton("Friday")
        btn6 = types.KeyboardButton("All_Week")
        btn7 = types.KeyboardButton("Switch_Week_even")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Ок".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         ' /Switch_Week_even - переключить неделю на четную \n /Switch_Week переключить неделю на нечетную \n /mtuci - Сайт университета \n Далее запросы выбираются спомощью плиток, что достаточно удобно. Если у вас пропали плитки просто свичните недели. Приятного пользования, также не забывайте проверять актуальность рассписания на сайте: https://mtuci.ru/')


    elif (message.text == "Monday_even"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Monday")
        btn2 = types.KeyboardButton("Tuesday")
        btn3 = types.KeyboardButton("Wednesday")
        btn4 = types.KeyboardButton("Thursday")
        btn5 = types.KeyboardButton("Friday")
        btn6 = types.KeyboardButton("All_Week")
        btn7 = types.KeyboardButton("Switch_Week_even")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Четный Понидельник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                         text="Предмет | Кабинет | Время | Преподаватель \n Физика(л) | Н-226 | 9:30 | Карпов И.А. \n Выш.математика(л) | Н-514 | 11:20 | Пискарев С.И \n Иностранный язык(пр) | Н-328 | 13:10 | Мальцева С.Н. \n История(пр) | Н-401 | 15:25 | Скляр Л.Н.".format(
                             message.from_user), reply_markup=markup)

    elif (message.text == "Wednesday_even"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Monday")
        btn2 = types.KeyboardButton("Tuesday")
        btn3 = types.KeyboardButton("Wednesday")
        btn4 = types.KeyboardButton("Thursday")
        btn5 = types.KeyboardButton("Friday")
        btn6 = types.KeyboardButton("All_Week")
        btn7 = types.KeyboardButton("Switch_Week_even")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Четная Среда".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n ВВИТ(пр) | H-515 | 9:30 \n Физика(пр) | Н-515 | 11:20 | Колесников О.В. \n ВВИТ(пр) | А-222 | 13:10 | Колесников О.В.),".format( message.from_user), reply_markup=markup)

    elif (message.text == "Tuesday_even"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Monday")
        btn2 = types.KeyboardButton("Tuesday")
        btn3 = types.KeyboardButton("Wednesday")
        btn4 = types.KeyboardButton("Thursday")
        btn5 = types.KeyboardButton("Friday")
        btn6 = types.KeyboardButton("All_Week")
        btn7 = types.KeyboardButton("Switch_Week_even")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Четный Вторник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                 text="Предмет | Кабинет | Время | Преподаватель \n Выш.математика(пр) | Н-515 | 9:30 | Пискарев С.И \n Физкультура(пр) | Н-С/Зал-2 | 11:20 | Волохова С.В. \n ВВИТ(лаб) | Н-515 | 13:10 | Воронкова М.Н.".format(
                     message.from_user), reply_markup=markup)

    elif (message.text == "Thursday_even"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Monday")
        btn2 = types.KeyboardButton("Tuesday")
        btn3 = types.KeyboardButton("Wednesday")
        btn4 = types.KeyboardButton("Thursday")
        btn5 = types.KeyboardButton("Friday")
        btn6 = types.KeyboardButton("All_Week")
        btn7 = types.KeyboardButton("Switch_Week_even")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Четный Четверг".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                 text="Предмет | Кабинет | Время | Преподаватель \n Физика(пр) | Н-515 | 11:20 | Оборотов В.А. \n 'Физкультура(пр) | Н-С/Зал-2 | 13:10 | Волохова С.В. \n История(Л) | Н-526 | 15:25 | Скляр Л.Н.".format(
                     message.from_user), reply_markup=markup)

    elif (message.text == "Friday_even"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Monday")
        btn2 = types.KeyboardButton("Tuesday")
        btn3 = types.KeyboardButton("Wednesday")
        btn4 = types.KeyboardButton("Thursday")
        btn5 = types.KeyboardButton("Friday")
        btn6 = types.KeyboardButton("All_Week")
        btn7 = types.KeyboardButton("Switch_Week_even")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Четная Пятница".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Нет пар".format(message.from_user),
                 reply_markup=markup)

    elif (message.text == "All_Week_even"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Monday")
        btn2 = types.KeyboardButton("Tuesday")
        btn3 = types.KeyboardButton("Wednesday")
        btn4 = types.KeyboardButton("Thursday")
        btn5 = types.KeyboardButton("Friday")
        btn6 = types.KeyboardButton("All_Week")
        btn7 = types.KeyboardButton("Switch_Week_even")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="Нечетный Понидельник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                 text="Предмет | Кабинет | Время | Преподаватель \n Физика(л) | Н-226 | 9:30 | Карпов И.А. \n Выш.математика(л) | Н-514 | 11:20 | Пискарев С.И \n Иностранный язык(пр) | Н-328 | 13:10 | Мальцева С.Н. \n История(пр) | Н-401 | 15:25 | Скляр Л.Н.".format(
                     message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Четный Вторник".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                 text="Предмет | Кабинет | Время | Преподаватель \n Выш.математика(пр) | Н-515 | 9:30 | Пискарев С.И \n Физкультура(пр) | Н-С/Зал-2 | 11:20 | Волохова С.В. \n ВВИТ(лаб) | Н-515 | 13:10 | Воронкова М.Н.".format(
                     message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Четная Среда".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                 text="Предмет | Кабинет | Время | Преподаватель \n ВВИТ(пр) | H-515 | 9:30 \n Физика(пр) | Н-515 | 11:20 | Колесников О.В. \n ВВИТ(пр) | А-222 | 13:10 | Колесников О.В.),".format(
                     message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Четный Четверг".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id,
                 text="Предмет | Кабинет | Время | Преподаватель \n Физика(пр) | Н-515 | 11:20 | Оборотов В.А. \n 'Физкультура(пр) | Н-С/Зал-2 | 13:10 | Волохова С.В. \n История(Л) | Н-526 | 15:25 | Скляр Л.Н.".format(
                     message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Четная Пятница".format(message.from_user), reply_markup=markup)
        bot.send_message(message.chat.id, text="Предмет | Кабинет | Время | Преподаватель \n Нет пар".format(message.from_user),
                 reply_markup=markup)

    elif (message.text == "Switch_Week_even"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Monday_even")
        btn2 = types.KeyboardButton("Tuesday_even")
        btn3 = types.KeyboardButton("Wednesday_even")
        btn4 = types.KeyboardButton("Thursday_even")
        btn5 = types.KeyboardButton("Friday_even")
        btn6 = types.KeyboardButton("All_Week_even")
        btn7 = types.KeyboardButton("Switch_Week")
        btn8 = types.KeyboardButton("Help")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id,
                 text="Уважаемый {0.first_name}! Вы переключили кнопки на четную неделю!".format(message.from_user),
                 reply_markup=markup)

    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")




bot.infinity_polling()