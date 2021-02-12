import datetime
from os import environ
import tweepy
import time
import os

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']
    
tweet = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
tweet.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(tweet)
agora = datetime.datetime.today()
dia_da_semana = agora.weekday()
imagem = "gyro.png"

dia_semana_lista = [
"segunda", "terça",
"quarta", "quinta", "sexta"]

while True:
    if dia_semana_lista[dia_da_semana] == "quarta":
        api.update_with_media(imagem)
    
    time.sleep(86399)
