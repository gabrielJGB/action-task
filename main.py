import requests
import bs4
from pathlib import Path

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'}
link = "https://es.wikipedia.org/wiki/Primera_Division_de_Argentina"
res = requests.get(link,headers=headers)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
data = soup.select("#mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(21) > td > a")[0].text
contenido = "{\"campeon\":\" %s \"}" %(data)
ruta = Path(__file__).parent.resolve().joinpath('datos.json')
archivo = open(ruta,'w',encoding='utf-8')
archivo.write(contenido)
archivo.close()






