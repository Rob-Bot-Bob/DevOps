from bs4 import BeautifulSoup
import requests
url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url) #gets the request from the url and put in response so we can handle it with .text lxml
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4') #find all the div in the page, later we can find all the divs in difernet pages
count = 1
for i in items:
    itemName = i.find('h4', class_='card-title').text.strip('\n')
    itemPrice = i.find('h5').text
    print('%s ) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
    count = count + 1
pages = soup.find('ul',class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')
for link in links:
    pageNum= int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        x = link.get('href')
        urls.append(x)
print(urls)
count = 1
for i in urls:
    newUrl= url + i 
    response = requests.get(newUrl)
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4') #find all the div in the page, later we can find all the divs in difernet pages
    for i in items:
        itemName = i.find('h4', class_='card-title').text.strip('\n')
        itemPrice = i.find('h5').text
        print('%s ) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
        count = count + 1