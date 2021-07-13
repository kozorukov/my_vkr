from BotQuestion import *
from BotAnswer import *
from sinonim import *

q = input('Что ты хочешь у меня узнать?\n')
text = question(q)
sin = []
for i in range(len(text)):
	sin = sin + sinonim(text[i])

text = sin
print(text)

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
			print(norm_answer[i])
else:
	print('У меня нет ответа на этот вопрос :((')
