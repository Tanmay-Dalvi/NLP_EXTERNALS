# Install spacy and download the language model
!pip install spacy
!python -m spacy download en_core_web_sm

# Corrected code 
import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm") 

text = "Natural Language Processing it farcinating"

doc = nlp(text)

for token in doc:
    print(f"{token.text} : {token.pos_}") # Corrected attribute names