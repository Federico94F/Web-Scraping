from bs4 import BeautifulSoup
import requests
from requests import get

#url = 'https://www.netflix.com/ar/title/80192098'
url = 'https://www.netflix.com/ar/title/80134797'   
request = get(url)
soup = BeautifulSoup(request.text, 'html.parser')

busc_capitulos = soup.find_all('div', class_ = 'episode-metadata')

cont = 0

for resultado in busc_capitulos:
    
    cap_cabecera = resultado.find("h3", class_="episode-title")
    nomcap = cap_cabecera.a
    
    cont = cont +1
    print(cap_cabecera.text)

    


Cabecera = soup.find('div', class_ = 'title-info')
Titulo = Cabecera.h1
genero = Cabecera.a
Estreno = Cabecera.span
temporadas = Cabecera.find(class_="test_dur_str")
Cant_cap = cont

##############################################################################

print(' ')
print("Titulo: " +Titulo.text)
print("Año de estreno: " +Estreno.text)
print("Genero: " +genero.text)
print("Cantidad de temporadas: " +temporadas.text)
print("Cantidad total de capitulos: " +str(Cant_cap))
print(' ')
##############################################################################