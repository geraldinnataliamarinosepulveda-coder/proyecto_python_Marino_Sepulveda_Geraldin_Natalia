from almacenamiento import leer_json, guardar_json

ARCHIVO = "pacientes.json"


def registrar_paciente():
    pacientes = leer_json(ARCHIVO)

    print("\n--- REGISTRO DE PACIENTE ---")

    identificacion = input("Número de identificación: ").strip()

    if any(p["identificacion"] == identificacion for p in pacientes):
        print("El paciente ya está registrado.")
        return

    nombres = input("Nombres: ").strip()
    apellidos = input("Apellidos: ").strip()
    telefono = input("Teléfono: ").strip()
    email = input("Correo electrónico: ").strip()
    direccion = input("Dirección: ").strip()
    genero = input("Género: ").strip()
    estado_civil = input("Estado civil: ").strip()

    if not identificacion or not nombres or not apellidos:
        print("La identificación y los nombres son obligatorios.")
        return

    paciente = {
        "identificacion": identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "genero": genero,
        "estado_civil": estado_civil
    }

    pacientes.append(paciente)

    guardar_json(ARCHIVO, pacientes)

    print("\n¡Paciente registrado correctamente!")