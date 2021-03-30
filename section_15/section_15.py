import requests
import bs4
# ---------------------------------------- Web Scraping - Grabbing a Title ----------------------------------------

# result = requests.get("http://www.example.com")
# soup = bs4.BeautifulSoup(result.text, "lxml")
# # print(soup)
# print(soup.select('title')[0].getText())
# site_paragraphs = soup.select('p')
# print(site_paragraphs[0].getText())

# ---------------------------------------- Web Scraping - Grabbing a Class ---------------------------------------
# res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
# soup = bs4.BeautifulSoup(res.text,"lxml")
# print(soup.select(".toctext"))
# for item in soup.select(".toctext"):
#     print(item.text)

# ---------------------------------------- Web Scraping - Grabbing an Image ----------------------------------------
# res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
# soup = bs4.BeautifulSoup(res.text,'lxml')
# image_info = soup.select('.thumbimage')
# print(len(image_info))
# computer = image_info[0]
# print(computer['src'])
# image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png')
# f = open('my_new_file_name.jpg', 'wb')
# f.write(image_link.content)
# f.close()

# ---------------------------------------- Web Scraping - Book Examples ----------------------------------------
# base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
# res = requests.get(base_url.format('1'))
# soup = bs4.BeautifulSoup(res.text,"lxml")
# soup.select(".product_pod")
# products = soup.select(".product_pod")
# example = products[0]
# type(example)
# example.attrs
# list(example.children)
# example.select('.star-rating.Three')
# example.select('.star-rating.Two')
# example.select('a')[1]['title']

# two_star_titles = []

# for n in range(1,51):

#     scrape_url = base_url.format(n)
#     res = requests.get(scrape_url)
    
#     soup = bs4.BeautifulSoup(res.text,"lxml")
#     books = soup.select(".product_pod")
    
#     for book in books:
#         if len(book.select('.star-rating.Two')) != 0:
#             two_star_titles.append(book.select('a')[1]['title'])

# print(two_star_titles)

# ---------------------------------------- Web Scraping - Exercises ----------------------------------------
import requests
import bs4

# res = requests.get('http://quotes.toscrape.com/')
# soup = bs4.BeautifulSoup(res.text, 'lxml')
# soup.select('.author')

# authors = set()
# for name in soup.select(".author"):
#     authors.add(name.text)

# print(authors)

# quotes = []
# for quote in soup.select(".text"):
#     quotes.append(quote.text)

# print(quotes)

# for item in soup.select('.tag-item'):
#     print(item.text)

# url = 'http://quotes.toscrape.com/page/'

# authors2 = set()

# for page in range(1,10):
#     page_url = url+str(page)

#     res = requests.get(page_url)

#     soup = bs4.BeautifulSoup(res.text, "lxml")

#     for name in soup.select(".author"):
#         authors2.add(name.text)

# print(authors)

url = 'http://quotes.toscrape.com/page/'
page_still_valid = True
authors = set()
page = 1

while page_still_valid:

    # Concatenate to get new page URL
    page_url = url+str(page)
    
    # Obtain Request
    res = requests.get(page_url)
    
    # Check to see if we're on the last page
    if "No quotes found!" in res.text:
        break
    
    # Turn into Soup
    soup = bs4.BeautifulSoup(res.text,'lxml')
    
    # Add Authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)
        
    # Go to Next Page
    page += 1

print(authors)