import telebot
import json

phonebook = {
    "Иванов": [4561234],
    "Петров": [4789123, 4123456],
    "Сидоров": [4895775, 4358825],
    "Семенова": [4789654, 4120354, 4857544]
}


def add_or_change_contact(lastname, number):
    global phonebook
    phonebook[lastname] = []
    phonebook[lastname].append(number)
    return phonebook


def save():
    with open("phone_book.json", "w", encoding="utf-8") as p_b:
        global phonebook
        p_b.write(json.dumps(phonebook, ensure_ascii=False))


def load():
    global phonebook
    with open("phone_book.json", "r", encoding="utf-8") as p_b:
        phonebook = json.load(p_b)


def print_items(data):
    for para in data.items():
        return para[0], para[1]
    

def send_contact(data):
    strings = []
    for key,item in data.items():
        strings.append("{}: {}".format(key.capitalize(), item))
    result = "; ".join(strings)
    return result


API_TOKEN = "Ругается гит"

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message):
    load()
    bot.send_message(message.chat.id, "Контакты загружены")


@bot.message_handler(commands=["add"])
def add_message(message):
    lastname = message.text
    telefon = lastname.split(" ")
    add_or_change_contact(str(telefon[1]), str(telefon[2]))
    save()
    bot.send_message(message.chat.id, "Контакт добавлен")


@bot.message_handler(commands=["all"])
def show_all(message):
    bot.send_message(message.chat.id, "Вот весь список контактов:")
    bot.send_message(message.chat.id, send_contact(phonebook))


print("Server start")
bot.polling()
