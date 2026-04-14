# Dados dois arrays ordenados nums1, A e B, nums2de tamanhos mn e n-ésimo, nrespectivamente, retorne a mediana dos dois arrays ordenados.

# A complexidade de tempo de execução geral deve ser de O(log (m+n)).

 

# Exemplo 1:

# Entrada: nums1 = [1,3], nums2 = [2]
#  Saída: 2.00000
#  Explicação: matriz mesclada = [1,2,3] e a mediana é 2.
# Exemplo 2:

# Entrada: nums1 = [1,2], nums2 = [3,4]
#  Saída: 2.50000
#  Explicação: array mesclado = [1,2,3,4] e a mediana é (2 + 3) / 2 = 2,5.

import numpy as np

def mediana(nums1: list[int], nums2: list[int]):
    nums = nums1 + nums2
    media = np.mean(nums)
    print(media)

if __name__ == "__main__":
    # Exemplo 1:
    nums1 = [1,3]
    nums2 = [2]
    mediana(nums1, nums2)

    # Exemplo 2:
    nums1 = [1,2]
    nums2 = [3,4]
    mediana(nums1, nums2)


