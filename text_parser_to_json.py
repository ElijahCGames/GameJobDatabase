import spacy
from spacy.matcher import Matcher
import re

import pandas as pd

import get_text

nlp = spacy.load("en_core_web_sm")

def load_in_text():
    return Text(input("Get some text"))

class Text:
    def __init__(self,text):
        self.text = text;
        self.skills = {}
        self.name = ""

    def set_skills():
        pass
    def set_name():
        pass
    def dump_to_json():
        pass

if __name__ == "__main__":
    entry = load_in_text()
    entry.set_skills()
    entry.set_name()
    entry.dump_to_json()
