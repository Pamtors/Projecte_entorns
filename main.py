import pygame
import sys
from database import *

pygame.init()

ANCHO = 800
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Space Upgrade")

fuente = pygame.font.SysFont(None, 40)

crear_tabla()
crear_admin()

usuario_texto = ""
pass_texto = ""
campo = "user"
mensaje = ""

pantalla_actual = "login"
usuario_logeado = None


def texto(msg, x, y, color=(255,255,255)):
    t = fuente.render(msg, True, color)
    pantalla.blit(t, (x, y))


def dibujar_login():
    pantalla.fill((0,0,30))

    texto("SPACE UPGRADE", 260, 50)
    texto("Usuario: " + usuario_texto, 180, 200)
    texto("Password: " + pass_texto, 180, 260)
    texto("ENTER=Login", 250, 350, (0,255,0))
    texto("R=Registro", 280, 400, (0,255,0))
    texto(mensaje, 250, 500, (255,255,0))


def dibujar_menu():
    pantalla.fill((20,20,20))

    nombre = usuario_logeado[1]
    coins = str(usuario_logeado[3])
    nivel = str(usuario_logeado[4])

    texto("MENU PRINCIPAL", 250, 50)
    texto("Usuario: " + nombre, 50, 150)
    texto("Coins: " + coins, 50, 200)
    texto("Nivel: " + nivel, 50, 250)

    texto("1 - JUGAR", 250, 350, (0,255,0))

    if usuario_logeado[4] >= 3:
        texto("2 - MODIFICAR NAVE", 250, 400, (0,255,0))
    else:
        texto("2 - BLOQUEADO (Nivel 3)", 250, 400, (255,0,0))

    texto("3 - LOGOUT", 250, 450, (255,255,0))


while True:

    pantalla.fill((0,0,0))

    if pantalla_actual == "login":
        dibujar_login()

    elif pantalla_actual == "menu":
        dibujar_menu()

    pygame.display.update()

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:

            if pantalla_actual == "login":

                if evento.key == pygame.K_TAB:
                    campo = "pass" if campo == "user" else "user"

                elif evento.key == pygame.K_BACKSPACE:
                    if campo == "user":
                        usuario_texto = usuario_texto[:-1]
                    else:
                        pass_texto = pass_texto[:-1]

                elif evento.key == pygame.K_RETURN:

                    user = login(usuario_texto, pass_texto)

                    if user:
                        usuario_logeado = user
                        pantalla_actual = "menu"
                        mensaje = ""
                    else:
                        mensaje = "Datos incorrectos"

                elif evento.key == pygame.K_r:

                    ok = registrar(usuario_texto, pass_texto)

                    if ok:
                        mensaje = "Registrado correctamente"
                    else:
                        mensaje = "Usuario ya existe"

                else:
                    if campo == "user":
                        usuario_texto += evento.unicode
                    else:
                        pass_texto += evento.unicode

            elif pantalla_actual == "menu":

                if evento.key == pygame.K_1:
                    mensaje = "Pronto iniciaremos juego"

                elif evento.key == pygame.K_2:
                    if usuario_logeado[4] >= 3:
                        mensaje = "Zona modificar nave"
                    else:
                        mensaje = "Bloqueado"

                elif evento.key == pygame.K_3:
                    pantalla_actual = "login"
                    usuario_texto = ""
                    pass_texto = ""
                    usuario_logeado = None