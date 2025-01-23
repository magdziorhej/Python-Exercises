import json


positive_words = ["love", "great", "fantastic", "excellent", "new", "awesome"]
negative_words = ["terrible", "bad", "worse", "worst", "awful", "hate"]


tweets = [
    {"tweet_id": 1, "text": "I love the new features in this app!"},
    {"tweet_id": 2, "text": "This update is terrible."},
    {"tweet_id": 3, "text": "Decent app, could be better."},
]


def generate_ngrams(text, n):
    words = text.split()
    ngrams = [" ".join(words[i:i + n]) for i in range(len(words) - n + 1)]
    return ngrams


def analyze_sentiment_and_ngrams(text):
    text_lower = text.lower()


    unigrams = generate_ngrams(text_lower, 1)
    bigrams = generate_ngrams(text_lower, 2)
    trigrams = generate_ngrams(text_lower, 3)


    positive_count = 0
    negative_count = 0


    for unigram in unigrams:
        if unigram in positive_words:
            positive_count += 1
        if unigram in negative_words:
            negative_count += 1

    for bigram in bigrams:
        if bigram in positive_words:
            positive_count += 1
        if bigram in negative_words:
            negative_count += 1

    for trigram in trigrams:
        if trigram in positive_words:
            positive_count += 1
        if trigram in negative_words:
            negative_count += 1

    if positive_count > negative_count:
        sentiment = "positive"
    elif negative_count > positive_count:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return sentiment, {"unigrams": unigrams, "bigrams": bigrams, "trigrams": trigrams}


for tweet in tweets:
    sentiment, ngrams = analyze_sentiment_and_ngrams(tweet["text"])
    tweet["sentiment"] = sentiment
    tweet["ngrams"] = ngrams


with open("tweets_with_sentiment_and_ngrams.json", "w") as outfile:
    json.dump(tweets, outfile, indent=4)
