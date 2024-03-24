## ATIVIDADE 1
lista = [1, 2, 3, 4]
def pares(lista: list):
    lista2 = []
    for number in lista:
        if number % 2 == 0:
            lista2.append(number*2)
    return lista2
print(pares(lista))

## ATIVIDADE 4

import json

abacate = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

def produtoVendido(vendas: list, produtos: dict):    
    for venda in vendas:
        produtos[venda['productID']] += venda['price'] * venda['quantity']
    
    maior = 0
    nomeproduto = 0
    for idProduto, total in produtos.items():
        if total > maior:
            maior = total
            nomeproduto = idProduto
    return nomeproduto

with open("teste.json", "r") as dados:
    lines = json.load(dados)
    print(produtoVendido(lines, abacate))