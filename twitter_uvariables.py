import tweepy

consumer_key = "3gNCmlvUcSK5Vi7wbcA3iRaI8"
consumer_secret = "lPkYMnMY77CAYC5PocXXc7Hgk4r0c3RO9vBE6cSJFnDFGlSd4Y"
access_token = "1376736627708592130-Dh20BG1I8DGlVfLDIJ1Hgvs7TmhB3c"
access_token_secret = "U2KWfWfjmMhhkl44u3lwreZUQle968LR8HdSVyWbox003"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

cursor = tweepy.Cursor(api.user_timeline, id='tupac',tweet_mode="extended").items(2)

for i in cursor:
    print(dir(i))