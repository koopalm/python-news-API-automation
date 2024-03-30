import requests
import sys

API_KEY = 'YOUR-API-KEY-HERE'

URL = ('https://newsapi.org/v2/top-headlines?')


def get_articles_by_category(category):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "gb",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def get_articles_by_query(query):
    query_parameters = {
        "q": query,
        "sortBy": "top",
        "country": "gb",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def _get_articles(params):
    response = requests.get(URL, params=params)

    articles = response.json()['articles']

    results = []
        
    for article in articles:
        results.append({"title": article["title"], "url": article["url"]})

    for result in results:
        print(result['title'])
        print(result['url'])
        print('')

def get_sources_by_category(category):
    url = 'https://newsapi.org/v2/top-headlines/sources'
    query_parameters = {
        "category": category,
        "language": "en",
        "apiKey": API_KEY
    }

    response = requests.get(url, params=query_parameters)

    sources = response.json()['sources']

    for source in sources:
        print(source['name'])
        print(source['url'])

# Function to get the 'news your-category' command to work
def main():
    if len(sys.argv) != 2:
        print("Usage: python news_automator.py <category>")
        return
    
    category = sys.argv[1]
    get_articles_by_category(category)

if __name__ == "__main__":
    main()

# Alternatively run this and comment out the 'def main()' function
# if __name__ == "__main__":
#     get_articles_by_category("health")
#     # get_articles_by_query("Dolly")
#     # get_sources_by_category("technology")