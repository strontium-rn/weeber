import requests
from bs4 import BeautifulSoup

url = 'https://www.onlinekhabar.com/'
response = requests.get(url)
print("Status Code:", response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    containers = soup.find_all('div', class_='ok-container')

    with open('scrapped_titles.txt', 'w', encoding='utf-8') as file:  # Specify UTF-8 encoding
        for container in containers:
            articles = container.find_all('h2')
            for article in articles:
                title = article.get_text().strip()
                link_tag = article.find('a')
                if link_tag:  # Check if the <a> tag exists
                    link = link_tag['href']
                    file.write(f"Title: {title}\nURL: {link}\n\n")
                    print(f"Title: {title}\nURL: {link}\n")
                else:
                    print(f"Title: {title} (No link found)\n")
else:
    print("Failed to retrieve the website")
