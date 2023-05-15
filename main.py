import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time, random, requests
from urllib.request import Request, urlopen
from fake_useragent import UserAgent
from IPython.display import clear_output

random_sleep = [2, 3, 4]
def random_proxy():
    return random.randint(0, len(proxies) - 1)

zillow_link = "https://www.zillow.com/atlanta-ga/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A34.020940947512194%2C%22east%22%3A-83.9150937578125%2C%22south%22%3A33.499180258111316%2C%22west%22%3A-85.0027402421875%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A403640%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A37211%2C%22regionType%22%3A6%7D%5D%7D"
url_google_form = "YOUR FORM HERE"


# It appears that zillow has now resorted to blocking any requests from my computer. What follows will seek to address this
ua = UserAgent()
proxies = []

proxies_req = Request('https://www.sslproxies.org/')
proxies_req.add_header('User-Agent', ua.random)

proxies_doc = urlopen(proxies_req).read().decode('utf8')

soup = BeautifulSoup(proxies_doc, 'html.parser')

proxies_table = soup.find(attrs={'class': ["table","table-striped","table-bordered"]})

# save proxies in an array
for row in proxies_table.tbody.find_all('tr'):
    proxies.append({
        'ip': row.find_all('td')[0].string,
        'port': row.find_all('td')[1].string
    })

# Choose a random proxy
proxy_index = random_proxy()
proxy = proxies[proxy_index]

for n in range(1, 20):
    req = Request('http:/icanhazip.com')
    req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')

#     Every 10 requests, generate a new proxy
    if n % 10 == 0:
        proxy_index = random_proxy()
        proxy = proxies[proxy_index]

#     Make the call
    try:
        my_ip = urlopen(req).read().decode('utf8')
        print('#' + str(n) + ': ' + my_ip)
        clear_output(wait=True)
    except: # If error, delete this proxy and find another one
        del proxies[proxy_index]
        print('Proxy ' + proxy['ip'] + ':' + proxy['port'] + ' deleted.')
        proxy_index = random_proxy()
        proxy = proxies[proxy_index]

# This will create different headers, pretending to be a browser.
user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

# Making a get request
user_agent = random.choice(user_agent_list)
headers = {'User-Agent': user_agent,
           'Accept-Language': 'en-US, en;q=0.5'}
proxy = random.choice(proxies)
response = requests.get(url=zillow_link,
                        headers=headers,
                        proxies=proxy)
zillow_webpage = response.text

soup_zillow = BeautifulSoup(zillow_webpage, 'lxml')
apt_listing_links = soup_zillow.find_all("a", {"class": ["StyledPropertyCardDataArea-c11n-8-84-0__sc-yipmu-0", "ednMDe", "property-card-link"]})
print(f"Num of links: {len(apt_listing_links)}")

# Getting the links for the listings and formatting correctly
for link in apt_listing_links:
    if "https://" in link['href']:
        # print(f"Formatted correctly: {link['href']}")
        print("Check")
    else:
        link['href'] = ''.join(('https://www.zillow.com',link['href']))

listing_links = []
listing_prices = []
listing_addrs = []
apt_listing_prices = soup_zillow.find_all("span",attrs={"data-test":"property-card-price"})
print(f"Testing:\tNum of prices: {len(apt_listing_prices)}")
for price in apt_listing_prices:
    listing_prices.append(price.text.split()[0][1:6])

for listing in apt_listing_links:
    listing_links.append(listing['href'])
    listing_addrs.append(listing.contents[0].contents)
    print(listing)
amended_listing_links = listing_links[::2]
amended_listing_addrs = listing_addrs[::2]
print(f"List of links len: {len(amended_listing_links)}\n"
      f"List of addrs len: {len(amended_listing_addrs)}")

# Final lists: amended_listing_links, amended_listing_addrs, listing_prices
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(url_google_form)

for apt in range(len(amended_listing_addrs)):
    time.sleep(random.choice(random_sleep))
    input_boxes = driver.find_elements(By.CSS_SELECTOR, ".whsOnd.zHQkBf")
    submit_btn = driver.find_element(By.CSS_SELECTOR, ".l4V7wb.Fxmcue")
    input_boxes[0].send_keys(amended_listing_addrs[apt])
    input_boxes[1].send_keys(listing_prices[apt])
    input_boxes[2].send_keys(amended_listing_links[apt])
    submit_btn.click()
    refresh_form_btn = driver.find_element(By.LINK_TEXT, "Submit another response")
    refresh_form_btn.click()