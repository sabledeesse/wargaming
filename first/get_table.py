import pytest
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass

@dataclass
class WebsiteData:
    name: str
    frontend: str
    backend: str
    visitors_per_month: int

# Функция для извлечения данных из таблицы
def fetch_website_data():
    url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})
    if not table:
        raise ValueError("Cannot find the required table on the webpage.")

    rows = table.find_all('tr')[1:]
    data = []
    for row in rows:
        cols = [col.text.strip() for col in row.find_all('td')]
        if len(cols) >= 4:
            name = cols[0]
            visitors_str = cols[1].replace(",", "").split()[0]  # Удаляем запятые и берем число
            frontend = cols[2]
            backend = cols[3]
            try:
                visitors = int(visitors_str)
                data.append(WebsiteData(name=name, frontend=frontend, backend=backend, visitors_per_month=visitors))
            except ValueError:
                continue
    return data

@pytest.mark.parametrize("min_visitors", [10**7, 1.5 * 10**7, 5 * 10**7, 10**8, 5 * 10**8, 10**9, 1.5 * 10**9])
def test_website_popularity(min_visitors):
    data = fetch_website_data()
    for entry in data:
        assert entry.visitors_per_month > min_visitors, \
            f"{entry.name} (Frontend:{entry.frontend} | Backend:{entry.backend}) " \
            f"has {entry.visitors_per_month} unique visitors per month. (Expected more than {min_visitors})"
