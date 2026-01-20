from bs4 import BeautifulSoup

class WebScraper:
    
    def parse_google_results(self, html):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            results = []
            
            for result in soup.find_all('div', class_='g'):
                title_elem = result.find('h3')
                link_elem = result.find('a')
                desc_elem = result.find('div', class_='VwiC3b')
                
                if title_elem and link_elem:
                    results.append({
                        'title': title_elem.get_text(),
                        'link': link_elem.get('href', ''),
                        'description': desc_elem.get_text() if desc_elem else 'Nuk ka përshkrim'
                    })
            
            return results
        except Exception as e:
            print(f"Gabim analizimi në Google: {e}")
            return []
    
    def parse_duckduckgo_results(self, html):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            results = []
            
            for result in soup.find_all('article'):
                title_elem = result.find('h2')
                link_elem = result.find('a')
                desc_elem = result.find('div', class_='result__snippet')
                
                if title_elem and link_elem:
                    results.append({
                        'title': title_elem.get_text(),
                        'link': link_elem.get('href', ''),
                        'description': desc_elem.get_text() if desc_elem else 'Nuk ka përshkrim'
                    })
            
            return results
        except Exception as e:
            print(f"Gabim analizimi në DuckDuckGo: {e}")
            return []
