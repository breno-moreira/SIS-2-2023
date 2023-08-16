#01 - Dada a lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52] faça um programa que:
#a) imprima o maior elemento
#b) imprima o menor elemento
#c) imprima os números pares
#d) imprima o número de ocorrências do primeiro elemento da lista
#e) imprima a média dos elementos
#f) imprima a soma dos elementos de valor negativo

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
print("="*50)
# a) Maior elemento
maior = max(lista)
print("Maior elemento:", maior)
print("="*50)
# b) Menor elemento
menor = min(lista)
print("Menor elemento:", menor)
print("="*50)
# c) Números pares
pares = [num for num in lista if num % 2 == 0]
print("Números pares:", pares)
print("="*50)
# d) Número de ocorrências do primeiro elemento
primeiro_elemento = lista[0]
ocorrencias_primeiro = lista.count(primeiro_elemento)
print("Número de ocorrências do primeiro elemento:", ocorrencias_primeiro)
print("="*50)
# e) Média dos elementos
media = sum(lista) / len(lista)
print("Média dos elementos:", media)
print("="*50)
# f) Soma dos elementos de valor negativo
negativos = [num for num in lista if num < 0]
soma_negativos = sum(negativos)
print("Soma dos elementos de valor negativo:", soma_negativos)

print("="*50)