import csv
filename = "Amazon Scraping - Sheet1.csv"
with open(filename,'r') as f_obj:
    csv_reader = csv.reader(f_obj)
    next(f_obj)
    for line in f_obj:
        ar = list(line.split(","))
        asin = ar[2]
        country = ar[3]
        print(asin,country)
        