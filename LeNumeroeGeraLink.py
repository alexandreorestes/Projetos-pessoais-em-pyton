arquivo = open('Lista.txt', 'rt')
for linha in arquivo:
    linha = linha.strip('\n')
    link = 'https://api.whatsapp.com/send?phone='+linha+'&text=Boa%20tarde!%20Aqui%20%C3%A9%20o%20Alexandre%20Prof%20de%20M%C3%BAsica!%20'
    with open('lista_pronta.txt', 'a') as arquivo:
        arquivo.write(link + '\n')
