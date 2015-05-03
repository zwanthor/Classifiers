import re

def normalize_string(string):
    string= string.lower()
    #remove extra spaces
    string= re.sub('[\s]+', ' ', string)
    return string


