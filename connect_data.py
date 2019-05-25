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
    ingredienc = data['ConceptsCollection'][0]['Ingredients']
    ingredienc = parse_ingedience(ingredienc)
    original_name = data['ConceptsCollection'][0]['ProductName']
    product_description = data['ConceptsCollection'][0]['ProductDescription']
    categori_id = data['ConceptsCollection'][0]['CategoryIds'][0]
    imageurl = data['ConceptsCollection'][0]['ImageUrl']

    print(ingredienc ,original_name ,product_description,categori_id,imageurl )