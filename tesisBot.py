import requests, json, tweepy, nltk, re
from botFase1 import *
from random import randint

#hacemos una petición a la api via http y guardamos la db en formato json
api = requests.get('http://tesis.filos.unam.mx/api/theses?limit=0')
api = api.json()
total = api['total']
tesis_db = api['data']
#definimos funcion para imprimir tesis al azar
def randomThesis():
#tomamos una tesis al azar y guardamos algunos campos
    rand = randint(1, len(tesis_db))
    tesisRandom = tesis_db[rand]
    keywords = tesisRandom['keywords']
    url = tesisRandom['rawData']['file']
    author = tesisRandom['author']
    author = nltk.tokenize.word_tokenize(author)
    author = [i for i in author if len(i) > 1][::-1]
    author = re.sub("\W"," ",str(author))
    author = "".join(author)
    author = re.sub("[  ]+"," ",author)
    title = tesisRandom['title']
    year = tesisRandom['rawData']['year']
    grade = tesisRandom['degree']
    text = f"Tesis del año {year} titulada \"{title}\", escrita por{author}para obtener el grado en {grade}. La puedes consultar en {url}"
    return text


if __name__ == '__main__':
    segs = 600
    bot = twitter_setup()
    while True:
        tesis = randomThesis()
        bot.update_status(tesis)
        print(f'Tuit enviado: {tesis}')
        time.sleep(segs)
