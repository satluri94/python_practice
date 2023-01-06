import requests #importing requests module to use all the http methods in the module 
from bs4 import BeautifulSoup
import csv
import sys

if len(sys.argv) < 2: #argv is the list of command-line arguments passed to the program while execution
    print("insufficient args")
    exit(0)

url = sys.argv[1] #Saving the elment in index[1] in argv list into a variable
print ("searching links in " + url)
webpage = requests.get(url) #url response is saved into a variable
soup = BeautifulSoup(webpage.content, 'html.parser') #creating a Soup object by parsing the HTML content in the response
all_links = [] #declaring the list

links = soup.select('a') #defining a variable to select 'a' tags from the Soup object

for allhref in links: #iterating through each of the 'a' tags
    text = allhref.text #extracting text from 'a' tags
    text = text.strip() if text is not None else '' #removing spaces from the text

    href = allhref.get('href') #extracting the href links from the 'a' tags
    href = href.strip() if text is not None else '' #removing spaces from the href
    all_links.append({"href": href.encode(), "text": text.encode()}) #appending each of the href, texp pair as a dictionary to the 'all_links' list
    print ({href})

#saving all the list as csv

keys = all_links[0].keys() 

with open('links.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_links)
