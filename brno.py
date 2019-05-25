import mysql.connector

mydb = mysql.connector.connect(
  host="138.197.181.210",
  user="student_dreamers",
  passwd="1bJSe9hcO5Jkj2G2Klz7",
  database="student_dreamers"
)

mycursor = mydb.cursor()

def insert_data(category, product):
    sql = """START TRANSACTION;
DELETE FROM ingredient_influence;
DELETE FROM data_product_ingredient;
DELETE FROM influence;
DELETE FROM data_product;
DELETE FROM data_category;

INSERT INTO `data_category` (`id`, `uuid`, `name`, `url_icon`) VALUES
(1,	'test',	'test',	NULL),
(2,	'test2',	'test2',	NULL);


INSERT INTO `data_product` (`id`, `uuid`, `ean`, `category_id`, `name`, `description`, `url_image`, `url_shop`, `price`) VALUES
(1,	'test',	'test',	1,	'test',	'',	'',	'',	4.00),
(2,	'test2',	'test2',	1,	'test2',	'',	'',	'',	2.00);

INSERT INTO `influence` (`id`, `name`, `description`) VALUES
(1,	'Ničí to zvířátka',	'helpppp'),
(2,	'Ničí to stromečky',	'pomoooooooc');

INSERT INTO `data_product_ingredient` (`product_id`, `ingredient_name`, `order`, `amount`) VALUES
(1,	'SUGAR',	0,	0.40000),
(1,	'SALT',	1,	0.60000),
(2,	'SALT',	0,	1);

INSERT INTO `ingredient_influence` (`ingredient_name`, `influence_id`, `score`) VALUES
('SUGAR',	1,	0.500),
('SUGAR',	2,	0.500),
('SALT',	1,	0.400),
('SALT',	2,	0.600);

COMMIT;"""
    mycursor.execute(sql)
    mydb.commit()

    for cat in category["CategoriesCollection"]:
        sql = "INSERT INTO `data_category` (`uuid`, `name`) VALUES (%s, %s)"
        val = (cat["Id"], cat["Name"])
        mycursor.execute(sql, val)
        mydb.commit()


    sql = "INSERT INTO `ingredient` (`name`) VALUES (%s)"
    val = "" #TODO
    mycursor.execute(sql, val)
    mydb.commit()

    for prod in product["ConceptsCollection"]:
        sql = "INSERT INTO `data_product` (`uuid`, `ean`, `category_id`, `name`, `description`, `url_image`, `url_shop`, `price`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (prod["ConceptCode"], , prod["CategoryIds"], prod["ProductName"], prod["ProductDescription"], prod["ImageUrl"])  # todo
        mycursor.execute(sql, val)
        mydb.commit()

        sql = "INSERT INTO `data_product_ingredient` (`product_id`, `ingredient_name`, `order`, `amount`) VALUES (%s, %s, %s, %s)"
        val = ""
        mycursor.execute(sql, val)
        mydb.commit()

