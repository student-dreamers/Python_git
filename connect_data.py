import json 
from collections import namedtuple

def strip_list(l):
    return([x.strip() for x in l])

def parse_ingedience(ingredience):
    lst = ingredience.split(",")
    list(map(str.strip, lst))
    lst = strip_list(lst)
    return lst 

with open('conceptdata.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
    ingredienc = data['ConceptsCollection'][0]['Ingredients']
    ingredienc = parse_ingedience(ingredienc)
    original_name = data['ConceptsCollection'][0]['ProductName']
    product_description = data['ConceptsCollection'][0]['ProductDescription']
    categori_id = data['ConceptsCollection'][0]['CategoryIds'][0]
    imageurl = data['ConceptsCollection'][0]['ImageUrl']
    concept_code = data ['ConceptsCollection'][0]['ConceptCode']
    shop_url = "https://in.oriflame.com/products/product?code="+concept_code
   # print(ingredienc ,original_name ,product_description,categori_id,imageurl,shop_url )
    json_file.close()

with open('prices.json', encoding='utf-8') as price_json_file:
    data = json.load(price_json_file)
    currnency = data['ConceptPricesCollection'][0]['Currency']
    price = data ['ConceptPricesCollection'][0]['Price']['CurrentPrice']
    concept_code = data['ConceptPricesCollection'][0]['ConceptCode']
    print(concept_code)

