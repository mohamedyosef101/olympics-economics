import requests
from bs4 import BeautifulSoup
import csv

def scrape_html_table(url, table_id, csv_filename):
    """Scrapes an HTML table and saves it as a CSV file.

    Args:
        url: The URL of the HTML page containing the table.
        table_id: The ID of the HTML table to scrape.
        csv_filename: The name of the CSV file to save the table data.
    """

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', id=table_id)

    if table:
        headers = [th.text.strip() for th in table.find_all('th')]
        data = []
        for row in table.find_all('tr'):
            cols = [td.text.strip() for td in row.find_all('td')]
            data.append(cols)

        with open(csv_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(data)

        print(f"Table data from {url} saved to {csv_filename}")
    else:
        print(f"Table with ID {table_id} not found on {url}")

# Example usage
url = "https://www.iban.com/country-codes"
table_id = "myTable"
csv_filename = "codes_table.csv"

scrape_html_table(url, table_id, csv_filename)