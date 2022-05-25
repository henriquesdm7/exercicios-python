def busca_binaria(lista, item, pos_inicial = False, pos_final = False):    
    if (pos_inicial == False):
        pos_inicial = 0
    if (pos_final == False):
        pos_final = len(lista) - 1
    
    if (item > lista[pos_final] or item < lista[pos_inicial]):
        return -1
    
    meio = pos_inicial + int((pos_final-pos_inicial)/2)
    
    if (int(item) < int(lista[meio])):
        # print(f"{item} is smaller than {lista[meio]}")
        # print(lista[pos_inicial:pos_final+1])
        return busca_binaria(lista, item, pos_inicial, meio)
    if (int(item) > int(lista[meio])):
        # print(f"{item} is bigger than {lista[meio]}")
        # print(f"{lista[pos_inicial:(pos_final+1)]} POS INICIAL: {pos_inicial} POS FINAL: {pos_final+1}")
        return busca_binaria(lista, item, meio, pos_final)
    if (int(item) == int(lista[meio])):
        # print(f"{item} is equal to {lista[meio]}")
        # print(lista[pos_inicial:pos_final+1])
        return meio
    # print(f"{item} is not in the list")
    return -1

integer_ordered_list = list(range(835,1561))
number_to_find = 986

result = busca_binaria(integer_ordered_list, number_to_find)
if (result != -1):
    print(f"\n{'-'*50}\nNúmero {number_to_find} na posição {result}: {integer_ordered_list[result]}\n{'-'*50}\n")
else:
    print(f"\n{'-'*50}\nNúmero {number_to_find} não encontrado na lista.\n{'-'*50}\n")