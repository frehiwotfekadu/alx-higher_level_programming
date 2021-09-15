#!/usr/bin/python3
# 10-best_score.py


def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None
