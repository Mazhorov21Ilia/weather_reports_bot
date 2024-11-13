from telebot import TeleBot
import json

token = "7891467095:AAERGih85-8a7QbJ5gqaXerbDtamkGpaGlI"

bot = TeleBot(token=token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Напиши дату в ближайшие 14 дней в формате гггг-мм-дд")

def search_weather(date):
	with open('forecast.json', 'r') as file:
		data = json.load(file)
		for i in data["forecast"]["forecastday"]:
			if date == i["date"]:
				return f"Что будет ночью: {i["astro"]}"
			# print(f"{i["date"]} - {i["day"]["condition"]["text"]}")

@bot.message_handler()
def zaglushka(message):
	text = message.text
	print(text)
	res = search_weather(text)
	bot.send_message(message.chat.id, res)
	
	



bot.infinity_polling()
