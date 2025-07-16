# news_fetcher.py
import requests
import dotenv
import os
dotenv.load_dotenv()

def get_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",
        "apiKey": os.getenv('news_apiKey'),
        "pageSize": 5  
    }
    response = requests.get(url, params=params)
    articles = response.json().get("articles", [])
    if articles:
        news_list = []
        for article in articles:
            title = article.get("title", "No title")
            description = article.get("description", "No description")
            news_list.append(f"{title}: {description}")
        return "\n".join(news_list)
    else:
        return "No news available."
get_news()
if __name__ == "__main__":
    print(get_news())