from datetime import datetime, timedelta
import tweepy
import time

CONSUMER_KEY = 'neoIwuLS9W8hyeoXhOlxfb1h0'
CONSUMER_SECRET = 'GLpH0VSwLUP160OqC0ksRJVA1aa2Gr5oNyWLuIX9mju6FOCRsA'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAMfpMQEAAAAAseWH4y0HtGv08Sb2%2BNQyIMDpzDk%3D56tRpHxHdaSmPvXN3OjQKmc9OoV1hCG0awbsWqofHTT0ufNny1'
ACCESS_KEY = '1358064835448221702-doQwMjxXE9BHfOU2puiOlOEqJXRFfS'
ACCESS_SECRET = 'w4NMdAsfUpLF5bSftdowrpTVFxWVNiWJNcJ3Ky2QEbJT1'
    
tweet = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
tweet.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(tweet)
agora = datetime.today()
dia_da_semana = agora.weekday()
image = 'gyro.py'

while True:
    if dia_da_semana == 3:
        api.update_with_media(image)
    else:
        api.update_status("gyro didn't turn stupd today ):")
    
    time.sleep(86399)