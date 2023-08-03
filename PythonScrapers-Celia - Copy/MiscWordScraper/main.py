import requests
from bs4 import BeautifulSoup
import csv

def scrape_words_from_tables(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            tables = soup.find_all('table')  # Find all the tables on the page

            all_words = []
            for table in tables:
                tbody = table.find('tbody')  # Find the tbody element containing the data

                # Find all the <p> tags within the tbody
                paragraphs = tbody.find_all('p')

                # Extract the text from the <p> tags and store them in a list
                words = [p.get_text() for p in paragraphs]

                stopwords = ['\xa0']
                for word in list(words):  # iterating on a copy since removing will mess things up
                    if word in stopwords:
                        words.remove(word)

                all_words.extend(words)

            return all_words
        else:
            print(f"Failed to fetch the page. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error during request: {e}")
        return None

def scrape_bullet_points(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            div_elements = soup.find_all('div', class_='two_columns')

            all_bullet_points = []
            for div_element in div_elements:
                li_elements = div_element.find_all('li')
                bullet_points = [li.get_text().strip() for li in li_elements]
                all_bullet_points.extend(bullet_points)

            return all_bullet_points
        else:
            print(f"Failed to fetch the page. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error during request: {e}")
        return None

def save_to_csv(filename, data):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Words'])
        for word in data:
            csv_writer.writerow([word])

if __name__ == "__main__":
    url_1 = "https://zety.com/blog/resume-action-words"
    words_in_p_tags = scrape_words_from_tables(url_1)
    if words_in_p_tags:
        print("Words in <p> tags inside all tables:")
        print(words_in_p_tags)

    url_2 = "https://www.jobscan.co/blog/top-resume-keywords-boost-resume/"
    bullet_points = scrape_bullet_points(url_2)
    if bullet_points:
        print("\nBullet points from all <div> elements with class 'two_columns':")
        for point in bullet_points:
            print(point)

    # Combine the words from both scrapers and save to CSV
    combined_words = words_in_p_tags + bullet_points
    save_to_csv('combined_words.csv', combined_words)
    print("\nWords saved to 'combined_words.csv'.")
