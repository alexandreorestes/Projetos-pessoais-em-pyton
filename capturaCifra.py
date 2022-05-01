from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Digite a URL de um espaço e aperte enter: ')
html = urlopen(url)
bs = BeautifulSoup(html)

cifra = bs.find_all('pre')
covert_cifra = str(cifra[0])


with open('copia_de-cifra.txt', 'w' ) as arquivo:
    arquivo.write('<div class="container"><div class="row"><div class="col-sm-8"><iframe width="360" height="200" src=" " frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></div><div class="col-sm-4">Transpor<div class="btn-group" role="group"><button type="button" onclick="baixar()">-</button><button onclick="location.reload()">½</button><button type="button" onclick="subir()">+</button></div></div></div></div>\n')
    for linhas in covert_cifra:
        arquivo.write(linhas)
    arquivo.write('\n\n<script src="/wp-admin/js/transpor.js"></script>')

