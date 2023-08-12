from urllib.request import urlopen
import html
from bs4 import BeautifulSoup
import csv

url = "https://en.m.wikipedia.org/wiki/List_of_inorganic_compounds"
page = urlopen(url)
raw_html = page.read()

soup = BeautifulSoup(raw_html, 'html.parser')
# print(soup.prettify())

all_compounds = soup.find_all('span', {'class': 'chemf nowrap'})

compounds_string = []
for compound in all_compounds:
    expr = ""
    for x in compound:
        if hasattr(x, 'childrne'):
            for y in x.children:
                if isinstance(y, str): expr += y
        else:
            if isinstance(x, str): expr += x
    
    # print(f"expression: {expr}")
    # print(f"raw html: {compound}")
    compounds_string.append(expr)

# print(len(compounds_string))
# print(f"Number of compounds: {len(all_compounds)}")

with open("compounds.csv", "w", newline="") as csvfile:
    csvwrite = csv.writer(csvfile, delimiter=",")
    for compound in compounds_string:
        csvwrite.writerow([compound])