Web Scraper for Largest Companies in India from Wikipedia
=========================================================

This Python script scrapes data from a Wikipedia page that lists the largest companies in India and saves the extracted data into a CSV file.

Requirements
------------

Ensure you have the following Python libraries installed before running the script:

*   `requests`
*   `beautifulsoup4`
*   `pandas`

You can install these libraries using `pip`:

```
pip install requests beautifulsoup4 pandas
```

How It Works
------------

The script performs the following steps:

1.  **Fetch HTML Data:** The script sends an HTTP GET request to the Wikipedia page to retrieve the HTML content.
2.  **Parse HTML:** It uses BeautifulSoup to parse the raw HTML content and locate the relevant table containing the list of the largest companies in India.
3.  **Extract Table Data:** The script extracts the column headers and rows from the table and organizes them into a Pandas DataFrame.
4.  **Save Data:** The resulting DataFrame is saved as a CSV file to the specified directory on your computer.

Usage
-----

1.  Clone or download this script.
2.  Open the script in your preferred IDE or text editor.
3.  Run the script with Python:

```
python scraper.py
```

### Customizing the Output Path

If you want to customize the output file path, you can change the `df.to_csv` line in the script:

```python
df.to_csv('your_custom_path.csv', index=False)
```

Example
-------

Here's an example of how the script can be executed:

```
python scraper.py
```

Output:

```
Data extraction complete. Data saved to 'largest_companies_in_india.csv'.
```

Error Handling
--------------

*   The script includes error handling for network issues when fetching the Wikipedia page.
*   It also checks if the required table is found on the page. If not, the script will exit with a message indicating the problem.
*   The script skips rows where the number of columns does not match the expected headers.

Notes
-----

*   This script assumes the desired table is the second one (`tables[1]`) on the Wikipedia page. If the structure of the page changes, you may need to adjust the table selection logic.
*   Make sure the specified output directory exists before running the script.

License
-------

This project is open-source and available under the MIT License.

* * *

This README gives a clear overview of your script's purpose, its usage, and what users can expect from it. Adjust the paths and instructions as needed to fit your specific requirements.