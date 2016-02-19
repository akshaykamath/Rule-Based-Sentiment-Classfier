__author__ = 'akshay'

import sys
from BinarySentimentClassifier import BinarySentiment
from nltk.tokenize import TweetTokenizer

reload(sys)


class RuleBasedSentimentClassifier:
    sentences = []
    sentiment_dict = {}

    def __init__(self, sentiment_dict):
        self.sentiment_dict = sentiment_dict
        #self.sentences = sentences

    def perform_classification(self):
        for sentence in self.sentences:
            sentiment = self.classify_sentence(sentence)
            sentence_sentiment = sentence + " " + sentiment
            print sentence_sentiment

    def classify_sentence(self, sentence):
        sentence = sentence.lower()
        tokenizer = TweetTokenizer()
        tokens = tokenizer.tokenize(sentence)

        sentiment_score = 0
        for token in tokens:

            if self.sentiment_dict.has_key(token):
                sentiment_score += self.sentiment_dict[token]

        if sentiment_score >= 0:
            return BinarySentiment.Positive
        else:
            return BinarySentiment.Negative

        return BinarySentiment.Positive