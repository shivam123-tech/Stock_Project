import tweepy
import pandas as pd


API_KEY = 'bustysbdshieiy15uhdujhdi'
API_SECRET_KEY = 'nigsgdub098uhh88w67y'
ACCESS_TOKEN = 'chiskouosiiw0nu0oijhin'
ACCESS_TOKEN_SECRET = 'idjoskmlksokxoioijz987'


auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)


def scrape_tweets(keywords, num_tweets=1000):
    tweets_data = []
    for keyword in keywords:
        for tweet in tweepy.Cursor(api.search_tweets, q=keyword, lang='en', tweet_mode='extended').items(num_tweets):
            tweets_data.append(tweet.full_text)
    return pd.DataFrame(tweets_data, columns=["Tweet"])


keywords = ["stock market", "stock prediction", "buy stock", "investing"]
tweets_df = scrape_tweets(keywords)
tweets_df.to_csv('data/stock_tweets.csv', index=False)
