import requests
from bs4 import BeautifulSoup
import csv

target_url = 'https://lenouvelliste.com'

def extract_article_data(article_url):
    response = requests.get(article_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        article_title = soup.find('h1').text
        article_image = soup.find('img')['src']
        article_description = soup.find('meta', {'name': 'description'})['content']
        
        return {'title': article_title, 'image': article_image, 'description': article_description, 'url': article_url}
    else:
        print(f"Erreur de requête HTTP : {response.status_code}")
        return None

def scrape_site():
    extracted_data = []
    main_page = requests.get(target_url)

    if main_page.status_code == 200:
        main_soup = BeautifulSoup(main_page.text, 'html.parser')
        article_links = [a['href'] for a in main_soup.find_all('a', {'class': 'article-link'})]

        for link in article_links:
            article_data = extract_article_data(link)
            
            if article_data:
                extracted_data.append(article_data)

        with open('news_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'image', 'description', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(extracted_data)
    else:
        print(f"Erreur de requête HTTP sur la page principale : {main_page.status_code}")

scrape_site()
