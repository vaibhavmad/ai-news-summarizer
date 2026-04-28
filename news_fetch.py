import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('NEWS_API_KEY')

URL = ("https://gnews.io/api/v4/search?"
       "q=iphone"
       f"&lang=en&apikey={API_KEY}"
       )

def get_news():
    url = URL
    response = requests.get(url, timeout=10)
    data = response.json()

    if response.status_code != 200:
        print("API request failed")
    else:
        articles = data['articles']
        article_list = []
        for index, article in enumerate(articles):
            article_title = f"{index + 1}. {article['title']}"
            article_description = article['description']
            complete_article = article_title + '\n' + article_description + '\n\n'
            article_list.append(complete_article)

        article_text = ''
        for article in article_list:
            article_text += article + '\n'

        return article_text
