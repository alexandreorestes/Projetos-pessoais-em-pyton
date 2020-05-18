from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Digite a URL de um espaço e aperte enter: ')
html = urlopen(url)
bs = BeautifulSoup(html)

cifra = bs.find_all('pre')
covert_cifra = str(cifra[0])


with open('copia_de-cifra.txt', 'w' ) as arquivo:
    arquivo.write('<div align="left"><button type="button" onclick="baixar()">- ½</button><button onclick="location.reload()"> Tom </button><button type="button" onclick="subir()">+ ½</button></div>\n')
    for linhas in covert_cifra:
        arquivo.write(linhas)
    arquivo.write('\n\n<script src="/wp-admin/js/transpor.js"></script>')

