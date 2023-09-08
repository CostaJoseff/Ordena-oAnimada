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

# Inicia janela
pygame.init()
altura = 600
largura = 1024
total_barras = 1024
janela = pygame.display.set_mode([largura, altura])

# Preenche array
array = []
for i in range(0, total_barras):
    numero = random.randint(0, total_barras+1)
    array.append(numero)

# Inicia a ordenação
pygame.display.update()
for i in range(0, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            swap(array, j, j-1)
            
        else:
            break

pygame.display.update()
time.sleep(5)