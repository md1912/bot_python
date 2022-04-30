from bs4 import BeautifulSoup
import requests

URL = "https://animekisa.tv/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0"
}


def get_requests(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html,  "html.parser")
    items = soup.find_all("div", class_='episode-box test')
    anime = []

    for item in items:
        anime.append(
            {
                "link": URL + item.find("a", class_='an').get("href"),
                # "title": item.find("div", class_="title-box-2").get_text(),
                # "image": URL + item.find("div", class_="image-box").find("img").get("src")
            }
        )
    return anime[0].values()


def scrapy_script():
    html = get_requests(URL)
    if html.status_code == 200:
        anime = []
        for page in range(0, 10):
            html = get_requests(f"https://animekisa.tv/latest/{page}")
            anime.extend(get_data(html.text))
        return anime
    else:
        raise Exception("Error in scrapy script function")