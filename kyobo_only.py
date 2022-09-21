import requests
from bs4 import BeautifulSoup

# ISBN input
isbn_input = input(": ")
dash_removed = isbn_input.replace("-", "")
isbn_removed = dash_removed.replace("ISBN", "").replace("isbn", "")


def cut_after_blank(string):
    try:
        idx = string.index(" ", 6)
        return string[:idx]
    except:
        return string


cut_blank = cut_after_blank(isbn_removed)
max_to_thirteen = cut_blank[:13]

isbn = max_to_thirteen

# request book data from kyobobook.co.kr
res = requests.get(f"https://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode={isbn}")
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# scrap data
org_price_elem = soup.find("span", attrs={"class": "org_price"})
org_price = org_price_elem.get_text().replace(",", "").replace("원", "").strip()

title_elem = soup.find("h1", attrs={"class": "title"}).find("strong")
title = title_elem.get_text().strip()

author_elem = soup.find("span", attrs={"class": "name"})
author_atags = author_elem.find_all("a")
authors = []
for item in author_atags:
    authors.append(item.get_text().strip())

author = ", ".join(authors)

publisher_elem = soup.find("span", attrs={"class": "name", "title": "출판사"})
publisher = publisher_elem.get_text().strip()

pubdate_elem = soup.find("span", attrs={"class": "date"})
pubdate = pubdate_elem.get_text().strip()[:4]

print(f"isbn: {isbn}")
print(f"가격: {org_price}")
print(f"서명: {title}")
print(f"저자: {author}")
print(f"출판사: {publisher}")
print(f"출판년: {pubdate}")
