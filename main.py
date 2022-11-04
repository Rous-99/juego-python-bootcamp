import pygame
#importamos la libreria
import random
from settings import * #así puedo llamar a las variables directamente sin llamar a setting en cada propiedad

pygame.init()
#inicializamos pygame

# SIZE=(400,500) #dimensiones de la ventana
surface=pygame.display.set_mode(SIZE)
pygame.display.set_caption('Introduccion a interfaces')
#le da un titulo a la ventana
# BACKGROUND=(255,255,255) #en mayusculas porque es una constante y no se va a modificar
# BLUE=(0,0,255)
game=True
win=False
seconds_count_after_win=0
# BLACK=(0,0,0)
player=pygame.Rect(200,200,100,20)
#                  posx posy w h
clock=pygame.time.Clock()

#Creacion de rectangulos
rects=[]

for x in range(0,10): #se apilan todos uno encima del otro y parece que solo hay uno si no utilizado con randint una posición aleatoria para cada uno
    pox=random.randint(0,385)
    poy=random.randint(0,485)
    rect=pygame.Rect(pox,poy,RECT_W,RECT_W)
    rects.append(rect)

#LIST COMPREHENSION, nos permite crear listas en una sola linea de codigo

# rects=[pygame.Rect(pox,poy,15,15) for x in range(0,10)]

while game: #se ejecuta hasta que pase de verdadero a falso
    clock.tick(FPS)
    seconds=pygame.time.get_ticks()//1000
    for event in pygame.event.get(): #por cada evento va a hacer lo siguiente
        if event.type==pygame.QUIT: #comprueba si el evento es de tipo quit (darle a la flecha para cerrar la ventana)
            game=False #si es así game cambia a false y se deja de "pintar" la ventana
    
    pos=pygame.mouse.get_pos()
    #para mover el rectangulo con el mpuse, el get_pos obtiene las coordenadas del mouse en la pantalla. pos es de esta forma: (x,y)
    if not win:
        player.center=pos
    
    # rect1.x=pos[0] #pilla la primera coordenada de la posición de pos.
    # rect1.y=pos[1]
    surface.fill(BACKGROUND)
    #le damos un color a la ventana
    pygame.draw.rect(surface,BLACK,player)
    #se pinta en la superficie, en negro

    for rect in rects:

        if player.colliderect(rect):
            color=RED
            rect.x=-100
            rect.y=-100
        else:
            color=BLUE

        pygame.draw.rect(surface, color,rect)

    count=0
    for rect in rects:
        if rect.x<0:
            count+=1
    
    if count==len(rects):
        surface.fill(RED)
        # print("GANASTE!")
        # game=False
    

    if win and seconds_count_after_win==0:
        seconds_count_after_win=seconds
    
    if seconds_count_after_win +5 <seconds:
        print("Ganaste")
        game=False
        
     
    
     
        
    pygame.display.flip()#actualiza la ventana, siempre es lo ultimo que va al final del ciclo while