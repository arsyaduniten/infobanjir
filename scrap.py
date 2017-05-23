import requests
from bs4 import BeautifulSoup


page = requests.get("http://publicinfobanjir.water.gov.my/View/OnlineFloodInfo/PublicWaterLevel.aspx?scode=WLH")
soup = BeautifulSoup(page.content, 'html.parser')
spans = soup.find_all('span')
