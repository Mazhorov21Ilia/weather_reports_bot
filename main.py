from telebot import TeleBot
import json

token = "7891467095:AAERGih85-8a7QbJ5gqaXerbDtamkGpaGlI"
bot = TeleBot(token=token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Напишите дату в ближайшие 14 дней в формате гггг-мм-дд")

def search_weather(date):
	with open('forecast.json', 'r') as file:
		data = json.load(file)
		for i in data["forecast"]["forecastday"]:
			if date == i["date"]:
				return f"Погода в Москве {i["date"]} {i["day"]["condition"]["text"]}:\nТемпература {i["day"]["avgtemp_c"]}C\nШанс дождя {i["day"]["daily_chance_of_rain"]}%\nШанс снега {i["day"]["daily_chance_of_snow"]}%"
			# print(f"{i["date"]} - {i["day"]["condition"]["text"]}")

@bot.message_handler()
def zaglushka(message):
	text = message.text
	res = search_weather(text)
	bot.send_message(message.chat.id, res)
	
	


if __name__ == "__main__":
	bot.infinity_polling()
