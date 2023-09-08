import random
import os
import time
import pygame


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    draw(array, i, j)
    

def draw(array, i, j):
    janela.fill([0,0,0,0])
    for numero in range(len(array)):
        blocos = pygame.Rect(((largura/total_barras)*numero), (altura/total_barras)*array[numero], (largura/total_barras), altura)
        if numero == j:
            pygame.draw.rect(janela, [255, 0, 0, 0], blocos)
        elif numero == i:
            pygame.draw.rect(janela, [0, 0, 255, 0], blocos)
        else:
            pygame.draw.rect(janela, [255, 255, 255, 255], blocos)
    pygame.display.update()

def merge_sort(array, left_index, right_index):
    if (left_index < right_index):
        middle_index = int((left_index + right_index) / 2)
        merge_sort(array, left_index, middle_index)
        merge_sort(array, middle_index+1, right_index)
        merge(array, left_index, right_index, middle_index)

def merge(array, left_index, right_index, middle_index):
    auxArray = []
    for i in range(right_index+1):
        auxArray.append(array[i])

    i = left_index
    j = middle_index + 1
    free_index = left_index
    while i != middle_index + 1 and j != right_index + 1:
        if (array[i] > array[j]):
            auxArray[free_index] = array[j]
            j += 1
        else:
            auxArray[free_index] = array[i]
            i += 1
        free_index += 1

    while i != middle_index + 1:
        auxArray[free_index] = array[i]
        i += 1
        free_index += 1

    while j != right_index + 1:
        auxArray[free_index] = array[j]
        j += 1
        free_index +=1

    i = left_index
    for j in range(left_index, right_index+1):
        array[i] = auxArray[j]
        draw(array, i, j)
        i +=1

# Inicia janela
pygame.init()
altura = 500
largura = 800
total_barras = 800
janela = pygame.display.set_mode([largura, altura])

# Preenche array
array = []
for i in range(0, total_barras+1):
    array.append(i)

clock = 0
while clock < total_barras:
    index1 = random.randint(0, total_barras)
    index2 = random.randint(0, total_barras)
    swap(array, index1, index2)
    clock += 1

# Inicia a ordenação
pygame.display.update()

merge_sort(array, 0, len(array)-1)

pygame.display.update()
time.sleep(5)