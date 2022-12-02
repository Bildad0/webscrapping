# This is a sample Python script.
import csv
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

html = urlopen("https://en.wikipedia.org/wiki/Comparison_of_programming_languages")
soup = BeautifulSoup(html, "html.parser")
table = soup.findAll("table", {"class": "wikitable"})[0]
rows = table.findAll("tr")

with open("language.csv", "wt+", newline="") as f:
    writer = csv.writer(f)
    for i in rows:
        row = []
        for cell in i.findAll(["td", "th"]):
            row.append(cell.get_text())
        writer.writerow(row)


a = pd.read_csv("language.csv")
a.head()
