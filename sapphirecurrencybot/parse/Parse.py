import requests
from bs4 import BeautifulSoup as BS

class Parse():
    def __init__(self, url):
        self.url = url
        self.values = []
        # запрос и получение html
        source = requests.get(self.url)
        self.html = BS(source.text, 'lxml')
    
    def get_content(self):
        table = self.html.find('table', {'class':'content_table with_department head_2_row'})
        tbody = table.find('tbody')
        
        for tr in tbody.find_all('tr', {'class':'tr-turn'}):
            td = tr.find_all('td')
            for value in td:
                if value.text != '':
                    self.values.append(value.text.lstrip())

        return self.values
    
    def get_all_banks_address(self):
        table = self.html.find('table', {'class':'content_table with_department head_2_row'})
        tbody = table.find('tbody')
        
        for tr in tbody.find_all('tr', {'class':'hidden-info-block'}):
            td = tr.find_all('td', {'class':''})
            for value in td:
                if value.text != '':
                    self.values.append(value.text.lstrip())
        for i in range(len(self.values)):
            if '\xa0' in self.values[i]:
                self.values[i] = self.values[i].replace('\xa0', ' ')

        return self.values