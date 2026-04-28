import pygame
import sys
from database import *

pygame.init()

ANCHO = 800
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Space Upgrade")

fuente = pygame.font.SysFont(None,40)

crear_tabla()
crear_admin()

usuario_texto = ""
pass_texto = ""
campo = "user"

mensaje = ""

def dibujar():
    pantalla.fill((0,0,30))

    titulo = fuente.render("SPACE UPGRADE",True,(255,255,255))
    pantalla.blit(titulo,(260,50))

    user = fuente.render("Usuario: " + usuario_texto,True,(255,255,255))
    pantalla.blit(user,(200,200))

    pwd = fuente.render("Password: " + pass_texto,True,(255,255,255))
    pantalla.blit(pwd,(200,260))

    info = fuente.render("ENTER=Login | R=Registro",True,(0,255,0))
    pantalla.blit(info,(180,350))

    msg = fuente.render(mensaje,True,(255,255,0))
    pantalla.blit(msg,(250,450))

    pygame.display.update()

while True:

    dibujar()

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:

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
                user = login(usuario_texto,pass_texto)

                if user:
                    mensaje = "Login correcto!"
                else:
                    mensaje = "Datos incorrectos"

            elif evento.key == pygame.K_r:
                ok = registrar(usuario_texto,pass_texto)

                if ok:
                    mensaje = "Usuario registrado"
                else:
                    mensaje = "Usuario ya existe"

            else:
                if campo == "user":
                    usuario_texto += evento.unicode
                else:
                    pass_texto += evento.unicode