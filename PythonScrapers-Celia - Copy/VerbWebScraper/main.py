import csv
import requests
from bs4 import BeautifulSoup

# List of URLs to scrape
urls = [
    "https://verbs.colorado.edu/verb-index/index/A.php",
    "https://verbs.colorado.edu/verb-index/index/B.php",
    "https://verbs.colorado.edu/verb-index/index/C.php",
    "https://verbs.colorado.edu/verb-index/index/D.php",
    "https://verbs.colorado.edu/verb-index/index/E.php",
    "https://verbs.colorado.edu/verb-index/index/F.php",
    "https://verbs.colorado.edu/verb-index/index/G.php",
    "https://verbs.colorado.edu/verb-index/index/H.php",
    "https://verbs.colorado.edu/verb-index/index/I.php",
    "https://verbs.colorado.edu/verb-index/index/J.php",
    "https://verbs.colorado.edu/verb-index/index/K.php",
    "https://verbs.colorado.edu/verb-index/index/L.php",
    "https://verbs.colorado.edu/verb-index/index/M.php",
    "https://verbs.colorado.edu/verb-index/index/N.php",
    "https://verbs.colorado.edu/verb-index/index/O.php",
    "https://verbs.colorado.edu/verb-index/index/P.php",
    "https://verbs.colorado.edu/verb-index/index/Q.php",
    "https://verbs.colorado.edu/verb-index/index/R.php",
    "https://verbs.colorado.edu/verb-index/index/S.php",
    "https://verbs.colorado.edu/verb-index/index/T.php",
    "https://verbs.colorado.edu/verb-index/index/U.php",
    "https://verbs.colorado.edu/verb-index/index/V.php",
    "https://verbs.colorado.edu/verb-index/index/W.php",
    "https://verbs.colorado.edu/verb-index/index/Y.php",
    "https://verbs.colorado.edu/verb-index/index/Z.php"
]

# Create a CSV file to save the data
csv_filename = 'word_list.csv'

# Initialize a list to store the words for each URL
all_words = [[] for _ in urls]

# Scrape words from each URL
for url_idx, url in enumerate(urls):
    # Send a GET request to the website
    response = requests.get(url)

    # Create a BeautifulSoup object from the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <td> elements with the specified style attribute
    td_elements = soup.find_all('td', style='border-left: 1px #000000 solid;')

    # Extract the words from each <td> element
    words = [td.text.strip() for td in td_elements]

    # Exclude words ending with .n
    words = [word for word in words if not word.endswith('.n')]

    # Store the words in the respective URL index
    all_words[url_idx] = words

# Determine the maximum number of words among all URLs
max_words = max(len(words) for words in all_words)

# Create a list of rows for the CSV file
rows = [[''] + [url for url in urls]]

# Iterate over each word index
for word_idx in range(max_words):
    row = [word_idx + 1]  # Word index starts from 1

    # Iterate over each URL index
    for url_idx, words in enumerate(all_words):
        if word_idx < len(words):
            row.append(words[word_idx])
        else:
            row.append('')

    rows.append(row)

# Write the rows to the CSV file
with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(rows)

