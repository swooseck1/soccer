import requests
import csv
from bs4 import BeautifulSoup 
from selenium import webdriver
# search_word = ""

path = "C:\\Users\\COM\\chromedriver_win32\\chromedriver.exe"
headers = {'User-Agent': 'Mozilla/5.0'}
driver = webdriver.Chrome(path)
pageNumber=1
for i in range(2):
    pageNumber += 1

url = 'https://sports.news.naver.com/wfootball/news/index.nhn?page={}&isphoto=N&type=latest'.format(pageNumber)


driver.get(url)
html = driver.page_source


# req = requests.get(url, headers=headers) # connection
# html = req.text
soup = BeautifulSoup(html,'html.parser')

csvFile = open("soccer.csv","wt")
writer = csv.writer(csvFile)
writer.writerow(["HeadLine", "URL"])

titles = []
titles1 = soup.select(
    '#_newsList > ul > li > div > a'
)
titles2 = soup.select(
    '#_newsList > ul > li > div > a'
)
titles.append(titles1)
titles.append(titles2)
# titles_by_find_all = soup.find_all(
#     "a"
# )

#driver.find_element_by_xpath("")

# print(titles)

for title in titles:
    # print(title['href'])
    print(title.text)


try :
    for title in titles:
        link = title['href']
        print(link)
        head = title.text
        writer.writerow([head, link])
finally :
    csvFile.close()