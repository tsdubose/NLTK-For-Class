import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()
my_sentiment = sia.polarity_scores("Wow, NLTK is really powerful!")
print(my_sentiment)