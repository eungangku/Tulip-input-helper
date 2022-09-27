import requests
from bs4 import BeautifulSoup

# ISBN input
isbn_input = input(": ")
dash_removed = isbn_input.replace("-", "")
isbn_removed = dash_removed.replace("ISBN", "").replace("isbn", "")


def cut_after_blank(string):
    idx = string.index(" ", 6)
    if idx < 0:
        return string
    else:
        return string[:idx]


cut_blank = cut_after_blank(isbn_removed)
max_to_thirteen = cut_blank[:13]

isbn = max_to_thirteen

# request book detail
res = requests.get(f"https://openapi.naver.com/v1/search/book.json?query={isbn}", headers={
    "X-Naver-Client-Id": "FJiPQVRjcKtIVoKPZLKO",
    "X-Naver-Client-Secret": "UkHhk7M0x2",
})
res.raise_for_status()

json = res.json()

title = json["items"][0]["title"]  # 서명
author = json["items"][0]["author"]  # 저자
publisher = json["items"][0]["publisher"]  # 출판사
pubdate = json["items"][0]["pubdate"][:4]  # 출판년
print(f"isbn: {isbn}")
print(f"서명: {title}")
print(f"저자: {author}")
print(f"출판사: {publisher}")
print(f"출판년: {pubdate}")

res = requests.get(f"https://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode={isbn}")
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
org_price_elem = soup.find("span", attrs={"class": "org_price"})
org_price = org_price_elem.get_text().replace(",", "").replace("원", "").strip()
print(f"가격: {org_price}")
