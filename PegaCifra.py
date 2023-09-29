from bs4 import BeautifulSoup
from urllib.request import urlopen
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

continuar = True

while continuar:
    url = input('Digite a URL de um espaço e aperte enter (ou digite "q" para sair): ')
    
    if url == 'q':
        continuar = False
        break
    
    html = urlopen(url)
    bs = BeautifulSoup(html)

    cifra = bs.find_all('pre')
    titulo = bs.find('title')
    titulo_novo = titulo.text[:-12] + "- Cifra Simplificada"

    covert_cifra = str(cifra[0]) 

    with open('copia_de-cifra.txt', 'w' ) as arquivo:
        arquivo.write('<div class="col-sm-4"><div class="btn-group" role="group"><button type="button" style="border-radius:10%; background-color:blue; color:white; border:none;" onclick="baixar()">-</button><button style="border-radius:10%; background-color:blue; color:white; border:none;" onclick="location.reload()">½</button><button type="button" style="border-radius:10%; background-color:blue; color:white; border:none;" onclick="subir()">+</button></div></div><br>')
        for linhas in covert_cifra:
            arquivo.write(linhas)
        arquivo.write('\n\n<script src="/wp-admin/js/transpor.js"></script>')

    with open('copia_de-cifra.txt', 'r') as arquivo:
        conteudo = arquivo.read()

    url_wp = 'https://worldmusic.mus.br/xmlrpc.php'
    username = 'World Music'
    password = 'LB75S87xuNDVDdf'

    wp = Client(url_wp, username, password)

    post = WordPressPost()
    post.title = titulo_novo
    post.content = conteudo
    post.post_type = 'post'
    post.post_status = 'publish'
    post.categories = ['Cifra', 'World Music']
    
    response = wp.call(NewPost(post))

    print("Post publicado com sucesso!")
