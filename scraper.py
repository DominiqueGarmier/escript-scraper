'''
scraper to scrape analysis escript of Prof. Manfred Einsiedler

course: Analysis I & II at ETH Zurich
'''

import pdfkit
import requests
import re
import time
from bs4 import BeautifulSoup as bs


HOME_URL = "https://wp-prd.let.ethz.ch/skript5/part/einfuhrung/"

def get_all_urls(url):
    html = requests.get(url).text
    soup = bs(html, "html.parser")
    urls = [tag.get('href', '') for tag in soup.find_all() if tag.name == 'a']
    urls = [url for url in urls if url.find("part") != -1 or url.find("chapter") != -1]
    return urls


def make_pdf_and_save(url):
    file_name = url[max(url.find("part"), url.find("chapter")):]
    file_name = "./out/" + file_name.replace('/', '-') + '.pdf'
    pdfkit.from_url(url, file_name)


def main():
    all_urls = get_all_urls(HOME_URL)
    for url in all_urls:
        time.sleep(1)
        print(url, '...')

        try:
            make_pdf_and_save(url)
        except Exception:
            pass

if __name__ == '__main__':
    raise SystemExit(main())
