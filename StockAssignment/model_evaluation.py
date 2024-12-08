import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report


model = joblib.load('model/stock_predictor.pkl')


test_df = pd.read_csv('data/sentiment_tweets.csv')


X_test = test_df[['Polarity', 'Subjectivity']]
y_test = test_df['Price movement']
y_pred = model.predict(X_test)

print("Accuracy on Test Data:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
