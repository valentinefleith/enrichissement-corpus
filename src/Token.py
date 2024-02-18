from typing import List, Tuple


class Token:
    def __init__(self, text, lib_tag, manual_tag):
        self.text = text
        self.lib_tag = lib_tag
        self.manual_tag = manual_tag


def construct_tokens(lib_tags, manual_tags) -> List[Token]:
    tags = []
    for lib_tag, manual_tag in zip(lib_tags, manual_tags):
        tags.append(Token(manual_tag[0], lib_tag[1], manual_tag[1]))
    return tags


def align_pos_tags(spacy_tags, stanza_tags):
    aligned = []
    spacy_index = 0
    stanza_index = 0
    while spacy_index < len(spacy_tags) - 1:
        if spacy_tags[spacy_index][1] == "SPACE":
            spacy_index += 1
        if spacy_tags[spacy_index][0] != stanza_tags[stanza_index][0]:
            aligned.append([spacy_tags[spacy_index], stanza_tags[stanza_index]])
            spacy_index += 1
            stanza_index += 1
            while spacy_tags[spacy_index][0] != stanza_tags[stanza_index][0]:
                aligned.append([("NA", "NA"), stanza_tags[stanza_index]])
                stanza_index += 1
        aligned.append([spacy_tags[spacy_index], stanza_tags[stanza_index]])
        spacy_index += 1
        stanza_index += 1
    aligned_spacy = [tag[0] for tag in aligned]
    aligned_stanza = [tag[1] for tag in aligned]
    return aligned_spacy, aligned_stanza
