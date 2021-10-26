import os

def process(first_str, second_str):
    return first_str + second_str

def get_text(filename):
    with open(filename, 'r') as file:
        string = file.read()
    return string

def clean_previous_text_file(path):
    os.remove(path)

def create_file(filename):
    return open("text_processed.txt", "a+")
