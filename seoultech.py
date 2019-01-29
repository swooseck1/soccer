import requests
import csv
from bs4 import BeautifulSoup 

# search_word = "장학"
url = 'http://www.seoultech.ac.kr/service/info/notice/'
headers = {'User-Agent': 'Mozilla/5.0'}
 
req = requests.get(url, headers=headers) # connection
html = req.text
soup = BeautifulSoup(html,'html.parser')

csvFile = open("seoultech.csv","wt")
writer = csv.writer(csvFile)
writer.writerow(["HeadLine", "URL"])
titles = soup.select(
    'table > tbody > tr > td > a'
)

# titles_by_find_all = soup.find_all(
#     "a"
# )

# print(titles)

for title in titles:
    # print(title['href'])
    print(title.text)
try :
    for title in titles:
        link = title['href']
        head = title.text
        writer.writerow([head, link])
finally :
    csvFile.close()