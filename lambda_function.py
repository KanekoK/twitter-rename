import os
import requests, json
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1Session
import re

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

def lambda_handler(event, context):
    URL = 'https://fortune.yahoo.co.jp/12astro/gemini'
    NAME = 'かねけん'
    html = requests.get(URL)
    soup = BeautifulSoup(html.text, 'html.parser')

    love_fate = soup.select_one('.yftn-md00 p').string
    pos = love_fate.find('。')
    love_fate = love_fate[:pos]

    # Twitterの名前変更
    twitter = OAuth1Session(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
    url = "https://api.twitter.com/1.1/account/update_profile.json"
    username = NAME + '🧝‍♀️' + love_fate + '(今日の双子座の恋愛運)'
    #変更したい名前の指定
    params = {"name": username}
    req = twitter.post(url, params = params)

    return {
        'edited_name': username,
        'status': req.status_code
    }

if __name__ == '__main__':
    lambda_handler()
