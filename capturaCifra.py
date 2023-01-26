
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Digite a URL de um espaço e aperte enter: ')
html = urlopen(url)
bs = BeautifulSoup(html)

cifra = bs.find_all('pre')
# video = bs.find_all('div class="player-embed"')
covert_cifra = str(cifra[0])




with open('copia_de-cifra.txt', 'w' ) as arquivo:
    arquivo.write('<div class="container"><div class="row"><div class="col-sm-8"><iframe width="360" height="200" src="VIDEO_EMBEDADO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></div><div class="col-sm-4">Transpor<div class="btn-group" role="group"><button type="button" style="border-radius:10%; background-color:blue; color:white; border:none;" onclick="baixar()">-</button><button style="border-radius:10%; background-color:blue; color:white; border:none;" onclick="location.reload()">½</button><button type="button" style="border-radius:10%; background-color:blue; color:white; border:none;" onclick="subir()">+</button></div></div>\n')
    for linhas in covert_cifra:
        arquivo.write(linhas)
    arquivo.write('\n\n<script src="/wp-admin/js/transpor.js"></script>')

