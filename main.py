from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_India'

try:
    # Send a GET request to fetch the raw HTML content
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
except requests.RequestException as e:
    print(f"Error fetching the URL: {e}")
    exit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the data
tables = soup.find_all('table', {'class': 'wikitable'})
if len(tables) < 1:
    print("No tables found on the page.")
    exit()

table = tables[1]  # Assuming the second table is the one we need

# Extract column headers
top_titles = table.find_all('th')
top_table_titles = [titles.text.strip() for titles in top_titles]

# Create a DataFrame with the column headers
df = pd.DataFrame(columns=top_table_titles)

# Extract row data
column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    # Ensure the row data matches the number of columns
    if len(individual_row_data) == len(top_table_titles):
        df.loc[len(df)] = individual_row_data
    else:
        print("Row data length does not match column length. Skipping row.")

# Save DataFrame to a CSV file (optional)
df.to_csv(r'your_custom_path.csv', index=False)

print("Data extraction complete. Data saved to 'largest_companies_in_india.csv'.")
