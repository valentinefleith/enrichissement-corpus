import sys
import numpy as np
import pandas as pd
from typing import List, Tuple
from pos_tagging_spacy import pos_tagging_spacy
from pos_tagging_stanza import pos_tagging_stanza
from csv_handle import write_to_csv, load_manual


def load_text(path):
    with open(path, "r") as text:
        return text.read()


def align_pos_tags(spacy_tags, stanza_tags):
    aligned = []
    spacy_index = 0
    stanza_index = 0
    while spacy_index < len(spacy_tags) - 1:
        if spacy_tags[spacy_index][1] == 'SPACE':
            spacy_index += 1
        if spacy_tags[spacy_index][0] != stanza_tags[stanza_index][0]:
            aligned.append([spacy_tags[spacy_index], stanza_tags[stanza_index]])
            spacy_index += 1
            stanza_index += 1
            while (spacy_tags[spacy_index][0] != stanza_tags[stanza_index][0]):
                aligned.append([("NA", "NA"), stanza_tags[stanza_index]])
                stanza_index += 1
        aligned.append([spacy_tags[spacy_index], stanza_tags[stanza_index]])
        spacy_index += 1
        stanza_index += 1
    aligned_spacy = [tag[0] for tag in aligned]
    aligned_stanza = [tag[1] for tag in aligned]
    return aligned_spacy, aligned_stanza


class Token:
    def __init__(self, text, spacy_tag, stanza_tag, manual_tag):
        self.text = text
        self.spacy_tag = spacy_tag
        self.stanza_tag = stanza_tag
        self.manual_tag = manual_tag


def parse_tags(spacy_tags, stanza_tags, manual_tags) -> List[Token]:
    tags = []
    for spacy_tag, stanza_tag, manual_tag in zip(spacy_tags, stanza_tags, manual_tags):
        tags.append(Token(manual_tag[0], spacy_tag[1], stanza_tag[1], manual_tag[1]))
    return tags

def main():
    if len(sys.argv) != 2:
        print("Usage: py main.py path/to/text")
        sys.exit()
    text = load_text(sys.argv[1])
    spacy_tags = pos_tagging_spacy(text)
    stanza_tags = pos_tagging_stanza(text)
    spacy_tags, stanza_tags = align_pos_tags(spacy_tags, stanza_tags)
    manual_tags = load_manual("annotation_manuelle.csv")
    tags = parse_tags(spacy_tags, stanza_tags, manual_tags)
    for tag in tags:
        print(tag.text)
    #for spacy_tag, stanza_tag in aligned_tags:
        #print("Spacy:", spacy_tag, "Stanza:", stanza_tag)


if __name__ == "__main__":
    main()
