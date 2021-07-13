def sinonim(text):
    import requests
    import re

    a = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20210505T163812Z.efcbddedee2a18cf.a576d68efc07ec4e7cbd7d7fc0f0a9ff1e5c35d4&lang=ru-ru&text=' + text
    response = requests.get(a)
    b = response.text
    mas = re.findall('text":"(.+?)",', b)

    return mas

if __name__ == "__main__":
    print(sinonim('красивый'))
