from pygame import *
import sys

init()

pikachu_img = image.load('pikachu.png')
pikachu_img = transform.scale(pikachu_img, (200, 200))

pikachu_font = font.Font('Bleeding_Cowboys.ttf', 50)

#colocar a fonte do mp3 dentro desse parenteses
#mixer.music.load()

window = display.set_mode((1280, 720))
window.fill((151, 209, 250))


#Programa para consguir fechar a janela
while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
    
    #desenhar a partir daqui
    
    #draw.rect(window, (cor), (x, y, largura, altura))
    draw.rect(window, (72, 157, 37), (0, 600, 1280, 250))
    draw.rect(window, (100, 100, 100), (300, 350, 200, 250))
    
    #draw.circle(window, (cor), (x, y), raio)
    draw.circle(window, (255, 242, 81), (120, 140), 60)
   
    #draw.polygon(window, (cor), ((ponto do triangulo), (ponto do triangulo), (ponto do triangulo)))
    draw.polygon(window, (242, 136, 59), ((300, 350), (400, 200), (500, 350)))
    
    #desenhar uma linha
    draw.line(window, (255, 0, 255), (100, 100), (200, 200), 5)

    #desenhar imagem
    window.blit(pikachu_img, (100, 420))

    #desenhar texto
    pikachu_text = pikachu_font.render('Pika Pika', True, (0, 0, 0))
    window.blit(pikachu_text, (100, 430))

    display.update()

