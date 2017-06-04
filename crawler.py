
import re
import urllib.request
import urllib.parse
from selenium import webdriver
from bs4 import BeautifulSoup

SEARCH_FOR = input("Search for: ")
TO_FIND = input("Regex to search for in websites: ")
SEARCH_FUNCTION = re.compile(TO_FIND)

VISITED = list()
ADDED = list()

QUERRY = urllib.parse.urlencode({'q': SEARCH_FOR})
DRIVER = webdriver.PhantomJS()
FILE_OUTPUT = open('result.txt', 'wb')

print('DuckDuckGo:')
DUCK_URL = 'https://duckduckgo.com/?%s' % QUERRY
DRIVER.get(DUCK_URL)
SOUP = BeautifulSoup(DRIVER.execute_script('return document.documentElement.innerHTML;'),
                     'html.parser')

for result in SOUP.find_all('a', attrs={'class':'result__a'}):
    page_url = result.get('href')
    if page_url in VISITED:
        continue
    else:
        VISITED.append(page_url)
    print('Crawling {} ...'.format(page_url))
    DRIVER.get(page_url)
    page = DRIVER.execute_script('return document.documentElement.innerHTML;')
    found = re.findall(SEARCH_FUNCTION, page)
    for one_of in found:
        print('- {}'.format(one_of))
        if one_of in ADDED:
            continue
        else:
            ADDED.append(one_of)
        FILE_OUTPUT.write(one_of.encode("utf8") + '\n'.encode('utf8'))

print('Bing:')
BING_URL = 'https://www.bing.com/search?%s' % QUERRY
DRIVER.get(BING_URL)
SOUP = BeautifulSoup(DRIVER.execute_script('return document.documentElement.innerHTML;'),
                     'html.parser')

for result in SOUP.find_all('li', attrs={'class':'b_algo'}):
    page_url = result.find('a').get('href')
    if page_url in VISITED:
        continue
    else:
        VISITED.append(page_url)
    print('Crawling {} ...'.format(page_url))
    DRIVER.get(page_url)
    page = DRIVER.execute_script('return document.documentElement.innerHTML;')
    found = re.findall(SEARCH_FUNCTION, page)
    for one_of in found:
        print('- {}'.format(one_of))
        if one_of in ADDED:
            continue
        else:
            ADDED.append(one_of)
        FILE_OUTPUT.write(one_of.encode("utf8") + '\n'.encode('utf8'))

print('Yahoo:')
YAHOO_URL = 'https://search.yahoo.com/search?%s' % QUERRY
DRIVER.get(YAHOO_URL)
SOUP = BeautifulSoup(DRIVER.execute_script('return document.documentElement.innerHTML;'),
                     'html.parser')

for result in SOUP.find_all('a', attrs={'class':'ac-algo'}):
    page_url = result.get('href')
    if page_url in VISITED:
        continue
    else:
        VISITED.append(page_url)
    print('Crawling {} ...'.format(page_url))
    DRIVER.get(page_url)
    page = DRIVER.execute_script('return document.documentElement.innerHTML;')
    found = re.findall(SEARCH_FUNCTION, page)
    for one_of in found:
        print('- {}'.format(one_of))
        if one_of in ADDED:
            continue
        else:
            ADDED.append(one_of)
        FILE_OUTPUT.write(one_of.encode("utf8") + '\n'.encode('utf8'))

FILE_OUTPUT.close()
