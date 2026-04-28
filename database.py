import sqlite3

def conectar():
    return sqlite3.connect("users.db")

def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT UNIQUE,
        password TEXT,
        coins INTEGER DEFAULT 0,
        nivel INTEGER DEFAULT 1,
        rol TEXT DEFAULT 'user',
        clase TEXT DEFAULT 'Normal'
    )
    """)

    conn.commit()
    conn.close()

def crear_admin():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE nombre='admin'")
    admin = cursor.fetchone()

    if not admin:
        cursor.execute("""
        INSERT INTO usuarios (nombre,password,rol)
        VALUES ('admin','admin123','admin')
        """)

    conn.commit()
    conn.close()

def registrar(nombre,password):
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO usuarios (nombre,password)
        VALUES (?,?)
        """,(nombre,password))

        conn.commit()
        conn.close()
        return True

    except:
        return False

def login(nombre,password):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM usuarios
    WHERE nombre=? AND password=?
    """,(nombre,password))

    usuario = cursor.fetchone()

    conn.close()
    return usuario

def subir_nivel_y_coins(nombre):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE usuarios
    SET coins = coins + 10,
        nivel = nivel + 1
    WHERE nombre = ?
    """, (nombre,))

    conn.commit()
    conn.close()


def obtener_usuario(nombre):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM usuarios WHERE nombre = ?
    """, (nombre,))

    usuario = cursor.fetchone()

    conn.close()
    return usuario

def cambiar_clase(nombre, clase):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE usuarios
    SET clase = ?
    WHERE nombre = ?
    """, (clase, nombre))

    conn.commit()
    conn.close()