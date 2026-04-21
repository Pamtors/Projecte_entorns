# Projecte_entorns
Projecte de entorns

ENLLAÇOS:
Diagrama de clases: 
//www.plantuml.com/plantuml/png/ZLJ1Rjiy3BxxAOHU_lGVSjWrs8PwZJUaM9EYJeRsoCXina6sKahAW7Lxg3t3NcmERTNs4BZBHT77Jn_9Zv8ld0VseJJ9V-hjwLyTsUIRz7QnoaT8se1pQkC2C5drb2WrLLJC55LU_bUst3BEbFDCrKuWB87C0DdN6jyi5mDGMwfSJuWEQEBsLRsI9k0S7TbgSYuOuuvg0M27BQAHkKVwcRJrfaL9bN0Bo-f9k6Ye1e7RNYPX5jjgjC3HhWxBqLvGL6F_RtvCfqFnPDJWgqtsSVMYkrS1Tz7Rq6HAjGzWdele78g1vN7JT-e6s5C1qHZW7R2GMiGZI_kHrtDBQ6t-AfJ8jXjBGG-aW_7G6rvCEaoWRRatw2Ce-ardPw_Fr7JwJbO9HZy74U6EsxbCFsVgNbskhj-dw-n5NvTmmBQjlNMaoLPtC_LWB7W13rH0rsbTbzKrKlGfHo6SgSlZ8bsMze2y-FuO2BbnEu9pPDHV8bIGsmC3ztsU2nOdNS3lNtOiVHJkIwospeCE9eeCMpZPPGJlJmatpqhJbdX-h6UYeVB7AaHK4f-ObJYRo2Wx-F-phhhaIEY7Okz9kmhUqKUdVlafpRDSJTQBcrMkvfbSW_EH8r3hCcYlnBDcUEr70FQ6D73sWDhRYOq5pBfQejdnO0xLZg6m9mN-9dy8o1x_YNeBUnfJ5P9yS8Pr309TpW7SwISo2N5Rq76drujiEK_L9BjRtwRdBxwlDM5LWBJGF7y6liQlbfyV0RgjiOy1WINxf7-XfAX68caMGUHgNTJRK9e_

Diagrama de secuencia: //www.plantuml.com/plantuml/png/VP51JiGm34NtEOMNiE02iq0ZJTcm61280tXICxBaDf6JL5oBCt0nd6PQbH6QIArQ__U_8tkVCcekWpZqEIXyf8BAmRdB1pmymdEXSu0TyCYUKTyfSHZlxcyWhvR9FHhZccB8aISIGppg6NN-gxg44A4hYcCc48JOh0xiR1eSSI8p3s4YDTl_Qi_9xBW0zTKaGxfP2qPvfGLPgmQyd596NwGYF4Jq-M_Ggb_3IfvFh1t-V8Uj0IN3GJ0HK8h6eCpbxQMQl0ECmXxrwPDyNZBiDFswNryR0NrbRLEYiNVrSMt2cssCjN08GnJAs5lmkerrU7MaoPBqZLAH2xMtk3B8Bm00




ESCRIT BASE DEL JOC:

BASE PLATAFORMA

Voy a diseñar un videojuego, el videojuego va a tener como base el juego llamado “Space Invaders”, pero se le añadirá un seguido de extras como modificar la nave y clases.


Pantalla principal, poder iniciar sesión y registrarte.


2 tipos de usuario; el administrador y el usuario básico.

Funciones del Administrador:
Gestionar a los usuarios, de tal manera que pueda eliminar la cuenta de los usuarios, pueda dar el rol de administrador a otro usuario.

Funciones del usuario:
Jugar al juego.

Cuando tenga iniciada la sesión el usuario visualizará 3 opciones donde poder acceder, jugar la partida en el nivel que le corresponda, modificar la nave (se desbloquea a partir de desbloquear el tercer nivel/mapa), o cerrar la sesión para cambiar la cuenta.

Además podrá visualizar el nivel que se encuentra y los puntos obtenidos, que les llamaremos “coins”. 

Estos Coins serán necesarios para poder modificar la nave.


JUGABILIDAD

NIVELES

