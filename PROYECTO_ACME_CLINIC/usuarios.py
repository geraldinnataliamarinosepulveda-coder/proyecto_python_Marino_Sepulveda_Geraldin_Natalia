import hashlib
from almacenamiento import guardar_json, leer_json

ARCHIVO = "usuarios.json"

def hash_clave(clave):
    return hashlib.sha256(clave.encode()).hexdigest()


def preparar_administrador():
    usuarios = leer_json(ARCHIVO)

    if not usuarios:
        administrador = {
            "identificacion": "0000",
            "nombres": "Admin",
            "apellidos": "Administrador",
            "telefono": "555000111",
            "email": "admin@acmeclinic.com",
            "direccion": "Cl 185 # 26 - 85",
            "rol": "administrativo",
            "clave": hash_clave("Admin123")
        }

        usuarios.append(administrador)
        guardar_json(ARCHIVO, usuarios)


def iniciar_sesion():
    preparar_administrador()

    usuarios = leer_json(ARCHIVO)

    print("\n--- INICIO DE SESION ---")

    email = input("Correo: ").strip().lower()
    clave = input("Contraseña: ")

    for usuario in usuarios:
        if (usuario["email"].lower() == email
                and usuario["clave"] == hash_clave(clave)):
            print("Inicio de sesión exitoso.")
            return usuario

    print("Correo o contraseña incorrectos.")
    return None


def registrar_usuario():
    usuarios = leer_json(ARCHIVO)

    print("\n--- REGISTRO DE USUARIO ---")

    identificacion = input("Identificación: ").strip()

    if any(u["identificacion"] == identificacion for u in usuarios):
        print("El usuario ya existe.")
        return

    nombres = input("Nombres: ").strip()
    apellidos = input("Apellidos: ").strip()
    telefono = input("Teléfono: ").strip()
    email = input("Correo: ").strip().lower()
    direccion = input("Dirección: ").strip()
    rol = input("Rol (medico/administrativo): ").strip().lower()
    clave = input("Contraseña: ")

    if rol not in ["medico", "administrativo"]:
        print("Rol incorrecto.")
        return

    nuevo_usuario = {
        "identificacion": identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "rol": rol,
        "clave": hash_clave(clave)
    }

    usuarios.append(nuevo_usuario)
    guardar_json(ARCHIVO, usuarios)

    print("Usuario registrado correctamente.")