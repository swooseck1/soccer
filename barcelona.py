import requests
import csv
from bs4 import BeautifulSoup

# # makes a file as search csv
# csvFile= open("barcelona.csv", "wt")
# writer=  csv.writer(csvFile)
# writer.writerow(["HEADLINE", "URL"])

search_word="FC 바르셀로나"
url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query={}&sm=tab_srt&sort=1&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so%3Add%2Cp%3Aall%2Ca%3Aall&mynews=0&mson=0&refresh_start=0&related=0'.format(search_word)
headers = {'User-Agent': 'Mozila/5.0'}

req= requests.get(url, headers=headers)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

titles = soup.select(
    'ul.type01 > li > dl > dt > a'
)

#라인주소
url = 'https://notify-api.line.me/api/notify'
token = {'Authorization' : 'Bearer dwakjI1B4H7EW9RgwuV8IxBeSFwsgGzX4jcddX1LDbB'}

for title in titles:
    print(title['href'])
    message = title.text + "\n" + title['href']
    parameter = {"message": message}
    
    #response
    response = requests.post(
        url, headers = token, data=parameter)

# for title in titles:
#     print(title['href'])
#     print(title.text)

# try:
#     for title in titles:
#         link = title['href']
#         headline = title.text
#         writer.writerow([headline, link])
# finally:
#     csvFile.close()


print(response.text)
