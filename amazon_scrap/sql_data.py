import json
import mysql.connector

def dump_sql():

    #Read data from JSON file
    json_data=open('amazon.json').read()
    json_obj = json.loads(json_data)

    #Connect Database
    con = mysql.connector.connect(host = 'localhost', user = 'root', passwd = '', db = 'amazon_scrape')
    cursor = con.cursor()

    #Put JSON extraced data into variables
    for i, item in enumerate(json_obj):
        id = item.get("ID", None)
        url = item.get("Product URL", None)
        title = item.get("Product Title", None)
        image = item.get("Product Image URL", None)
        price = item.get("Price of the Product", None)
        detail = item.get("Product Details", None)

        #Insert data into the database
        cursor.execute("INSERT INTO `scraped_data` (`ID`, `Product URL`, `Product Title`, `Product Image URL`, `Price of the Product`, `Product Details`) VALUES (%s, %s, %s, %s, %s, %s)", (id, url, title, image, price, detail))

    con.commit()
    con.close()