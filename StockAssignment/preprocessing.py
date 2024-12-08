import pandas as pd
import re
from textblob import TextBlob


tweets_df = pd.read_csv('data/stock_tweets.csv')


def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text


tweets_df['Cleaned_Tweet'] = tweets_df['Tweet'].apply(clean_text)


tweets_df['Polarity'] = tweets_df['Cleaned_Tweet'].apply(lambda x: TextBlob(x).sentiment.polarity)
tweets_df['Subjectivity'] = tweets_df['Cleaned_Tweet'].apply(lambda x: TextBlob(x).sentiment.subjectivity)


tweets_df.to_csv('data/sentiment_tweets.csv', index=False)
