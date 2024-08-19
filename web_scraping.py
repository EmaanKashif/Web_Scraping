from bs4 import BeautifulSoup
import requests

url = 'https://www.freecodecamp.org/news/tag/web-development/'
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')

title = soup.title.get_text()
print("Freecode camp:", title)

links = soup.find_all('a')
for link in links:
    print("Link:", link.get('href'))

paragraph = soup.find('p').get_text()
print(paragraph)

headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
for heading in headings:
    print(heading.get_text())
