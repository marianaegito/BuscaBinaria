# Lista original
Lista = [10, 9, 4, 2, 18, 16, 15]

# Ordenando a lista (busca binária só funciona ordenada)
Lista.sort()

print("Lista ordenada:", Lista)

# Alvo que queremos encontrar
alvo = 18

l = 0
h = len(Lista) - 1

Iteracao = 0

while l <= h:
    m = (l + h) // 2
    print("\nIteração:", Iteracao)
    print("l =", l, "| h =", h, "| m =", m)
    print("O valor no meio:", Lista[m])

    if Lista[m] == alvo:
        print("\nÍndice encontrado:", m)
        break
    elif Lista[m] < alvo:
        l = m + 1
    else:
        h = m - 1

    Iteracao += 1


def buscaBinaria(lista, alvo):
    l = 0
    h = len(lista) - 1
    iteracao = 0
    
    while l <= h:
        m = (l + h) // 2
        l = m + 1
        print(f"Iteração {iteracao}: l{l}, h{h}, m{m}")
        if lista[m] == alvo:
            return m
        elif lista[m] < alvo:
             l = m + 1 
        else:
            h = m - 1 
    return -100
lista1 = [11, 17, 18, 45, 50, 71, 95]
target = 50
resultado = buscaBinaria(lista1, target)

print(f"Indice do alvo: {resultado}")