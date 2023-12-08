#!/usr/bin/env python
# coding: utf-8

# In[30]:


#libraries
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor


# In[31]:


#Function to fetch url


# In[44]:


def scrape_page(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('html')
        print(f"Scraped {url}, found {len(links)} links.")
        print(f"Links : {links}.")
    except Exception as e:
        print(f"Error scrapping {url} : {e}")


# In[33]:


#Mutli threaded scraper


# In[45]:


def multi_threaded_scraper(urls,num_threads):
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(scrape_page, urls)


# In[35]:


#urls


# In[46]:


url_list = ["https://www.geo.tv/","https://www.express.pk/","https://arynews.tv/"]


# In[47]:


num_threads = len(url_list)


# In[48]:


if __name__ == "__main__":
    multi_threaded_scraper(url_list,len(url_list))


# In[ ]:




