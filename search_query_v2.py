import tweepy
import pandas as pd

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

number_of_tweets = 100
tweets = []
likes = []
time = []

for i in tweepy.Cursor(api.search, q='$GVSI',tweet_mode="extended").items(number_of_tweets):
    tweets.append(i.full_text)
    likes.append(i.favorite_count)
    time.append(i.created_at)

df = pd.DataFrame({'tweets':tweets,'likes':likes,'time':time})
df.to_excel("C:\Python Projects\Data Collection\$GVSI_9-19-21.xlsx")
