import tweepy
import pandas as pd

consumer_key = "3gNCmlvUcSK5Vi7wbcA3iRaI8"
consumer_secret = "lPkYMnMY77CAYC5PocXXc7Hgk4r0c3RO9vBE6cSJFnDFGlSd4Y"
access_token = "1376736627708592130-Dh20BG1I8DGlVfLDIJ1Hgvs7TmhB3c"
access_token_secret = "U2KWfWfjmMhhkl44u3lwreZUQle968LR8HdSVyWbox003"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

number_of_tweets = 200
tweets = []
likes = []
time = []

for i in tweepy.Cursor(api.search, q='$GVSI',tweet_mode="extended").items(number_of_tweets):
    tweets.append(i.full_text)
    likes.append(i.favorite_count)
    time.append(i.created_at)

df = pd.DataFrame({'tweets':tweets,'likes':likes,'time':time})
df.to_excel("C:\Python Projects\Data Collection\$GVSI_9-19-21.xlsx")
