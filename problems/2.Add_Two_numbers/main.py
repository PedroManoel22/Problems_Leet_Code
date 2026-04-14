# São dadas duas listas ligadas não vazias representando dois números inteiros não negativos. Os dígitos estão armazenados em ordem inversa e cada um dos nós contém um único dígito. Some os dois números e retorne a soma como uma lista ligada.

# Você pode assumir que os dois números não contêm nenhum zero à esquerda, exceto o próprio número 0.

# Exemplo 1:

# Entrada: l1 = [2,4,3], l2 = [5,6,4]
#  Saída: [7,0,8]
#  Explicação: 342 + 465 = 807.
# Exemplo 2:

# Entrada: l1 = [0], l2 = [0]
#  Saída: [0]
# Exemplo 3:

# Entrada: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
#  Saída: [8,9,9,9,0,0,0,1]

def somar(nums1: list[int], num2: list[int]):
    nums1_str = ""
    num2_str = ""
    lista: list[int] = []

    for num in nums1:
        nums1_str += str(num)
    
    for num in num2:
        num2_str += str(num)
    
    soma = int(nums1_str) + int(num2_str)
    soma = str(soma)

    for i in range(len(soma)-1, -1, -1):
        lista.append(int(soma[i]))

    print(lista)
    

if __name__ == "__main__":
    # Exemplo 1
    l1 = [2,4,3]
    l2 = [5,6,4]
    somar(l1, l2)

    # Exemplo 2
    l1 = [0]
    l2 = [0]
    somar(l1, l2)

    # Exemplo 3
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]
    somar(l1, l2)
