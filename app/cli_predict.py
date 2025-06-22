import pickle
import re
import nltk
import sys

# Load stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

# Load model and vectorizer
with open('svm_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Label index to emotion name mapping
label_mapping = {
    0: 'anger',
    1: 'fear',
    2: 'joy',
    3: 'love',
    4: 'sadness',
    5: 'surprise'
}

# Cleaning function (same as notebook)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text

# Main
def predict_emotion():
    user_input = input("Enter a sentence to detect its emotion:\n> ")
    cleaned = clean_text(user_input)
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)[0]
    print(f"\n🧠 Predicted Emotion: {label_mapping[pred].upper()}")

if __name__ == '__main__':
    predict_emotion()
