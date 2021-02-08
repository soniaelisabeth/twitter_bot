from datetime import datetime, timedelta
from os import environ
import tweepy
import time
import os

CONSUMER_KEY = 'neoIwuLS9W8hyeoXhOlxfb1h0'
CONSUMER_SECRET = 'GLpH0VSwLUP160OqC0ksRJVA1aa2Gr5oNyWLuIX9mju6FOCRsA'
ACCESS_KEY = '1358064835448221702-doQwMjxXE9BHfOU2puiOlOEqJXRFfS'
ACCESS_SECRET = 'w4NMdAsfUpLF5bSftdowrpTVFxWVNiWJNcJ3Ky2QEbJT1'
    
tweet = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
tweet.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(tweet)
agora = datetime.today()
dia_da_semana = agora.weekday()
imagem = "gyro.png"

while True:
    if dia_da_semana == 0:
        api.update_with_media(imagem)
    
    time.sleep(86399)
