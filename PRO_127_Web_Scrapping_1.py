import csv
import requests
from bs4 import BeautifulSoup

html_text = requests.get("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars").text
soup = BeautifulSoup(html_text, 'html.parser')

headers = ['Name', 'Distance(light-years)', 'Mass', 'Radius']
table = soup.find('table')
table_body = table.tbody

names = []
dists = []
masses = []
radii = []

# Finding Names
for row in table_body.find_all('tr'):
    data =  row.find_all('td')
    if data != []:
        try:
            name = data[1].a.text
            names.append(name)
        except:
            names.append(data[1].text)
    else:
        continue

# Finding Distance
for row in table_body.find_all('tr'):
    data = row.find_all('td')
    if data != []:
        try:
            dist = data[3].text
            final = dist.strip("\n")
            if "[1]" in final:
                dists.append(final[:-3])
            else:
                dists.append(final)
        except:
            print("Error")
    else:
        continue

# Finding Mass
for row in table_body.find_all('tr'):
    data = row.find_all('td')
    if data != []:
        try:
            mass = data[5].text
            masses.append(mass.strip("\n"))
        except:
            print("Error")

    else:
        continue

# Finding Radius
for row in table_body.find_all('tr'):
    data = row.find_all('td')
    if data != []:
        try:
            radius = data[6].text
            radii.append(radius.strip("\n"))
        except:
            print("Error")

    else:
        continue

# Writing a CSV file
with open("Star_data.csv", "w", newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    for i in range(0,98):
        try:
            csv_writer.writerow([names[i], dists[i], masses[i], radii[i]])
        except:
            csv_writer.writerow(["Error", "Error", "Error", "Error"])
    