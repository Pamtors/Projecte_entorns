import pygame
import sys
from database import *
from game import jugar

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

usuario_seleccionado = None
usuarios_admin = []

def texto(msg, x, y, color=(255, 255, 255)):
    t = fuente.render(msg, True, color)
    pantalla.blit(t, (x, y))


def dibujar_login():
    pantalla.fill((0, 0, 30))

    texto("SPACE UPGRADE", 250, 50)
    texto("Usuario: " + usuario_texto, 180, 200)
    texto("Password: " + pass_texto, 180, 260)

    texto("ENTER = Login", 250, 350, (0, 255, 0))
    texto("R = Registro", 250, 400, (0, 255, 0))
    texto("TAB = Cambiar campo", 220, 450, (255, 255, 0))

    texto(mensaje, 220, 520, (255, 255, 255))


def dibujar_menu():
    pantalla.fill((20, 20, 20))

    nombre = usuario_logeado[1]
    coins = str(usuario_logeado[3])
    nivel = str(usuario_logeado[4])
    clase = str(usuario_logeado[6])

    texto("MENU PRINCIPAL", 250, 50)

    texto("Usuario: " + nombre, 50, 150)
    texto("Coins: " + coins, 50, 200)
    texto("Nivel: " + nivel, 50, 250)
    texto("Clase: " + clase, 50, 300)

    texto("1 - JUGAR", 250, 350, (0, 255, 0))

    if usuario_logeado[4] >= 3:
        texto("2 - ELEGIR CLASE", 250, 400, (0, 255, 0))
    else:
        texto("2 - BLOQUEADO (Nivel 3)", 250, 400, (255, 0, 0))

    texto("3 - LOGOUT", 250, 450, (255, 255, 0))

    if usuario_logeado[5] == "admin":
        texto("9 - PANEL ADMIN", 250, 500, (255, 0, 0))

    texto(mensaje, 100, 560, (255, 255, 255))


def dibujar_clases():

    pantalla.fill((20, 20, 20))

    texto("SELECCIONAR CLASE", 220, 100)

    texto("1 - Sangrado", 250, 220)
    texto("2 - Fuerte", 250, 280)
    texto("3 - Rapido", 250, 340)

    texto("ESC - Volver", 250, 450, (255, 255, 0))

def dibujar_admin():

    pantalla.fill((20,20,20))

    texto("PANEL ADMIN", 250, 50)

    y = 140

    for i, usuario in enumerate(usuarios_admin[:9]):

        color = (255,255,255)

        if usuario_seleccionado == i:
            color = (0,255,0)

        texto(
            f"{i+1} - {usuario[0]} ({usuario[1]})",
            100,
            y,
            color
        )

        y += 40

    texto("A - HACER ADMIN", 450, 180, (255,255,0))
    texto("B - ELIMINAR", 450, 240, (255,255,0))
    texto("ESC - VOLVER", 450, 300, (255,255,0))

    if usuario_seleccionado is not None:

        texto(
            "SELECCIONADO:",
            100,
            520,
            (0,255,0)
        )

        texto(
            usuarios_admin[usuario_seleccionado][0],
            350,
            520,
            (0,255,0)
        )


while True:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:

            # ---------------- LOGIN ----------------
            if pantalla_actual == "login":

                if evento.key == pygame.K_TAB:

                    if campo == "user":
                        campo = "pass"
                    else:
                        campo = "user"

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
                        mensaje = "Login correcto"
                    else:
                        mensaje = "Datos incorrectos"

                elif evento.key == pygame.K_r:

                    ok = registrar(usuario_texto, pass_texto)

                    if ok:
                        mensaje = "Usuario registrado"
                    else:
                        mensaje = "Usuario ya existe"

                else:

                    if campo == "user":
                        usuario_texto += evento.unicode
                    else:
                        pass_texto += evento.unicode

            # ---------------- MENU ----------------
            elif pantalla_actual == "menu":

                if evento.key == pygame.K_1:

                    ganado = jugar(
                        pantalla,
                        usuario_logeado[6],
                        usuario_logeado[4]
                    )

                    if ganado:

                        subir_nivel_y_coins(usuario_logeado[1])

                        usuario_logeado = obtener_usuario(
                            usuario_logeado[1]
                        )

                        mensaje = "Nivel completado! +10 coins +1 nivel"

                    else:
                        mensaje = "Has perdido"

                elif evento.key == pygame.K_2:

                    if usuario_logeado[4] >= 3:
                        pantalla_actual = "clases"
                    else:
                        mensaje = "Bloqueado hasta nivel 3"

                elif evento.key == pygame.K_3:

                    pantalla_actual = "login"
                    usuario_texto = ""
                    pass_texto = ""
                    usuario_logeado = None
                    mensaje = "Sesion cerrada"
                
                elif evento.key == pygame.K_9:

                    if usuario_logeado[5] == "admin":

                        usuarios_admin = obtener_usuarios()
                        usuario_seleccionado = None

                        pantalla_actual = "admin"


            # ---------------- CLASES ----------------
            elif pantalla_actual == "clases":

                if evento.key == pygame.K_1:

                    cambiar_clase(
                        usuario_logeado[1],
                        "Sangrado"
                    )

                    usuario_logeado = obtener_usuario(
                        usuario_logeado[1]
                    )

                    mensaje = "Clase Sangrado equipada"
                    pantalla_actual = "menu"

                elif evento.key == pygame.K_2:

                    cambiar_clase(
                        usuario_logeado[1],
                        "Fuerte"
                    )

                    usuario_logeado = obtener_usuario(
                        usuario_logeado[1]
                    )

                    mensaje = "Clase Fuerte equipada"
                    pantalla_actual = "menu"

                elif evento.key == pygame.K_3:

                    cambiar_clase(
                        usuario_logeado[1],
                        "Rapido"
                    )

                    usuario_logeado = obtener_usuario(
                        usuario_logeado[1]
                    )

                    mensaje = "Clase Rapido equipada"
                    pantalla_actual = "menu"

                elif evento.key == pygame.K_ESCAPE:

                    pantalla_actual = "menu"

            # ---------------- ADMIN ----------------
            elif pantalla_actual == "admin":

                if evento.key >= pygame.K_1 and evento.key <= pygame.K_9:

                    indice = evento.key - pygame.K_1

                    if indice < len(usuarios_admin):
                        usuario_seleccionado = indice

                elif evento.key == pygame.K_a:

                    if usuario_seleccionado is not None:

                        nombre = usuarios_admin[usuario_seleccionado][0]

                        hacer_admin(nombre)

                        usuarios_admin = obtener_usuarios()

                        mensaje = nombre + " ahora es admin"

                elif evento.key == pygame.K_b:

                    if usuario_seleccionado is not None:

                        nombre = usuarios_admin[usuario_seleccionado][0]

                        eliminar_usuario(nombre)

                        usuarios_admin = obtener_usuarios()

                        usuario_seleccionado = None

                        mensaje = nombre + " eliminado"

                elif evento.key == pygame.K_ESCAPE:

                    pantalla_actual = "menu"

    # ---------------- DIBUJAR ----------------
    if pantalla_actual == "login":
        dibujar_login()

    elif pantalla_actual == "menu":
        dibujar_menu()

    elif pantalla_actual == "clases":
        dibujar_clases()
    
    elif pantalla_actual == "admin":
        dibujar_admin()

    pygame.display.update()







