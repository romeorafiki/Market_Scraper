import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

cursor = tweepy.Cursor(api.user_timeline, id='tupac',tweet_mode="extended").items(1)

for i in cursor:
    print(dir(i))