import spacy


def pos_tagging_spacy(text):
    nlp = spacy.load("fr_core_news_sm")
    doc = nlp(text)
    pos_tags = [(token.text, token.pos_) for token in doc]
    return pos_tags
