from bs4 import BeautifulSoup
import requests
import csv
import json
import time
from cookies import cookies, headers
from sql_data import dump_sql

#Important Variables
filename = open('Amazon_Scraping.csv', 'r')
start_time = time.time()
db = []
url = []
form = []
count = 1
printcounter = 0

#Extract CSV file data into a list
for line in csv.reader(filename):
    db.append(line)

#Make URLs from Extracted Data
for i in range(len(db)):
    url.append("https://www.amazon."+db[i][3]+"/dp/"+db[i][2])

#Main Code
for i in range(1,len(url)):
    try:
        dic = {}

        #Print Time Taken After Scraping every 100 URLs
        if (printcounter == 100):
            print("--- %s seconds ---" % (time.time() - start_time))
            printcounter = 0
        printcounter += 1

        #Using cookies to bypass Amazon Captcha
        response = requests.get(url[i], headers=headers, cookies=cookies)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        #ID
        dic['ID'] = count

        #Put Product URL into Dictionary
        dic['Product URL'] = url[i]

        #Put Product Title In Dictionary
        title = soup.find("span", {"id": "productTitle"})
        dic['Product Title'] = title.text.strip()

        #Put Product Image URL In Dictionary
        image = soup.find("div", {"id": "main-image-container"})
        image1 = image.find_all("img")
        for src in image1:
            dic['Product Image URL'] = src.get('src')

        #Put Product Price In Dictionary
        price = soup.find("span", {"class": "a-offscreen"})
        dic['Price of the Product'] = price.text.strip()

        #Put Product Details In Dictionary
        try:
            details = soup.find_all(lambda tag: tag.name=="div" and
			    tag.get("id")=="detailBulletsWrapper_feature_div" or 
			    tag.get("id") == "productDescription")
            for text in details:
                dic['Product Details'] = ' '.join(text.text.splitlines()).replace("  ","").encode('ascii','ignore').decode()
        #Exception Handling (In Case Product Doesn't Has Details)
        except:
            dic['Product Details'] = "NULL"

        #Dump the data in JSON file
        form.append(dic)
        with open("amazon.json", 'w') as json_file:
            json.dump(form, json_file, indent=4)

        count = count + 1
        print(str(i)+". "+url[i]+" scraped successfully.")

    #Exception Handling (If Page Returns 404 Error)
    except requests.exceptions.HTTPError:
        print(str(i)+". "+url[i]+" is not available.")
    except AttributeError:
        print(str(i)+". "+url[i]+" is ERROR.")

#Dump the data in MySQL database
dump_sql()