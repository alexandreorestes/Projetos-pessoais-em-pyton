import datetime

def menu():
    print('>>>EMISSÃO DE RECIBO COMERCIAL<<<')
    print('1 - Emitir recibo')

def recibo():
    data = datetime.datetime.now()
    data_de_hoje = data.day,data.month,data.year
    print('>>>Por favor informe os seguintes dados para a emissão do recibo<<<')
    nome = input('Qual o nome do cliente: ')
    cpf = input('Qual o cpf: ')
    email = input('Qual o email: ')
    endereco = input('Qual o endereço: ')
    valor = input('Qual é o valor do recibo: ')
    aula1 = input('Qual o dia da aula 1: ')
    aula2 = input('Qual o dia da aula 2: ')
    aula3 = input('Qual o dia da aula 3: ')
    aula4 = input('Qual o dia da aula 4: ')


    print('\n>>>RECIBO COMERCIAL<<<')
    print('>>>ALEXANDRE | AULAS DE MÚSICA<<<')
    print('\nUberlandia', data_de_hoje, '             Valor: R$ ', valor,'\n')
    print('Recebi do(a) Senhor(a): \n', nome,', CPF: ',cpf, ', Email: ', email)
    print('Residente na: ', endereco, '\no valor de: ',valor, 'Reais referente às')
    print('aulas de musica a serem realizadas nos dias: ')
    print(aula1,',', aula2,',', aula3,',', aula4)
#COMEÇO DO PROGRAMA
menu()
opcao = input('Escolha uma opção: ')
if opcao == '1':
    recibo()
