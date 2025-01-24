from transformers import pipeline
import spacy

nlp = spacy.load("en_core_web_sm")

def summarize_text(text, max_length=130, min_length=30):

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
 
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
  
    return summary[0]["summary_text"]

def analyze_text_spacy(text):
    doc = nlp(text)

    #total words
    total_words = len([token for token in doc if token.is_alpha])

    #unique words
    unique_words = len(set(token.text.lower() for token in doc if token.is_alpha))

 
    word_freq = {}
    for token in doc:
        if token.is_alpha:
            word = token.text.lower()
            word_freq[word] = word_freq.get(word, 0) + 1

    #part-of-speech
    pos_counts = {}
    for token in doc:
        pos = token.pos_
        pos_counts[pos] = pos_counts.get(pos, 0) + 1

    #dictionaries yay
    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "word_freq": dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]),
        "pos_counts": dict(sorted(pos_counts.items(), key=lambda x: x[1], reverse=True)),
    }

if __name__ == "__main__":
    input_text = """
    Rabbits are mammals, which is an animal that
    has warm blood and backbones. They are small,
    fluffy animals with short tails that look like a ball.
    They have long ears and whiskers. Their long legs
    let them hop around quickly. They can weigh one
    pound or even up to 16 pounds! Rabbits can live
    for about 10 years. Some people call rabbits
    bunnies, but they are the same. A female rabbit is called a doe while a male
    rabbit is called a buck.
    Rabbits have lots of babies, which are called kits.
    Kits are born without fur and can’t see. When the
    babies are 5 weeks old, they can live on their
    own. Rabbits can make their own families at 2 to
    3 months old.
    """

    #summarized text
    summary = summarize_text(input_text)

    original_analysis = analyze_text_spacy(input_text)
    summary_analysis = analyze_text_spacy(summary)

    # Print results
    print("Original Text Analysis:")
    for key, value in original_analysis.items():
        print(f"{key}: {value}")

    print("\nSummarized Text Analysis:")
    for key, value in summary_analysis.items():
        print(f"{key}: {value}")

    print("\nOriginal Text:\n", input_text)
    print("\nSummarized Text:\n", summary)
