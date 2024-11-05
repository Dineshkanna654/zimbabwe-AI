import spacy
from textblob import TextBlob
from symspellpy import SymSpell, Verbosity
import pkg_resources

# Load spaCy language model
nlp = spacy.load("en_core_web_sm")

# Initialize SymSpell for spell correction (if using SymSpell)
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
dictionary_path = pkg_resources.resource_filename("symspellpy", "frequency_dictionary_en_82_765.txt")
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)


def correct_spelling_textblob(text):
    blob = TextBlob(text)
    return str(blob.correct())

def correct_spelling_symspell(text):
    corrected_words = []
    for word in text.split():
        suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)
        if suggestions:
            corrected_words.append(suggestions[0].term)
        else:
            corrected_words.append(word)
    return " ".join(corrected_words)


def process_text(text, method="textblob"):
    # Run spaCy NLP pipeline
    doc = nlp(text)

    # Extract corrected text
    if method == "textblob":
        corrected_text = correct_spelling_textblob(doc.text)
    elif method == "symspell":
        corrected_text = correct_spelling_symspell(doc.text)
    else:
        corrected_text = doc.text  # No correction if an unknown method is provided

    return corrected_text


text = "Outstanding Amt"
corrected_text = process_text(text, method="textblob")  # or method="symspell"
print("Corrected Text:", corrected_text)
