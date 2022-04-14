# Amazon_Product_review
## Aim
* It is an project to extract the amazon product details.
* It's aim is to extract the product details from the amazon website whichurl is listed in csv file.
## Required Details 
* Scraping the given information from the web Page.
  1. Product Title
  2. Product Image URL
  3. Price of the Product
  4. Product Details
* If any URL throws Error 404 then print the {URL} not available and skip that URL.
* Print Time Taken After Scraping every 100 URLs
* Dump the extracted data into a JSON file.
* Store the same data in MySQL database.
## Tools and Libraries Used 
* Create the repository and open with VS Code.
* Install Libraries - 

  ```pip install beautifulsoup4```
  
  ```pip install requests```
  
  ```pip install csv```
  
  ```pip install mysql```
 
* Create a database named "amazon_scrape" with table named "scraped_data".
* Run the Script with command 

  ```python s.py```
