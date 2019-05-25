import json 
from collections import namedtuple

def parse_ingedience(ingredience):
    lst = ingredience.split(",")
 #   lst = lst.strip()
    return lst 

with open('conceptdata.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
    x = data['ConceptsCollection'][0]['Ingredients']
    parse_ingedience(x)