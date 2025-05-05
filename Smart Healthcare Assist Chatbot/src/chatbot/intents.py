from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class IntentHandler:
    def __init__(self, intents):
        self.intents = intents
        self.vectorizer = TfidfVectorizer()
        self.train_examples()

    def train_examples(self):
        # Collect all examples for training
        self.examples = []
        self.intent_map = []
        for intent in self.intents['intents']:
            for example in intent['examples']:
                self.examples.append(example)
                self.intent_map.append(intent['intent'])
        self.tfidf_matrix = self.vectorizer.fit_transform(self.examples)

    def match_intent(self, user_input):
        # Transform user input and calculate similarity
        user_input_tfidf = self.vectorizer.transform([user_input])
        similarities = cosine_similarity(user_input_tfidf, self.tfidf_matrix)
        best_match_index = similarities.argmax()
        if similarities[0, best_match_index] > 0.5:  # Threshold for matching
            return self.intent_map[best_match_index]
        return "unknown"