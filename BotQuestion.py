def question(x):
	text = x.lower()

	import string
	spec_chars = string.punctuation + '\xa0«»\t—…' 

	text = "".join([ch for ch in text if ch not in spec_chars])
	text = "".join([ch for ch in text if ch not in string.digits])

	import re
	text = re.split(" ", text)

	from nltk.corpus import stopwords
	rus_stopwords = stopwords.words("russian")
	text = [i for i in text if (i not in rus_stopwords) and (i != '')]

	import pymorphy2
	morph = pymorphy2.MorphAnalyzer()
	text = [morph.parse(i)[0].normal_form if morph.parse(i) else i for i in text]

	# print(text)

	return text


if __name__ == "__main__":
	q = input('Что ты хочешь у меня узнать?\n')
	print(question(q))
