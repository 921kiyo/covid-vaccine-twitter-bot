import requests
import bs4
import urllib.request

url = "https://coronavirus.data.gov.uk/details/vaccinations"

url = "https://github.com/owid/covid-19-data/blob/master/public/data/vaccinations/country_data/United%20Kingdom.csv"
url = "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/vaccine_sesshujisseki.html"


def get_page_contents(url):
    page = requests.get(url, headers={"Accept-Language": "en-US,en;q=0.9"})
    return bs4.BeautifulSoup(page.content, "html.parser")


soup = get_page_contents(url)

print(soup)
