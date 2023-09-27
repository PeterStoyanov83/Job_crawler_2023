import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def fetch_job_portals(search_engine_url, query_param, headers):
    job_portals = []
    soup = None
    r = requests.get(search_engine_url + query_param, headers=headers)

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all('a'):
            url = link.get('href')
            text = link.text
            if url and "jobs" in url:
                parsed_uri = urlparse(url)
                domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
                job_portals.append([domain, text])

    return job_portals, r.status_code, soup


if __name__ == "__main__":
    search_engine_url = 'https://duckduckgo.com/html/?q='  # DuckDuckGo URL
    query_param = 'job+portals+in+Switzerland'
    excel_file = 'job_portals.xlsx'

    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }

    while True:
        print("Fetching job portal listings...")

        for i in range(3):  # Retry logic
            job_portal_list, status_code, soup = fetch_job_portals(search_engine_url, query_param, headers)
            if status_code == 200:
                break
            else:
                print(f"Attempt {i + 1} failed with status code {status_code}. Retrying...")
                time.sleep(10)

        print(f"HTTP Status Code: {status_code}")

        if soup:
            print(f"HTML Content: {soup.prettify()}")

        print(f"Fetched URLs: {job_portal_list}")

        if job_portal_list:  # Only export if list is not empty
            df = pd.DataFrame(job_portal_list, columns=['link', 'Description'])  # Changed 'URL' to 'link'
            df.to_excel(excel_file, index=False)

        print(f"Data exported to {excel_file}")

        time.sleep(24 * 60 * 60)  # Wait 24 hours before the next crawl
