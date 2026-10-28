from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

from intent_data import intent_data


# Prepare training data
texts = []
labels = []

for intent, questions in intent_data.items():
    for question in questions:
        texts.append(question)
        labels.append(intent)


# Convert text into TF-IDF features
vectorizer = TfidfVectorizer(
    lowercase=True,
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(texts)


# Train Logistic Regression model
model = LogisticRegression(
    max_iter=1000
)

model.fit(X, labels)


# Save trained model
joblib.dump(model, "intent_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")


print("====================================")
print("NLP MODEL TRAINED SUCCESSFULLY")
print("====================================")
print("Training questions:", len(texts))
print("Intents:", len(intent_data))
print("Model saved successfully!")