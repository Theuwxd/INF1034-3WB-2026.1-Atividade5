from pygame import *
import sys

init()

pikachu_img = image.load('pikachu.png')
pikachu_img = transform.scale(pikachu_img, (150, 150))

pikachu_font = font.Font('Pokemon Solid.ttf', 40)

# colocar a fonte do mp3 dentro desse parenteses
mixer.music.load('pokemon.mp3')
mixer.music.play(-1)

window = display.set_mode((1280, 720))
window.fill((151, 209, 250))


# Programa para consguir fechar a janela
while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

    # desenhar a partir daqui

    # draw.rect(window, (cor), (x, y, largura, altura))
    draw.rect(window, (72, 157, 37), (0, 600, 1280, 250))
    draw.rect(window, (100, 100, 100), (300, 350, 220, 250))
    draw.rect(window, (255, 255, 255), (320, 440, 60, 90))
    draw.rect(window, (102, 51, 0), (420, 420, 80, 180))
    draw.rect(window, (152, 76, 0), (850, 420, 50, 180))

    # draw.circle(window, (cor), (x, y), raio)
    draw.circle(window, (255, 242, 81), (120, 140), 50)
    draw.circle(window, (255, 242, 81), (430, 500), 5)
    draw.circle(window, (76, 153, 0), (880, 350), 100)
    draw.circle(window, (255, 255, 255), (700, 100), 40)
    draw.circle(window, (255, 255, 255), (750, 100), 45)
    draw.circle(window, (255, 255, 255), (800, 100), 40)
    draw.circle(window, (255, 255, 255), (850, 100), 45)
    draw.circle(window, (255, 255, 255), (900, 100), 40)

    # draw.polygon(window, (cor), ((ponto do triangulo), (ponto do triangulo), (ponto do triangulo)))
    draw.polygon(window, (242, 136, 59), ((300, 350), (420, 200), (520, 350)))

    # desenhar uma linha
    draw.line(window, (255, 242, 81), (50, 70), (200, 200), 13)
    draw.line(window, (255, 242, 81), (200, 70), (50, 200), 13)
    draw.line(window, (255, 242, 81), (120, 40), (120, 230), 10)
    draw.line(window, (255, 242, 81), (30, 135), (220, 135), 10)

    # desenhar imagem
    window.blit(pikachu_img, (500, 465))

    # desenhar texto
    pikachu_text = pikachu_font.render('Pikachu!!', True, (0, 0, 0))
    window.blit(pikachu_text, (500, 600))

    display.update()
