import stanza


def pos_tagging_stanza(text):
    nlp = stanza.Pipeline("fr", processors="tokenize,pos", download_method=None)
    doc = nlp(text)
    pos_tags = [
        (word.text, word.pos) for sentence in doc.sentences for word in sentence.words
    ]
    return pos_tags
