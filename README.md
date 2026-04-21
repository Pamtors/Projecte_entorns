# Projecte_entorns
Projecte de entorns
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
