#import urlopen and BeautifulSoup library
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

#Wikipedia Link for data
wikiLink = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Nepal'

#HTTP Rrequest
wikiClient = urlopen(wikiLink)
wikiHTML = wikiClient.read()
wikiClient.close()

#Parse the HTML file type
wikiBS = BS(wikiHTML,"html.parser")
containers = wikiBS.findAll("table",{"class":"wikitable"})[0].findAll("tr")

#Create and Open CSV file to store data and write related headers for the file
file = open("wikiCOVID19data.csv","w")
header = "district, cases, recovered, deaths, activeCases\n"
file.write(header)

num = len(containers)
containers = containers[2:num-1]

#Loop through each row in wiki-tables to catch the expected data in python variable and write in CSV file
for container in containers:
    district = container.th.text.replace("\n","")
    cases=container.findAll("td")[0].text.replace("\n","")
    recovered=container.findAll("td")[1].text.replace("\n","")
    deaths=container.findAll("td")[3].text.replace("\n","")
    activeCase=container.findAll("td")[5].text.replace("\n","")
    print(district+", "+cases+", "+recovered+", "+deaths+", "+activeCase+"\n")
    file.write(district+", "+cases+", "+recovered+", "+deaths+", "+activeCase+"\n")

#Close file after writing to it
file.close()