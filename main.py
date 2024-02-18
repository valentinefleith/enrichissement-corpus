import sys
from typing import List, Tuple
from pos_tagging_spacy import pos_tagging_spacy
from pos_tagging_stanza import pos_tagging_stanza
from csv_handle import write_to_csv, load_manual
from Token import construct_tokens


def load_text(path):
    with open(path, "r") as text:
        return text.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: py main.py path/to/text")
        sys.exit()
    text = load_text(sys.argv[1])
    spacy_tags = pos_tagging_spacy(text)
    stanza_tags = pos_tagging_stanza(text)
    manual_tags = load_manual("annotation_manuelle.csv")
    tokens = construct_tokens(spacy_tags, stanza_tags, manual_tags)
    for token in tokens:
        print(token.text)


if __name__ == "__main__":
    main()
