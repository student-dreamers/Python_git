import json 
from collections import namedtuple

def strip_list(l):
    return([x.strip() for x in l])

def parse_ingedience(ingredience):
    lst = ingredience.split(",")
    list(map(str.strip, lst))
    lst = strip_list(lst)
    print(lst)
    return lst 

with open('conceptdata.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
    x = data['ConceptsCollection'][0]['Ingredients']
    parse_ingedience(x)

    