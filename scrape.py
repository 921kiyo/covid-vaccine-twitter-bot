import requests
import bs4
import urllib.request


def get_page_contents(url):
    page = requests.get(url, headers={"Accept-Language": "en-US,en;q=0.9"})
    return bs4.BeautifulSoup(page.content, "html.parser")


def extract_total_num():
    url = "https://github.com/owid/covid-19-data/blob/master/public/data/vaccinations/country_data/Japan.csv"
    soup = get_page_contents(url)
    table = soup.find("table")

    last_row = table("tr")[-1]
    people_vaccinated = last_row("td")[-2].text
    people_fully_vaccinated = last_row("td")[-1].text
    collect_date = last_row("td")[2].text

    second_last_row = table("tr")[-2]
    people_vaccinated_previous = second_last_row("td")[-2].text
    people_fully_vaccinated_previous = second_last_row("td")[-1].text
    return (
        int(people_vaccinated),
        int(people_vaccinated) - int(people_vaccinated_previous),
        int(people_fully_vaccinated),
        int(people_fully_vaccinated) - int(people_fully_vaccinated_previous),
        collect_date,
    )
