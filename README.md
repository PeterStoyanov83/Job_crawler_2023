# Web Scraping Job Portals in Switzerland 🇨🇭

## 📌 Overview

This Python script is designed to scrape DuckDuckGo's search results for job portals in Switzerland. It captures relevant links and descriptions, saves them to an Excel file, and then waits for 24 hours before the next crawl.

## 📦 Dependencies

- Python 3.x
- `requests`
- `BeautifulSoup`
- `pandas`

To install all dependencies, run:
```bash
pip install requests beautifulsoup4 pandas
```


## 🛠 How it Works

### Main Components

1. **`fetch_job_portals(search_engine_url, query_param, headers)`**: A function designed to fetch job portal data.
2. **Retry Logic**: Handles unsuccessful HTTP requests and retries.
3. **Data Export**: Uses Pandas to save scraped job portal URLs into an Excel file.
4. **Scheduler**: Pauses for 24 hours before the next scraping cycle.

### Steps

1. The DuckDuckGo HTML search results page is used to scrape data.
2. An HTTP GET request is made to fetch search results for the query `'job+portals+in+Switzerland'`.
3. All anchor tags (`<a>`) from the HTML are parsed, and URLs containing the term "jobs" are identified.
4. Extracts and saves the domain of each job-related URL along with its link text.
5. If the HTTP request returns a non-200 status code, the script will retry up to 3 times.
6. Finally, the script saves the scraped data into an Excel file using Pandas.

### 📂 Output

- `job_portals.xlsx`: An Excel file featuring two columns—"link" and "Description"—that list the job portal URLs and their associated textual descriptions, respectively.

## 🚀 How to Run

1. **Clone the Repository**
    ```bash
    git clone <repository_link>
    ```

2. **Navigate to the Directory**
    ```bash
    cd <directory_name>
    ```

3. **Run the Script**
    ```bash
    python <script_name>.py
    ```

## ✨ Future Improvements

1. Proxy rotation to dodge IP bans.
2. Logging features to capture historical data.
3. Advanced error-handling mechanisms.

## ⚠️ Caution

Web scraping may violate the terms of service of some websites. Ensure you are aware of and respect DuckDuckGo's terms and policies before running this script.
