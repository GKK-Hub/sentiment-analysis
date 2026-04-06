import re
import nltk

nltk.download('stopwords', quiet=True)
nltk.download('wordnet',   quiet=True)
nltk.download('punkt',     quiet=True)
nltk.download("punkt_tab")

from nltk.corpus import movie_reviews, stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

stop_words = stopwords.words('English')
lemmatizer = WordNetLemmatizer()


def preprocess(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation and numbers
    text = re.sub(r'[^a-z\s]', '', text)

    # Tokenize
    tokens = word_tokenize(text)

    # Remove stop words
    tokens = [token for token in tokens if token not in stop_words]

    # Lemmatize: convert it back to root word
    tokens  = [lemmatizer.lemmatize(token) for token in tokens]

    # Join tokens back to string
    return " ".join(tokens)


if __name__ == "__main__":
    print(preprocess("I'm not satisfied with this product... It say fresh which is why i purchased but I got the spoiled tapioca instead of fresh."))
