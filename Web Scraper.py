import requests
from bs4 import BeautifulSoup

url = "https://www.codewithtomi.com/"

# Make a request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "lxml")

title = soup.find_all('h2',{'class':'post-title'})

tile[0].getText()

title1 = title[0].getText()

print(title1)

for t in title:
    print(t.getText())


