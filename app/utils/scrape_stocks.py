import requests
from bs4 import BeautifulSoup



def get_stock_list():
    """
    Retrieves a list of company codes for stocks from the oyakyatirim.com.tr website.

    Returns:
        list: A list of company codes for stocks, with ".IS" appended to each code.
    """
    company_codes = []

    url = 'https://www.oyakyatirim.com.tr/piyasa-verileri/XUTUM'

    # Send a request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve the webpage from oyakyatirim.com.tr. Status code: {response.status_code} and response: {response}")

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Using the provided div class "portlet box green" to locate the table and then extract company codes from it
    # Find the div with the class "portlet box green"
    div_with_class = soup.find('div', class_='portlet box green')

    # Locating the table within this div
    if not div_with_class:
        return []

    found_table = div_with_class.find('table')

    # Extracting company codes from the located table
    if not found_table:
        return []

    rows = found_table.find_all('tr')

    if not rows:
        return []

    for row in rows:
        cells = row.find_all('td')

        if not cells:
            continue
        code = cells[0].get_text().strip()
        company_codes.append(code)

    # Add .IS to the end of each code
    company_codes = [code + ".IS" for code in company_codes]

    return company_codes

