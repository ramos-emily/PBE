#insertionSort

# lista = [5, 2, 9, 1, 5, 6]


# for i in lista:
#     if i < proximo item:

def insertion_sort(array):
    for i in range(1, len(array)):
        chave = array[i]
        j = i - 1 
        while j >= 0 and array[j] > chave:
            array[j + 1] = array[j]  
            j -= 1  
        array[j + 1] = chave

lista = [5, 2, 9, 1, 5, 6]
insertion_sort(lista)
print(lista)

