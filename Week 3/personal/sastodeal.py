import bs4
import requests as req
from datetime import datetime

def request_site(web_url: str) -> str:
    return req.get(web_url, timeout=100).text

def parse_html(normal_html_str: str) -> bs4.BeautifulSoup:
    return bs4.BeautifulSoup(normal_html_str, "html.parser")

def get_price_from_soup(soup: bs4.BeautifulSoup) -> str:
    price_element = soup.find('span', class_="price-wrapper")
    npr = price_element.span.string[3:]

    return npr

def write_price_to_file(price: str, filename: str) -> None:
    current_time = datetime.now()
    time_str = current_time.strftime("%Y-%m-%d")
    with open(filename, mode="a") as f:
        f.write(price)

def main():
    web_url = 'https://www.sastodeal.com/deviser-l560-70-acoustic-guitar-with-cover-sd-10-mp-58.html'
    file_path = 'price.txt'
    html_str = request_site(web_url)
    soup = parse_html(html_str)

    price = get_price_from_soup(soup)

    write_price_to_file(price, file_path)


if __name__ == "__main__":
    main()