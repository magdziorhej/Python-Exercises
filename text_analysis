import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from collections import Counter
import matplotlib.pyplot as plt


nltk.download('punkt')


text = """
Kot pije mleko, a pies szczeka. Kot i pies to najlepsi przyjaciele, 
chociaż czasami się kłócą. Pies je karmę, a kot pije wodę.
"""


tokens = word_tokenize(text.lower())


bigrams = list(ngrams(tokens, 2))
trigrams = list(ngrams(tokens, 3))


bigram_freq = Counter(bigrams)
trigram_freq = Counter(trigrams)


top_n = 5  
most_common_bigrams = bigram_freq.most_common(top_n)
most_common_trigrams = trigram_freq.most_common(top_n)


def plot_ngram_frequency(ngrams, title):
    ngram_labels = [' '.join(ngram) for ngram, _ in ngrams]
    frequencies = [freq for _, freq in ngrams]

    plt.figure(figsize=(10, 6))
    plt.bar(ngram_labels, frequencies, color='skyblue')
    plt.xlabel('N-gramy')
    plt.ylabel('Częstość')
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


plot_ngram_frequency(most_common_bigrams, 'Most common bigrams')

plot_ngram_frequency(most_common_trigrams, 'Most common trigrams')