Como hemos comentado anteriormente hay diferentes niveles los cuales a medida que se completa el nivel da la opción a empezar el siguiente nivel o ir al menú principal del usuario iniciado.



NAVE
En la parte inferior de la pantalla visualizamos la nave, la nave se ve de la misma manera con y sin modificaciones para hacerlo más simple.
Y esta dispara en dirección vertical hacia arriba. Y se mueve de manera horizontal dentro de la pantalla.


OBSTÁCULOS

Los obstáculos empezarán en la parte superior de la pantalla de tal manera que a medida de que pasen los segundos irán desplazándose de manera vertical hacia abajo.
A medida que pase el tiempo del nivel irán apareciendo nuevos obstáculos. Estos serán igual de “difíciles” en el mismo nivel (misma vida y tamaño en el mismo nivel de mapa).


CLASES 

La nave cuando la modifiques (en el apartado de modificar la nave) y llegues al 3 nivel podrás escoger 3 clases diferentes;
clase Sangrado, clase Fuerte y clase Rápido.

La clase Sangrado cuando un disparo de la nave impacta a un obstáculo, este recibe 2 ticks de daño adicional, además del primer contacto.

La clase Fuerte, dispara más lento de lo normal, pero el disparo hace más daño.

La clase Rápido, dispara más rápido pero hace menos daño por disparo.




ESCRIT DIAGRAMA CLASES UML

@startuml

' =======================
' USUARIOS
' =======================

class Usuario {
  - id: int
  - nombre: string
  - email: string
  - password: string
  - coins: int
  - nivel: int
  + iniciarSesion()
  + registrarse()
  + cerrarSesion()
}

class Administrador {
  + eliminarUsuario(u: Usuario)
  + asignarAdmin(u: Usuario)
}

Usuario <|-- Administrador

' =======================
' JUEGO
' =======================
class Juego {
  - usuarioActual: Usuario
  - nivelActual: Nivel
  + iniciarPartida()
  + cargarNivel()
  + terminarPartida()
}

class Nivel {
  - numero: int
  - dificultad: string
  + iniciarNivel()
  + completarNivel()
}

Juego "1" --> "1" Nivel
Usuario "1" --> "1" Juego

' =======================
' NAVE Y COMBATE
' =======================
class Nave {
  - posicionX: float
  - vida: int
  - velocidad: float
  - clase: Clase
  + moverIzquierda()
  + moverDerecha()
  + disparar()
}

class Disparo {
  - daño: int
  - velocidad: float
  + mover()
}

class Obstaculo {
  - vida: int
  - posicionX: float
  - posicionY: float
  + mover()
  + recibirDaño(cantidad: int)
}

Usuario "1" --> "1" Nave
Nivel "1" --> "*" Obstaculo
Nave "1" --> "*" Disparo
Disparo --> Obstaculo

' =======================
' CLASES (TIPOS DE NAVE)
' =======================
abstract class Clase {
  + aplicarEfecto(obstaculo: Obstaculo)
}

class ClaseSangrado {
  + aplicarEfecto()
}

class ClaseFuerte {
  + aplicarEfecto()
}

class ClaseRapido {
  + aplicarEfecto()
}

Clase <|-- ClaseSangrado
Clase <|-- ClaseFuerte
Clase <|-- ClaseRapido

Nave --> Clase

' =======================
' TIENDA (EXTRA)
' =======================
class Tienda {
  + comprarMejora()
  + desbloquearClase()
}

Usuario --> Tienda
Tienda --> Nave

@enduml


ESCRIT DIAGRAMA SECUENCIES UML

@startuml

actor Usuario

Usuario -> Juego : iniciarSesion()
Usuario -> Juego : iniciarPartida()

Juego -> Nivel : cargarNivel()

loop Durante la partida
    Usuario -> Nave : mover()
    Usuario -> Nave : disparar()
    
    Nave -> Disparo : crear()
    Disparo -> Obstaculo : impactar()
    
    Obstaculo -> Obstaculo : recibirDaño()
    
    alt Clase especial
        Nave -> Clase : aplicarEfecto()
        Clase -> Obstaculo : daño extra
    end
end

Nivel -> Juego : nivelCompletado()
Juego -> Usuario : mostrarResultado()

@enduml
