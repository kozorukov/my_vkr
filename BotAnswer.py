def answers(x):
	answer = x.read()

	import re
	norm_answer = re.split("\n", answer)

	import string
	spec_chars = string.punctuation + '\xa0«»\t—…' 

	answer = "".join([ch for ch in answer if ch not in spec_chars])
	answer = "".join([ch for ch in answer if ch not in string.digits])

	answer = re.split("\n", answer)

	mas01 = []
	answer_tokens = []

	import pymorphy2
	morph = pymorphy2.MorphAnalyzer()

	for i in range(len(answer)):
		answer_tokens.append(re.split(" ", answer[i]))
		answer_tokens[i] = [morph.parse(ch)[0].normal_form if morph.parse(ch) else ch for ch in answer_tokens[i]]
		mas01.append(0)

	return norm_answer, answer_tokens, mas01


if __name__ == "__main__":
	a = open('answer.txt', encoding="utf-8")
	print(answers(a))
