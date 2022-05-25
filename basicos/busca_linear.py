def busca_linear(lista, item):
    for i in range(len(lista)):
        if (item == lista[i]):
            return i
    return -1

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(busca_linear(lista, 2)) # Retorna 1
print(busca_linear(lista, 11)) # Retorna -1