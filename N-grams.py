!pip install nltk
import nltk
from nltk.util import ngrams
from collections import Counter
import matplotlib.pyplot as plt

# Download necessary NLTK data
# Download 'punkt_tab' to resolve the LookupError
nltk.download('punkt_tab') 

# Define the function to analyze n-grams
def analyze_ngrams(text: str, n: int = 2, top_n: int = 10) -> None:
    """
    Analyze n-grams in the given text and plot the most common ones.

    Args:
        text (str): The input text to analyze.
        n (int): The size of the n-grams to generate (default is 2 for bigrams).
        top_n (int): The number of top n-grams to display in the plot.
    """
    # Tokenize the text
    try:
        tokens = nltk.word_tokenize(text)
    except LookupError as e:
        print(f"Error with tokenizer: {e}")
        print("Trying to redownload 'punkt' resource...")
        nltk.download('punkt')
        tokens = nltk.word_tokenize(text)

    # Handle edge case: text too short for n-grams
    if len(tokens) < n:
        print(f"Text is too short to generate {n}-grams.")
        return

    # Generate unigrams, bigrams, and trigrams
    unigrams = list(ngrams(tokens, 1))
    bigrams = list(ngrams(tokens, 2))
    trigrams = list(ngrams(tokens, 3))

    # Print sample n-grams for clarity
    print("Sample Unigrams:", unigrams[:10])
    print("Sample Bigrams:", bigrams[:10])
    print("Sample Trigrams:", trigrams[:10])

    # Generate n-grams of the specified size
    ngram_counts = Counter(ngrams(tokens, n))

    # Print n-gram frequencies
    print(f"{n}-gram Frequencies:", ngram_counts.most_common(top_n))

    # Extract the most common n-grams
    most_common = ngram_counts.most_common(top_n)
    labels, values = zip(*most_common)

    # Plot the most common n-grams
    plt.figure(figsize=(10, 5))
    plt.bar([' '.join(gram) for gram in labels], values, color='skyblue')
    plt.title(f"Most Common {n}-grams")
    plt.xlabel("N-grams")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Example text for analysis
text = ("People become vegetarians for many reasons, including health, religious convictions, "
        "concerns about animal welfare or the use of antibiotics and hormones in livestock, "
        "or a desire to eat in a way that avoids excessive use of environmental resources.")
analyze_ngrams(text, n=2, top_n=10)
