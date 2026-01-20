import requests
from urllib.parse import quote
from scraper import WebScraper

class SearchEngine:
    
    def __init__(self):
        self.scraper = WebScraper()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def search(self, query, engine='google', num_results=5):
        if engine == 'google':
            return self._search_google(query, num_results)
        elif engine == 'duckduckgo':
            return self._search_duckduckgo(query, num_results)
        else:
            return []
    
    def _search_google(self, query, num_results=5):
        try:
            url = f"https://www.google.com/search?q={quote(query)}&num={num_results}"
            response = self.session.get(url, timeout=10)
            results = self.scraper.parse_google_results(response.text)
            return results[:num_results]
        except Exception as e:
            print(f"Gabim kërkimi në Google: {e}")
            return []
    
    def _search_duckduckgo(self, query, num_results=5):
        try:
            url = f"https://duckduckgo.com/?q={quote(query)}"
            response = self.session.get(url, timeout=10)
            results = self.scraper.parse_duckduckgo_results(response.text)
            return results[:num_results]
        except Exception as e:
            print(f"Gabim kërkimi në DuckDuckGo: {e}")
            return []
