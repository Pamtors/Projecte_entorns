import pygame
import random

pygame.init()

def jugar(pantalla, clase, nivel):

    reloj = pygame.time.Clock()

    nave = pygame.Rect(380, 540, 40, 30)

    balas = []

    enemigos = []

    # Configuración según nivel
    cantidad_enemigos = 5 + (nivel * 2)
    vida_enemigo = nivel

    for i in range(cantidad_enemigos):

        enemigo = {
            "rect": pygame.Rect(
                random.randint(50, 730),
                random.randint(20, 200),
                40,
                30
            ),
            "vida": vida_enemigo
        }

        enemigos.append(enemigo)

    # Configuración clases
    cooldown = 0
    velocidad_bala = 8
    daño_bala = 1

    if clase == "Rapido":
        velocidad_bala = 12

    if clase == "Fuerte":
        daño_bala = 2

    corriendo = True
    ganar = False

    while corriendo:

        reloj.tick(60)
        pantalla.fill((0, 0, 20))

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()

        teclas = pygame.key.get_pressed()

        # Movimiento nave
        if teclas[pygame.K_LEFT] and nave.x > 0:
            nave.x -= 5

        if teclas[pygame.K_RIGHT] and nave.x < 760:
            nave.x += 5

        # Cooldown
        if cooldown > 0:
            cooldown -= 1

        # Disparo
        if teclas[pygame.K_SPACE] and cooldown == 0:

            balas.append({
                "rect": pygame.Rect(nave.x + 15, nave.y, 10, 20),
                "daño": daño_bala
            })

            if clase == "Rapido":
                cooldown = 10
            elif clase == "Fuerte":
                cooldown = 35
            else:
                cooldown = 25

        # Movimiento balas
        for bala in balas[:]:

            bala["rect"].y -= velocidad_bala

            if bala["rect"].y < 0:
                balas.remove(bala)

        # Movimiento enemigos
        for enemigo in enemigos:
            enemigo["rect"].y += 0.20 + (nivel * 0.05)

        # Colisiones
        for bala in balas[:]:

            for enemigo in enemigos[:]:

                if bala["rect"].colliderect(enemigo["rect"]):

                    enemigo["vida"] -= bala["daño"]

                    # Sangrado
                    if clase == "Sangrado":
                        enemigo["vida"] -= 1

                    if bala in balas:
                        balas.remove(bala)

                    if enemigo["vida"] <= 0:
                        enemigos.remove(enemigo)

                    break

        # Dibujar nave
        pygame.draw.rect(pantalla, (0, 255, 0), nave)

        # Dibujar balas
        for bala in balas:
            pygame.draw.rect(
                pantalla,
                (255, 255, 0),
                bala["rect"]
            )

        # Dibujar enemigos
        for enemigo in enemigos:

            pygame.draw.rect(
                pantalla,
                (255, 0, 0),
                enemigo["rect"]
            )

        # Victoria
        if len(enemigos) == 0:
            ganar = True
            corriendo = False

        # Derrota
        for enemigo in enemigos:

            if enemigo["rect"].y > 560:
                corriendo = False

        # Mostrar nivel
        fuente = pygame.font.SysFont(None, 30)

        texto_nivel = fuente.render(
            f"Nivel {nivel}",
            True,
            (255, 255, 255)
        )

        pantalla.blit(texto_nivel, (10, 10))

        pygame.display.update()

    return ganar
