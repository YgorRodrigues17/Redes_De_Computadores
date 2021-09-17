import csv

caminho = str(input('Digite o caminho do arquivo .csv:'))
ipv4 = str(input('Coloque o endereco IPv4:'))

arquivo = csv.reader(open(caminho),delimiter=';')
for linha in arquivo:
    if(ipv4 == linha[0]):
            print(linha[2])