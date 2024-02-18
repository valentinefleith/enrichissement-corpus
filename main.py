import sys
from typing import List
from pos_tagging_spacy import pos_tagging_spacy
from pos_tagging_stanza import pos_tagging_stanza
from csv_handle import load_manual
import evaluation
import Token


def load_text(path):
    with open(path, "r") as text:
        return text.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: py main.py path/to/text")
        sys.exit()
    text = load_text(sys.argv[1])
    spacy_tags, stanza_tags = Token.align_pos_tags(
        pos_tagging_spacy(text), pos_tagging_stanza(text)
    )
    manual_tags = load_manual("annotation_manuelle.csv")
    spacy_tokens = Token.construct_tokens(spacy_tags, manual_tags)
    stanza_tokens = Token.construct_tokens(stanza_tags, manual_tags)
    evaluation.compare_models(spacy_tokens, stanza_tokens)


if __name__ == "__main__":
    main()
