
pre_link = 'https://wa.me/'
fone = input('>>>ATENÇÃO<<<\nDigite o número inicial da sequência a ser gerada \nseguindo o modelo de 13 Digitos\n(PAIS)(DDD)(NÚMERO DE 9 DIGITOS) EX:(5534988980000): ')
fone = int(fone)
quantidade = input('Quantos numeros você gostaria de gerar: ')
quantidade = int(quantidade)
for x in range(quantidade):
    numero = fone + x
    numero = str(numero)
    resultado = pre_link + numero
    with open('lista_pronta.txt', 'a') as arquivo:
        arquivo.write(resultado + '\n')


