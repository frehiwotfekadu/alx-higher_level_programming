#!/usr/bin/python3
# 102-complex_delete.py


def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary."""
    tmp = a_dictionary.copy()
    for k, v in tmp.items():
        if value == v:
            a_dictionary.pop(k)
    return a_dictionary
