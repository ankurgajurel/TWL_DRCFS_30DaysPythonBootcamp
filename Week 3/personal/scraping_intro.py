import requests as req
from bs4 import BeautifulSoup

def send_req(web_url: str) -> str:
    return req.get(web_url).text

def parse_html_str(html_str: str) -> BeautifulSoup:
    return BeautifulSoup(html_str, 'html.parser')

def fetch_current_bs_date(parsed_html: BeautifulSoup) -> str:
    top_elem = parsed_html.find(id="top")
    data_elem = top_elem.find("div", class_="date")
    current_date = data_elem.span.string.removeprefix('\n')
    return current_date.string

def main(website):
    html_str = send_req(website)
    parsed_html = parse_html_str(html_str)

    current_date = fetch_current_bs_date(parsed_html)
    print(f"current date is: {current_date}")

web_url = "https://hamropatro.com/"
main(web_url)