import requests
from bs4 import BeautifulSoup
from requests import get

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree

url = 'https://www.imdb.com/title/tt1520211/?ref_=nv_sr_1?ref_=nv_sr_1'

request = get(url)
soup    = BeautifulSoup(request.text, 'html.parser')

#Titulo
titulo_wrapper = soup.find('div', class_ = 'title_wrapper')
Titulo = titulo_wrapper.h1

#Sinopsis
sinopsis_w = soup.find('div', class_ = 'summary_text')
sinopsis = sinopsis_w.text

#Temporadas
temporadas_w = soup.find('div', class_ = 'seasons-and-year-nav')
temporadas= temporadas_w.a.text

#Capitulos
capitulos_wrapper = soup.find('div', class_ = 'bp_description')
capitulos = capitulos_wrapper.find('span', class_ = 'bp_sub_heading')

###############################################################################################
root=Element('Serie')
tree=ElementTree(root)


titlo = Element('Titulo')
sinsis = Element('sinopsis')
tempdas = Element('temporadas')
caps = Element('capitulos')

root.append(titlo)
root.append(sinsis)
root.append(tempdas)
root.append(caps)

titlo.text = Titulo.text
sinsis.text = sinopsis
caps.text = capitulos.text
tempdas.text = temporadas

root.set('id','001')
tree.write('TheWalkingDead_IMDB.xml')

#print(etree.tostring(root))