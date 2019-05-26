import json 
from collections import namedtuple

def strip_list(l):
    return([x.strip() for x in l])

def parse_ingedience(ingredience):
    if(ingredience == None):
        return False
    lst = ingredience.split(",")
    list(map(str.strip, lst))
    lst = strip_list(lst)
    return lst 

data_send = [0]

data_send.append(5)


with open('conceptdata.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
    for x in range(300):
        print(x)
        ingredienc = data['ConceptsCollection'][x]['Ingredients']
        ingredienc = parse_ingedience(ingredienc)
        original_name = data['ConceptsCollection'][x]['ProductName']
        product_description = data['ConceptsCollection'][x]['ProductDescription']
       #categori_id = data['ConceptsCollection'][x]['CategoryIds'][0]
        imageurl = data['ConceptsCollection'][x]['ImageUrl']
        concept_code = data ['ConceptsCollection'][x]['ConceptCode']
        shop_url = "https://in.oriflame.com/products/product?code="+concept_code
        
        
        print(ingredienc ,original_name ,product_description,imageurl,shop_url )
    json_file.close()

with open('prices.json', encoding='utf-8') as price_json_file:
    data = json.load(price_json_file)
    currnency = data['ConceptPricesCollection'][0]['Currency']
    price = data ['ConceptPricesCollection'][0]['Price']['CurrentPrice']
    concept_code = data['ConceptPricesCollection'][0]['ConceptCode']
    print(concept_code)

