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

def quick_sort(array, left_index, right_index):
    if (left_index < right_index):
        pivot = quick(array, left_index, right_index)
        quick_sort(array, left_index, pivot-1)
        quick_sort(array, pivot+1, right_index)
        

def quick(array, left_index, right_index):
    pivot = findNewPivot(left_index, right_index)
    swap(array, left_index, pivot)
    pivot = left_index
    next_free_index = left_index+1
    for j in range(pivot+1, right_index+1):
        if array[pivot] > array[j]:
            swap(array, next_free_index, j)
            next_free_index +=1

    next_free_index -= 1
    swap(array, next_free_index, pivot)
    return next_free_index

def findNewPivot(left_index, right_index):
    return random.randint(left_index, right_index)

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

quick_sort(array, 0, len(array)-1)

pygame.display.update()
time.sleep(5)