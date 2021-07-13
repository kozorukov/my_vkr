import telebot
from BotQuestion import *
from BotAnswer import *
from sinonim import *

bot = telebot.TeleBot('1727168363:AAEz3_XaDa5tTPO8w7C10-uga1OYouMm-R8')


@bot.message_handler(content_types='text')
def get_text_messages(message):
	q = message.text
	if q == "/start":
		bot.send_message(message.from_user.id, "Привет, друг мой! Я помогу тебе найти ответы, касающиеся поступления и обучения в РГПУ им. А.И. Герцена")
	elif q =="/help":
		bot.send_message(message.from_user.id, "Задавай мне вопросы - помогу, чем смогу!")
	else:
		text = question(q)
		sin = []
		for i in range(len(text)):
			sin = sin + sinonim(text[i])

		text = sin
		a = open('answer.txt', encoding="utf-8")
		norm_answer, answer_tokens, mas01 = answers(a)

		for i in range(len(text)):
			for j in range(len(answer_tokens)):
				for g in range(len(answer_tokens[j])):
					if text[i] == answer_tokens[j][g]:
						mas01[j] = mas01[j] + 1

		k = 0
		for i in range(len(mas01)):
			if mas01[i] > k:
				k = mas01[i]

		if k != 0:
			for i in range(len(mas01)):
				if mas01[i] == k:
					bot.send_message(message.from_user.id, norm_answer[i])
		else:
			bot.send_message(message.from_user.id, "У меня нет ответа на этот вопрос :((")


bot.polling(none_stop=True, interval=0)
