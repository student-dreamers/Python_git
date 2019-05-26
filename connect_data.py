import json
import brno
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
    x=0
    w, h = 8, 1000;
    product = [[0 for x in range(w)] for y in range(h)]
    for row in data['ConceptsCollection']:
        ingredienc = row['Ingredients']
        ingredience = parse_ingedience(ingredienc)
        original_name = row['ProductName']
        product_description = row['ProductDescription']
        try:
            categori_id = row['CategoryIds'][2]
        except:
            categori_id = ""

        imageurl = row['ImageUrl']
        concept_code = row['ConceptCode']
        shop_url = "https://in.oriflame.com/products/product?code="+concept_code

        if 'categori_id' in locals():
            product[x] = [concept_code, "NULL", categori_id, original_name, product_description, imageurl, shop_url, ingredience]
            #print(x)
            x += 1
            #print(concept_code, "",  categori_id, original_name, product_description, imageurl, shop_url, ingredienc,)
    json_file.close()

with open('prices.json', encoding='utf-8') as price_json_file:
    data = json.load(price_json_file)
    for row in data['ConceptPricesCollection']:
        price = row['Price']['CurrentPrice']
        concept_code = row['ConceptCode']
        price = dict()
        price[concept_code] = price

brno.insert_data(product, price)


