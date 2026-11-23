from datetime import datetime
from almacenamiento import leer_json, guardar_json

ARCHIVO_PACIENTES = "pacientes.json"
ARCHIVO_CONSULTAS = "diagnosticos.json"


def crear_consulta(usuario):

    pacientes = leer_json(ARCHIVO_PACIENTES)

    print("\n--- REGISTRO DE DIAGNÓSTICO ---")

    identificacion = input("Identificación del paciente: ")

    paciente = None

    for p in pacientes:
        if p["identificacion"] == identificacion:
            paciente = p
            break

    if paciente is None:
        print("Paciente no encontrado.")
        return

    sintomas = input("Síntomas del paciente: ")
    diagnostico = input("Diagnóstico registrado por el médico: ")

    print("\n--- PRESCRIPCIÓN MÉDICA ---")

    medicamento = input("Medicamento: ")
    cantidad = input("Cantidad: ")
    dosis = input("Dosis indicada por el médico: ")
    tiempo = input("Tiempo de tratamiento: ")

    consulta = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "paciente_id": identificacion,
        "paciente": paciente["nombres"] + " " + paciente["apellidos"],
        "medico": usuario["nombres"] + " " + usuario["apellidos"],
        "sintomas": sintomas,
        "diagnostico": diagnostico,
        "prescripcion": {
            "medicamento": medicamento,
            "cantidad": cantidad,
            "dosis": dosis,
            "tiempo": tiempo
        }
    }

    consultas = leer_json(ARCHIVO_CONSULTAS)
    consultas.append(consulta)

    guardar_json(ARCHIVO_CONSULTAS, consultas)

    print("\n¡Consulta registrada correctamente!")


def ver_historia_clinica():

    pacientes = leer_json(ARCHIVO_PACIENTES)
    consultas = leer_json(ARCHIVO_CONSULTAS)

    print("\n--- HISTORIA CLÍNICA ---")

    identificacion = input("Identificación del paciente: ")

    paciente = None

    for p in pacientes:
        if p["identificacion"] == identificacion:
            paciente = p
            break

    if paciente is None:
        print("Paciente no encontrado")
        return

    print("\n========== DATOS DEL PACIENTE ==========")
    print("Nombre:", paciente["nombres"], paciente["apellidos"])
    print("Identificación:", paciente["identificacion"])
    print("Teléfono:", paciente["telefono"])
    print("Correo electrónico:", paciente["email"])
    print("Dirección:", paciente["direccion"])
    print("Género:", paciente["genero"])
    print("Estado civil:", paciente["estado_civil"])

    print("\nHISTORIAL DE CONSULTAS")

    encontrado = False

    for consulta in consultas:
        if consulta["paciente_id"] == identificacion:
            encontrado = True

            print("\nFecha:", consulta["fecha"])
            print("Síntomas:", consulta["sintomas"])
            print("Diagnóstico:", consulta["diagnostico"])
            print("Médico:", consulta["medico"])
            print("Medicamento:", consulta["prescripcion"]["medicamento"])
            print("Dosis:", consulta["prescripcion"]["dosis"])

    if not encontrado:
        print("Este paciente no tiene consultas registradas.")
        