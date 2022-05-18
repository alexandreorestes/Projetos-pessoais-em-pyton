arquivo = open('Lista2.txt', 'r')
for numero in range(350):
    numero = arquivo.readline()
    pre_link = 'https://wa.me/'
    link = pre_link + numero
    print(link)



