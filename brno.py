import random

def get_score():
    x = random.randrange(0,75)
    x = x/100
    return(x)

def get_price():
    x = random.randrange(49,299)
    return(x)

def insert_data(product, price):
    import mysql.connector

    mydb = mysql.connector.connect(
        host="138.197.181.210",
        user="student_dreamers",
        passwd="1bJSe9hcO5Jkj2G2Klz7",
        database="student_dreamers"
    )

    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM data_product;")
    mydb.commit()
    mycursor.close()
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM data_product_ingredient;")
    mydb.commit()
    mycursor.close()
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO `influence`(`name`, `description`, `score`) VALUES('Nepříznivý vliv na přírodu', 'Nepříznivý vliv na přírodu', '1');")
    mydb.commit()
    mycursor.close()
    mycursor = mydb.cursor()
    mycursor.execute(
        """INSERT INTO `data_product` (`uuid`,`ean` ,`category_id`, `name`, `description`, `url_image`, `url_shop`, `price`) values 
        ("31347", `8594008043876`, 70, "SoftCaress Protecting Hand & Nail Cream", "A light and fast absorbing hand cream that nourishes and conditions hands and nails. Formulated with intensively moisturising Macadamia Nut Oil to protect against dryness, helping to leave hands and nails healthy and hydrated without a greasy finish.","https://media-ce-cdn.oriflame.com/-/media/Images/Catalog/Products/_global/03/31/313/31347.ashx?u=0101010000&q=90" ,"https://cz.oriflame.com/products/product?code=31347" , "169");""")
    mydb.commit()
    mycursor.close()
    mycursor = mydb.cursor()

    i = 1

    for prod in product:
        try:
            price[prod[0]]
        except KeyError:
            price[prod[0]] = get_price() #TODO

        sql = "INSERT INTO `data_product` (`uuid`, `ean`, `category_id`, `name`, `description`, `url_image`, `url_shop`, `price`) VALUES (%s, %s, (SELECT id FROM data_category WHERE uuid = %s LIMIT 1), %s, %s, %s, %s, %s)"
        val = (prod[0], prod[1], prod[2], prod[3], prod[4], prod[5], prod[6], price[prod[0]])
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()
        mycursor = mydb.cursor()
        if (not(prod[7])):
            prod[7] = []
        for ingred in prod[7]:
            sql = "SELECT `name` FROM `ingredient`"
            mycursor.execute(sql)
            ingRaw = mycursor.fetchall()
            mydb.commit()
            mycursor.close()
            mycursor = mydb.cursor()
            ing = []
            for ingRow in ingRaw:
                ing.append(ingRow[0])
            if (ingred not in ing):
                sql = "INSERT INTO `ingredient` (`name`, `url_icon`) VALUES (%s, %s)"
                val = (ingred, "")
                mycursor.execute(sql, val)
                mydb.commit()
                mycursor.close()
                mycursor = mydb.cursor()
                ing.append(ingred)

                sql = "INSERT INTO `ingredient_influence` (ingredient_name, influence_id, score) values (%s, %s, %s)"
                val = (ingred, 5, get_score())
                mycursor.execute(sql, val)
                mydb.commit()
                mycursor.close()
                mycursor = mydb.cursor()

        for ingred in prod[7]:
            sql = "INSERT INTO `data_product_ingredient` (`product_id`, `ingredient_name`, `order`) VALUES ((SELECT id FROM data_product WHERE uuid = %s LIMIT 1), %s, %s)"
            val = (prod[0], ingred, i)
            mycursor.execute(sql, val)
            mydb.commit()
            mycursor.close()
            mycursor = mydb.cursor()
            i += 1



