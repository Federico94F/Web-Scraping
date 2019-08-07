from bs4 import BeautifulSoup
import requests
from requests import get

url = 'https://www.netflix.com/ar/title/80134797'   
request = get(url)
soup = BeautifulSoup(request.text, 'html.parser')


temporadas = soup.find_all('div', class_ = 'season')

cont = 0
cont_cap = 0
Cant_cap= 0

for resultado in temporadas:
       
    cont = cont +1 #contador de temporadas
    
    capitulos = resultado.find_all('div', class_ = 'episode')
    cont_cap = 0  # contador de capitulos

    for capitulo in capitulos:

        cont_cap = cont_cap +1 # contador de capitulos sumando

        
    print("La temporada: " + str(cont) +" tiene "+str(cont_cap)+" capitulos")            
    Cant_cap = cont_cap + Cant_cap

    #cap_totales = cap_totales + Cant_cap


print("Hay en total: " + str(Cant_cap)+ " capitulos.")


    

    


    
    


Cabecera = soup.find('div', class_ = 'title-info')
Titulo = Cabecera.h1
genero = Cabecera.a
Estreno = Cabecera.span
temporadas = Cabecera.find(class_="test_dur_str")
