from bs4 import BeautifulSoup
import requests
from requests import get

#url = 'https://www.netflix.com/ar/title/80192098'
url = 'https://www.netflix.com/ar/title/80134797'
request = get(url)
soup = BeautifulSoup(request.text, 'html.parser')
############################################### ###############################################################

# Temporadas y capitulos
temps_y_caps = soup.find(id="seasons-and-episodes-list-container") 

# Temporadas
temps= temps_y_caps.find_all('div', {'class': ['season season-active','season']})
contador_temp = 0                                            # setea un contador para calcular cantidad de temporadas


for temporada in temps:                                       # por cada temporada en temporadas busca la lista de cap correspondientes
    contador_temp =contador_temp+1
    temporada = temps.find_all('div', class__ ='season-release-year')
    caps = temporada.find_all('div', class_ = 'episode') 
    contador_cap =0

    print( " temp: " +str(contador_temp))
    
    for capitulo in caps:
        contador_cap = contador_cap+1
        capitulo= caps.find('div', class__ ='episode-metadata')
        capi_titulo = capitulo.find('h3', class_ ='episode-title')
        
        print(capi_titulo.text)
        print( " cap:   " +str(contador_cap) + " temporada:" +str(contador_temp))


print( "total de cap: " +str(contador_cap))
print( "total de temp: " +str(contador_temp))
'''
for resultado in busc_capitulos:
    
    cap_cabecera = resultado.find("h3", class_="episode-title")  
    año_estr = cap_cabecera.a
    
    #print(cap_cabecera.text)

    cont = cont +1
'''
#temp = soup.find('div', class_ ='season-release-year')
#print(temps.text)
