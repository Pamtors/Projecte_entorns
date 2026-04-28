import pygame
import random

pygame.init()

ANCHO = 800
ALTO = 600

fuente = pygame.font.SysFont(None, 40)

def jugar(pantalla):

    reloj = pygame.time.Clock()

    nave = pygame.Rect(380, 540, 40, 30)
    balas = []
    enemigos = []

    for i in range(5):
        x = random.randint(50, 750)
        enemigos.append(pygame.Rect(x, 50, 40, 30))

    corriendo = True
    ganar = False

    while corriendo:

        reloj.tick(60)
        pantalla.fill((0,0,20))

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    balas.append(pygame.Rect(nave.x+15, nave.y, 10, 20))

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT] and nave.x > 0:
            nave.x -= 5

        if teclas[pygame.K_RIGHT] and nave.x < 760:
            nave.x += 5

        for bala in balas:
            bala.y -= 8

        for enemigo in enemigos:
            enemigo.y += 0.2

        for bala in balas[:]:
            for enemigo in enemigos[:]:
                if bala.colliderect(enemigo):
                    if bala in balas:
                        balas.remove(bala)
                    if enemigo in enemigos:
                        enemigos.remove(enemigo)

        pygame.draw.rect(pantalla, (0,255,0), nave)

        for bala in balas:
            pygame.draw.rect(pantalla, (255,255,0), bala)

        for enemigo in enemigos:
            pygame.draw.rect(pantalla, (255,0,0), enemigo)

        if len(enemigos) == 0:
            ganar = True
            corriendo = False

        for enemigo in enemigos:
            if enemigo.y > 560:
                corriendo = False

        pygame.display.update()

    return ganar