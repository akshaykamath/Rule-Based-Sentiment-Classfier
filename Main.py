__author__ = 'Akshay'

import sys
from SentWordNetDataCleaner import SentWordNetDataCleaner
from RuleBasedClassifier import RuleBasedSentimentClassifier

reload(sys)
sys.setdefaultencoding('utf-8')


def prepare_data_set():
    sent_word_cleaner = SentWordNetDataCleaner()
    sent_word_cleaner.prepare_sent_word_data()


def main():

    sentence = "this is extremely bad."
    sent_word_cleaner = SentWordNetDataCleaner()
    sentiment_dict = sent_word_cleaner.get_sent_word_dict()
    rule_based_classifier = RuleBasedSentimentClassifier(sentiment_dict)
    verdict = rule_based_classifier.classify_sentence(sentence)

    print verdict


    print "######## Exit ###########"

if __name__ == "__main__":
    main()
