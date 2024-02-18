from typing import List
from tabulate import tabulate
from Token import Token


def calculate_metrics(tokens):
    lib_errors = 0
    for token in tokens:
        if token.lib_tag != token.manual_tag and token.lib_tag != "NA":
            lib_errors += 1
    total = len(tokens)
    precision = (total - lib_errors) / total
    recall = (total - lib_errors) / total
    fscore = 2 * (precision * recall) / (precision + recall)
    return precision, recall, fscore


def compare_models(spacy_tokens, stanza_tokens):
    spacy_precision, spacy_recall, spacy_fscore = calculate_metrics(spacy_tokens)
    stanza_precision, stanza_recall, stanza_fscore = calculate_metrics(stanza_tokens)
    header = ["Library", "Precision", "Recall", "F-score"]
    table = [
        ["Spacy", spacy_precision, spacy_recall, spacy_fscore],
        ["Stanza", stanza_precision, stanza_recall, stanza_fscore],
    ]
    print(tabulate(table, header, tablefmt="fancy_grid"))
