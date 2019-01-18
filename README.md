# Sentiment-Analysis
Steps:
  1. Collecting tweets from twitter using twitter API and tweepy.
  2. Creating a dataset from the tweets.
  3. Using NLTK and machine learning to anlayse the dataset.


**Working of Basic sentiment analysis:**
  1. Tokenizes the input sentences.
  2. Removes any punctuation by comparing from string.punctuation.
  3. Removes all stopwords by comparing from nltk.stopwords, and converts to lowercase.
  4. Created a dictionary from EffectWordNet words, split them into three keys, +ve, -ve and null.
  5. Compared the words from the dictionary to the input tokens, +1 for word in +ve dataset and -1 for word in -ve dataset.
