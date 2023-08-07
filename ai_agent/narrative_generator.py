```python
import random
import nltk
from nltk.corpus import brown

class NarrativeGenerator:
    def __init__(self):
        self.sentences = brown.sents()

    def generate_sentence(self):
        sentence = random.choice(self.sentences)
        return ' '.join(sentence)

    def generate_narrative(self, num_sentences=5):
        narrative = [self.generate_sentence() for _ in range(num_sentences)]
        return ' '.join(narrative)

narrative_generator = NarrativeGenerator()
```