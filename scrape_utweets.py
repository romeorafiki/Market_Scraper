#This scrapes tiwtter data and impots into .xlsx


import tweepy
import pandas as pd

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

number_of_tweets = 200
tweets = []
likes = []
time = []

for i in tweepy.Cursor(api.user_timeline, id="tupac",tweet_mode="extended").items(number_of_tweets):
    tweets.append(i.full_text)
    likes.append(i.favorite_count)
    time.append(i.created_at)

df = pd.DataFrame({'tweets':tweets,'likes':likes,'time':time})
df.to_excel("C:\Python Projects\Data Collection\est_output.xlsx")